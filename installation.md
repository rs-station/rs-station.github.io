---
title: Installation
layout: content_page
---

# How to install

All of the Reciprocal Space Station packages are `pip`-installable, e.g.:

```bash
pip install reciprocalspaceship
```

We recommend that you use a package manager such as [`conda`](https://docs.conda.io/en/latest/) and always install into a fresh environment, e.g.:

```bash
conda create -n my-new-careless-environment
conda activate my-new-careless-environment
pip install careless
```

## Development builds

If you're looking for a version of the software that's newer than the latest version published to PyPI, you can alternatively install directly from source:

```bash
pip install git+https://github.com/rs-station/rs-booster.git
```

or if you want to develop yourself and use your own custom version, you can clone the source code:

```bash
git clone https://github.com/rs-station/rs-booster.git
cd rs-booster
pip install -e .
```

## Companion software

The pure-python dependencies of RSS packages (`numpy`, `pandas`, `gemmi`, etc.) will be downloaded automatically when you use `pip`. However, some functionality (e.g. [`rs.scaleit`](https://rs-station.github.io/rs-booster/misc.html#id1) from `rs-booster`) is just a wrapper around other software (in this case, [`CCP4`](https://www.ccp4.ac.uk/download/#os=mac)) which does need to be installed separately. Hopefully, some day soon, software such as `CCP4` and `phenix` will follow the lead of `dials`, `gemmi`, `cctbx`, and more and become `pip`/`conda`-installable!