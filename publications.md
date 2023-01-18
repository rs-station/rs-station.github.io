---
title: Publications
layout: content_page
---

# Publications
The following publications make use of RSS packages. If there's a paper we're missing, or you've recently published a paper using an RSS package, please [let us know!](/contact.html)

{% for pub in site.data.publications %}
 - [{{ pub.title }}]({{ pub.url}}). {{ pub.authors }}. *{{ pub.info }}*
{% endfor %}
---
## How to cite
If you're making use of any RSS packages, amazing! Please cite them as follows:

### ReciprocalSpaceship
{% assign rspub = site.data.publications | where: "nickname", "rs" %}
{% for pub in rspub %}
[{{ pub.title }}]({{ pub.url}}). {{ pub.authors }}. *{{ pub.info }}*
{% endfor %}

### Careless
{% assign clpub = site.data.publications | where: "nickname", "careless" %}
{% for pub in clpub %}
[{{ pub.title }}]({{ pub.url}}). {{ pub.authors }}. *{{ pub.info }}*
{% endfor %}

### RS-booster
[Cite GitHub directly](https://github.com/rs-station/rs-booster)