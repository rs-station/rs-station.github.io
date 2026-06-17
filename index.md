---
title: Home
layout: base_page
fullwidth: true
---

<!-- ═══════════════════════════════════════════════
     Wrapper: cover image spans hero + vision
     ═══════════════════════════════════════════════ -->
<div class="hero-vision-wrapper" style="background-image: url('{{ '/assets/data/reciprocal_space_station_cover.jpg' | relative_url }}')">

  <!-- HERO -->
  <section class="hero-section">
    <div class="hero-overlay" aria-hidden="true"></div>
    <div class="hero-content text-center">
      <img
        src="{{ '/assets/data/RSS_Worm_no_background.png' | relative_url }}"
        alt="Reciprocal Space Station"
        class="hero-logo mb-4"
      />
      <h1 class="hero-title">Reciprocal Space Station</h1>
      <p class="hero-subtitle">open-source structural biology for the AI era</p>
      <div class="hero-actions mt-4">
        <a class="btn btn-primary btn-sm" href="https://github.com/orgs/rs-station">
          <i class="fa-brands fa-github me-1"></i>GitHub
        </a>
        <a class="btn btn-outline-light btn-sm ms-2" href="{{ '/about.html' | relative_url }}">
          About us
        </a>
      </div>
    </div>
    <div class="scroll-hint">
      <span>Scroll</span>
      <i class="fa-solid fa-chevron-down fa-xs"></i>
    </div>
  </section>

  <!-- VISION -->
  <section class="vision-section">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-7 col-md-9 text-center">
          <p class="vision-label reveal">What we do</p>
          <h2 class="vision-heading reveal" style="transition-delay:.1s">
            Open science for the next generation of structural biology
          </h2>
          <p class="vision-text reveal" style="transition-delay:.2s">
            RSS is a new consortium developing an open-source ecosystem for methods spanning X-ray crystallography,
            cryo-EM/ET, SAXS, and the AI that increasingly connects structure to function.
            We're an open community that welcomes contributions from academics, industry,
            and non-profits across the world of structural biology.
          </p>
          <a class="btn btn-primary reveal mt-2" href="{{ '/about.html' | relative_url }}" style="transition-delay:.3s">
            Learn more
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Blur band softening the hero ↔ vision interface -->
  <div class="hero-vision-blur" aria-hidden="true"></div>

</div>

<!-- ═══════════════════════════════════════════════
     TABS — Software · Forum · Blog
     ═══════════════════════════════════════════════ -->
<section class="tabs-section">
  <div class="container">

    <ul class="nav rss-tabs" id="landingTabs" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" data-bs-toggle="tab"
                data-bs-target="#tab-software" type="button" role="tab" aria-selected="true">
          Software
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" data-bs-toggle="tab"
                data-bs-target="#tab-forum" type="button" role="tab" aria-selected="false">
          Forum
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" data-bs-toggle="tab"
                data-bs-target="#tab-blog" type="button" role="tab" aria-selected="false">
          Blog
        </button>
      </li>
    </ul>

    <div class="tab-content rss-tab-content" id="landingTabContent">

      <!-- ── Software ── -->
      <div class="tab-pane fade show active" id="tab-software" role="tabpanel">
        <div class="row gx-4 gy-4 mt-1">
          {% for card in site.data.packages %}
          {% if card.type == 'production' %}
          <div class="col-lg-4 col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">{{ card.name }}</h5>
                <p class="card-text small text-muted">{{ card.desc | markdownify | strip_html | truncate: 120 }}</p>
              </div>
              <div class="card-footer bg-transparent border-0 pb-3">
                {% if card.docs %}<a class="btn btn-outline-secondary btn-sm me-1" href="{{ card.docs }}">Docs</a>{% endif %}
                {% if card.examples %}<a class="btn btn-outline-secondary btn-sm me-1" href="{{ card.examples }}">Examples</a>{% endif %}
                <a class="btn btn-primary btn-sm" href="{{ card.link }}">GitHub</a>
              </div>
            </div>
          </div>
          {% endif %}
          {% endfor %}
          <div class="col-lg-4 col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">🛠️ Development Zone</h5>
                <p class="card-text small text-muted">More RSS packages under active development — use at your own risk!</p>
              </div>
              <div class="card-footer bg-transparent border-0 pb-3">
                <a class="btn btn-primary btn-sm" href="{{ '/software.html' | relative_url }}">See packages</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ── Forum ── -->
      <div class="tab-pane fade" id="tab-forum" role="tabpanel">
        <div class="tab-feature-pane text-center py-5">
          <i class="fa-regular fa-comments mb-4" style="font-size:2.75rem;color:var(--rss-blue);opacity:.85;"></i>
          <h3>Community Forum</h3>
          <p class="text-muted mb-4" style="max-width:460px;margin-inline:auto;">
            Ask questions, share ideas, and discuss crystallographic data analysis
            with the RS Station community on our open-source Discourse forum.
          </p>
          <a class="btn btn-primary" href="https://discourse.rs-station.org">Go to Forum</a>
        </div>
      </div>

      <!-- ── Blog ── -->
      <div class="tab-pane fade" id="tab-blog" role="tabpanel">
        <div class="blog-tab-list py-3">
          {% for post in site.posts limit:8 %}
          <a class="blog-tab-entry" href="{{ post.url | relative_url }}">
            <span class="blog-tab-date">{{ post.date | date: "%b %d, %Y" }}</span>
            <span class="blog-tab-title">{{ post.title }}</span>
          </a>
          {% endfor %}
          {% if site.posts.size == 0 %}
          <p class="text-muted py-3">No posts yet — check back soon.</p>
          {% endif %}
          <div class="mt-4">
            <a class="btn btn-outline-primary btn-sm" href="{{ '/blog.html' | relative_url }}">All posts →</a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
