---
title: Publications
layout: content_page
---

# Citing Reciprocal Space Station packages
If you're making use of any RSS packages, amazing! Please cite them as follows:

### reciprocalspaceship
{% assign rspub = site.data.publications | where: "nickname", "rs" %}
{% for pub in rspub %}
[{{ pub.title }}]({{ pub.url}}). **{{ pub.first_author }}**{{ pub.authors }}. *{{ pub.info }}*
{% endfor %}

### careless
{% assign clpub = site.data.publications | where: "nickname", "careless" %}
{% for pub in clpub %}
[{{ pub.title }}]({{ pub.url}}). **{{ pub.first_author }}**{{ pub.authors }}. *{{ pub.info }}*
{% endfor %}

### laue-dials
{% assign ldpub = site.data.publications | where: "nickname", "lauedials" %}
{% for pub in ldpub %}
[{{ pub.title }}]({{ pub.url}}). **{{ pub.first_author }}**{{ pub.authors }}. *{{ pub.info }}*
{% endfor %}

### matchmaps
{% assign mmpub = site.data.publications | where: "nickname", "matchmaps" %}
{% for pub in mmpub %}
[{{ pub.title }}]({{ pub.url}}). **{{ pub.first_author }}**{{ pub.authors }}. *{{ pub.info }}*
{% endfor %}

### SFCalculator
{% assign sfpub = site.data.publications | where: "nickname", "SFCalculator" %}
{% for pub in sfpub %}
[{{ pub.title }}]({{ pub.url}}). **{{ pub.first_author }}**{{ pub.authors }}. *{{ pub.info }}*
{% endfor %}

### abismal
[Cite GitHub directly](https://github.com/rs-station/abismal)

### rs-booster
[Cite GitHub directly](https://github.com/rs-station/rs-booster)


# RSS in other publications 
The following publications explore, expand upon, or apply RSS packages. If there's a paper we're missing, or you've recently published a paper using an RSS package, please [let us know!](/contact.html)

{% for pub in site.data.publications %}
{% if pub.section == "pubs" %}
 - [{{ pub.title }}]({{ pub.url}}), {{ pub.first_author }} et. al. *{{ pub.info }}*
{% endif %}
{% endfor %}

---
