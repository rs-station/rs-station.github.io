---
title: Publications
layout: content_page
---

# Citing Reciprocal Space Station packages
If you're making use of any RSS packages, amazing! Please cite them as follows:

{% assign cite_pubs = site.data.publications | where: "section", "cite" | sort_natural: "package" | group_by: "package" %}
{% for group in cite_pubs %}
### {{ group.name }}
{% for pub in group.items %}
[{{ pub.title }}]({{ pub.url}}). {{ pub.authors }}. *{{ pub.info }}*
{% endfor %}
{% for pub in group.items %}{% if pub.footnote %}
<small>{{ pub.footnote }}</small>
{% endif %}{% endfor %}
{% endfor %}


# RSS in other publications 
The following publications explore, expand upon, or apply RSS packages. If there's a paper we're missing, or you've recently published a paper using an RSS package, please [let us know!](/contact.html)

{% for pub in site.data.publications %}
{% if pub.section == "applications" %}
 - [{{ pub.title }}]({{ pub.url}}). {{ pub.authors }}. *{{ pub.info }}*
{% endif %}
{% endfor %}

---
