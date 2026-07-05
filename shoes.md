---
layout: page
title: Shoes
permalink: /shoes/
---

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox/dist/css/glightbox.min.css">

<style>
.shoe-grid{
  display:grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  align-items:start;
}
@media (max-width: 900px){
  .shoe-grid{ grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 520px){
  .shoe-grid{ grid-template-columns: repeat(1, minmax(0, 1fr)); }
}

.shoe-card{
  position:relative;
  width:100%;
  aspect-ratio: 1 / 1;
  overflow:hidden;
  border-radius: 14px;
  background:#f3f3f3;
  display:block;
  padding:0;
  border:none;
  cursor:pointer;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);
  text-align:left;
}
.shoe-card img{
  width:100%;
  height:100%;
  object-fit:cover;
  transform: scale(1.02);
  transition: transform .25s ease;
  display:block;
}
.shoe-card:hover img{ transform: scale(1.06); }

.shoe-label{
  position:absolute;
  left:10px;
  bottom:10px;
  padding:6px 10px;
  border-radius: 999px;
  background: rgba(0,0,0,0.55);
  color:#fff;
  font-size: 14px;
  line-height: 1;
  backdrop-filter: blur(6px);
}

.shoe-count{
  position:absolute;
  right:10px;
  top:10px;
  min-width:28px;
  height:28px;
  padding:0 8px;
  border-radius:999px;
  background: rgba(0,0,0,0.55);
  color:#fff;
  font-size: 13px;
  font-weight: 600;
  display:flex;
  align-items:center;
  justify-content:center;
  backdrop-filter: blur(6px);
  z-index: 2;
  pointer-events:none;
}

.shoe-expand{
  grid-column: 1 / -1;
  border-radius: 14px;
  background: #f7f7f7;
  border: 1px solid rgba(0,0,0,0.06);
  padding: 12px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.thumb-row{
  display:flex;
  gap: 10px;
  overflow-x:auto;
  padding-bottom: 4px;
  -webkit-overflow-scrolling: touch;
  scroll-snap-type: x mandatory;
}
.thumb-row::-webkit-scrollbar{ height: 8px; }
.thumb-row::-webkit-scrollbar-thumb{
  background: rgba(0,0,0,0.15);
  border-radius: 999px;
}

.thumb{
  flex: 0 0 auto;
  width: 120px;
  aspect-ratio: 1 / 1;
  border-radius: 12px;
  overflow:hidden;
  background:#eaeaea;
  display:block;
  scroll-snap-align: start;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.thumb img{
  width:100%;
  height:100%;
  object-fit:cover;
  display:block;
  transition: transform .2s ease;
}
.thumb:hover img{ transform: scale(1.05); }

.expand-hint{
  font-size: 14px;
  color: rgba(0,0,0,0.6);
  margin: 0 0 10px 0;
}
</style>

{% assign shoe_collections = "kobe-x|Kobe X,vomero-plus|Vomero Plus,07042026-collection|07042026 Collection" | split: "," %}

<div class="shoe-grid">
  {% for item in shoe_collections %}
    {% assign parts = item | split: "|" %}
    {% assign slug = parts[0] %}
    {% assign title = parts[1] %}
    {% assign folder_prefix = "/assets/img/shoes/" | append: slug | append: "/" %}
    {% assign images = site.static_files | where_exp: "file", "file.path contains folder_prefix" | sort: "name" %}
    {% assign cover = images | first %}

    <button class="shoe-card shoe-toggle" type="button" data-target="{{ slug }}" aria-expanded="false" aria-controls="expand-{{ slug }}">
      <img src="{{ cover.path | relative_url }}" alt="{{ title }} cover">
      <span class="shoe-count">{{ images | size }}</span>
      <span class="shoe-label">{{ title }}</span>
    </button>

    <div id="expand-{{ slug }}" class="shoe-expand" hidden>
      <p class="expand-hint">Click a thumbnail to view large.</p>
      <div class="thumb-row">
        {% for image in images %}
          <a class="thumb glightbox"
             href="{{ image.path | relative_url }}"
             data-gallery="{{ slug }}"
             data-title="{{ title }}">
            <img src="{{ image.path | relative_url }}" alt="{{ title }} {{ forloop.index }}">
          </a>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>

<script src="https://cdn.jsdelivr.net/npm/glightbox/dist/js/glightbox.min.js"></script>
<script>
  GLightbox({ selector: '.glightbox', touchNavigation: true, loop: true });

  document.querySelectorAll('.shoe-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const key = btn.dataset.target;
      const panel = document.getElementById('expand-' + key);
      const isOpen = !panel.hasAttribute('hidden');

      document.querySelectorAll('.shoe-expand').forEach(p => p.setAttribute('hidden', ''));
      document.querySelectorAll('.shoe-toggle').forEach(b => b.setAttribute('aria-expanded', 'false'));

      if (!isOpen) {
        panel.removeAttribute('hidden');
        btn.setAttribute('aria-expanded', 'true');
        panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      } else {
        panel.setAttribute('hidden', '');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  });
</script>
