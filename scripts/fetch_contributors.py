#!/usr/bin/env python3
"""Aggregate contributors across all public rs-station repos into _data/contributors.json.

Uses only the Python standard library. Reads an optional GITHUB_TOKEN from the
environment to raise the API rate limit (the data itself is public, so a token is
not required — unauthenticated runs just hit the 60 req/hr limit).

Run locally with:  GITHUB_TOKEN=$(gh auth token) python3 scripts/fetch_contributors.py
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

ORG = "rs-station"
API = "https://api.github.com"

# Repo root is the parent of this script's directory.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEAM_YML = os.path.join(ROOT, "_data", "team.yml")
OUT_PATH = os.path.join(ROOT, "_data", "contributors.json")

# Bot accounts that aren't flagged as type=="Bot" or suffixed with "[bot]".
BOT_DENYLIST = {
    "renovate-bot",
    "copilot",
    "dependabot",
    "github-actions",
    "pre-commit-ci",
    "allcontributors",
}


def gh_get(path):
    """GET an absolute or API-relative GitHub URL, returning parsed JSON."""
    url = path if path.startswith("http") else API + path
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "rs-station-contributors-script")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def paginate(path):
    """Yield items across all pages of a list endpoint."""
    page = 1
    sep = "&" if "?" in path else "?"
    while True:
        batch = gh_get(f"{path}{sep}per_page=100&page={page}")
        if not batch:
            break
        for item in batch:
            yield item
        if len(batch) < 100:
            break
        page += 1


def core_logins():
    """Logins listed in _data/team.yml (lowercased), parsed without PyYAML."""
    logins = set()
    try:
        with open(TEAM_YML, encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r"\s*github:\s*(\S+)", line)
                if m:
                    logins.add(m.group(1).strip().strip("\"'").lower())
    except FileNotFoundError:
        pass
    return logins


def is_bot(login, ctype):
    login_l = login.lower()
    return ctype == "Bot" or login_l.endswith("[bot]") or login_l in BOT_DENYLIST


def main():
    excluded = core_logins()
    # login -> aggregated record
    people = {}

    for repo in paginate(f"/orgs/{ORG}/repos?type=public"):
        if repo.get("fork"):
            continue
        name = repo["name"]
        try:
            contributors = list(paginate(f"/repos/{ORG}/{name}/contributors?anon=0"))
        except urllib.error.HTTPError as e:
            # Empty repos return 204/no contributors; skip quietly.
            print(f"  skipping {name}: {e}", file=sys.stderr)
            continue
        for c in contributors:
            login = c.get("login")
            if not login or is_bot(login, c.get("type", "")):
                continue
            if login.lower() in excluded:
                continue
            rec = people.setdefault(
                login,
                {
                    "login": login,
                    "avatar_url": c.get("avatar_url", ""),
                    "html_url": c.get("html_url", ""),
                    "contributions": 0,
                },
            )
            rec["contributions"] += c.get("contributions", 0)

    # Resolve display names (best effort).
    for login, rec in people.items():
        try:
            user = gh_get(f"/users/{login}")
            rec["name"] = user.get("name") or login
        except urllib.error.HTTPError:
            rec["name"] = login

    ordered = sorted(
        people.values(), key=lambda r: (-r["contributions"], r["login"].lower())
    )

    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(ordered, fh, indent=2, sort_keys=True)
        fh.write("\n")

    print(f"Wrote {len(ordered)} contributors to {OUT_PATH}")


if __name__ == "__main__":
    main()
