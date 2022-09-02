---
title: Publications
layout: content_page
---

# Publications
The following publications make use of RSS packages. If there's a paper we're missing, or you've recently published a paper using an RSS package, please [let us know!](/contact.html)

{% for pub in site.data.publications %}
 - [{{ pub.title }}]({{ pub.url}}). {{ pub.authors }}. *{{ pub.info }}*
{% endfor %}

## Citing RSS packages

Information about citing RSS packages coming soon! In the mean time, if you're using an RSS package in your work, please [reach out to us directly](/contact.html)
