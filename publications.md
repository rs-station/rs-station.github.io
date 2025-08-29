---
title: Publications
layout: content_page
---

# Citing Reciprocal Space Station packages
If you're making use of any RSS packages, amazing! Please cite them as follows:

{% for pub in site.data.publications %}
{% if pub.section == "cite" %}
### {{ pub.package }}
[{{ pub.title }}]({{ pub.url}}). {{ pub.authors }}. *{{ pub.info }}*
{% endif %}
{% endfor %}


# RSS in other publications 
The following publications explore, expand upon, or apply RSS packages. If there's a paper we're missing, or you've recently published a paper using an RSS package, please [let us know!](/contact.html)

{% for pub in site.data.publications %}
{% if pub.section == "pubs" %}
 - [{{ pub.title }}]({{ pub.url}}). {{ pub.authors }}. *{{ pub.info }}*
{% endif %}
{% endfor %}

---
