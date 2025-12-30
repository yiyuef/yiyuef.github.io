---
layout: page
title: Notes
permalink: /notes/
---

{% assign notes = site.notes | sort: "date" | reverse %}
<ul>
  {% for n in notes %}
    <li><a href="{{ n.url | relative_url }}">{{ n.title }}</a></li>
  {% endfor %}
</ul>
