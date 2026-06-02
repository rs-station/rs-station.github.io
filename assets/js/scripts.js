document.addEventListener('DOMContentLoaded', function () {

  /* ── Transparent → opaque navbar on hero page ─────────────────
     When a .hero-section is present, start navbar transparent
     and fade it in as the user scrolls past the hero.           */
  var navbar = document.querySelector('.navbar');
  var heroSection = document.querySelector('.hero-section');
  var heroOverlay = document.querySelector('.hero-overlay');
  if (navbar && heroSection) {
    navbar.classList.add('navbar-hero');
    function updateOnScroll() {
      var y = window.scrollY;

      // Navbar: transparent at top, opaque after scrolling
      if (y > 60) {
        navbar.classList.add('navbar-scrolled');
      } else {
        navbar.classList.remove('navbar-scrolled');
      }

      // Hero dark overlay: full at top, gone by the time the hero is scrolled past
      if (heroOverlay) {
        var fadeDistance = heroSection.offsetHeight * 0.6;
        var opacity = 1 - (y / fadeDistance);
        heroOverlay.style.opacity = Math.max(0, Math.min(1, opacity));
      }
    }
    window.addEventListener('scroll', updateOnScroll, { passive: true });
    updateOnScroll();
  }

  /* ── Scroll reveal ─────────────────────────────────────────────
     .reveal elements fade + slide up when they enter the
     viewport. Uses IntersectionObserver (graceful no-op if
     unsupported).                                               */
  var revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length > 0 && 'IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(function (el) { revealObserver.observe(el); });
  }

  /* ── Scrollspy TOC sidebar ─────────────────────────────────────
     Dynamically builds a nav from page headings and activates
     Bootstrap ScrollSpy to highlight the current section.      */
  var content = document.getElementById('content-body');
  var tocNav  = document.getElementById('page-toc');
  var tocCol  = document.getElementById('toc-col');
  if (!content || !tocNav) return;

  var headings = Array.from(content.querySelectorAll('h1, h2, h3'));

  if (headings.length < 2) {
    if (tocCol) {
      tocCol.style.display = 'none';
      content.classList.remove('col-lg-9', 'offset-lg-0');
      content.classList.add('col-lg-8', 'offset-lg-2');
    }
    return;
  }

  /* Strip emoji, variation selectors (U+FE0E/FE0F) and zero-width joiners,
     then drop any leading non-letter junk (e.g. the "1/" brand prefix). */
  var emojiRe = /[\p{Emoji_Presentation}\p{Extended_Pictographic}\uFE0E\uFE0F\u200D]/gu;
  function cleanLabel(text) {
    return text
      .replace(emojiRe, '')
      .replace(/^[^\p{L}]+/u, '')
      .trim();
  }

  headings.forEach(function (h) {
    var label = cleanLabel(h.textContent);

    if (!h.id) {
      h.id = label
        .toLowerCase()
        .replace(/[^\w\s-]/g, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-')
        .replace(/^-|-$/g, '');
    }

    var a = document.createElement('a');
    a.className = 'nav-link toc-' + h.tagName.toLowerCase();
    a.href = '#' + h.id;
    a.textContent = label;
    tocNav.appendChild(a);
  });

  new bootstrap.ScrollSpy(document.body, {
    target: '#page-toc',
    rootMargin: '0px 0px -55%'
  });

});
