---
layout: page
title: Shoes
permalink: /shoes/
---

<style>
  .shoe-grid{
    display:grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
  }
  @media (max-width: 900px){
    .shoe-grid{ grid-template-columns: repeat(2, minmax(0, 1fr)); }
  }
  @media (max-width: 520px){
    .shoe-grid{ grid-template-columns: repeat(1, minmax(0, 1fr)); }
  }

  .shoe-card{
    position:relative;
    aspect-ratio: 1 / 1;
    overflow:hidden;
    border-radius: 14px;
    background:#f3f3f3;
    display:block;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
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

  /* 右上角：相册叠片 + 数量角标 */
  .shoe-count{
    position:absolute;
    right:10px;
    top:10px;
    width:28px;
    height:28px;
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
  }
  /* 小叠片效果（像相册） */
  .shoe-card::before,
  .shoe-card::after{
    content:"";
    position:absolute;
    right:12px;
    top:12px;
    width:26px;
    height:26px;
    border-radius:8px;
    border:1px solid rgba(255,255,255,0.65);
    background: rgba(0,0,0,0.08);
    z-index:1;
    pointer-events:none;
  }
  .shoe-card::before{ transform: translate(4px, -4px); opacity: .55; }
  .shoe-card::after { transform: translate(2px, -2px); opacity: .75; }
</style>

<div class="shoe-grid">

  <!-- ================= Kobe X ================= -->
  <a
    class="shoe-card glightbox"
    href="{{ '/assets/img/shoes/kobe-x/1.JPG' | relative_url }}"
    data-gallery="kobe-x"
    data-title="Kobe X"
  >
    <img src="{{ '/assets/img/shoes/kobe-x/1.JPG' | relative_url }}" alt="Kobe X cover">

    <!-- 角标：图片数量 -->
    <span class="shoe-count">5</span>

    <span class="shoe-label">Kobe X</span>
  </a>

  <!-- 其余图片：隐藏，但进入同一画廊 -->
  <a class="glightbox" style="display:none"
     href="{{ '/assets/img/shoes/kobe-x/2.JPG' | relative_url }}"
     data-gallery="kobe-x"
     data-title="Kobe X"></a>

  <a class="glightbox" style="display:none"
     href="{{ '/assets/img/shoes/kobe-x/3.JPG' | relative_url }}"
     data-gallery="kobe-x"
     data-title="Kobe X"></a>

  <a class="glightbox" style="display:none"
     href="{{ '/assets/img/shoes/kobe-x/4.JPG' | relative_url }}"
     data-gallery="kobe-x"
     data-title="Kobe X"></a>

  <a class="glightbox" style="display:none"
     href="{{ '/assets/img/shoes/kobe-x/5.JPG' | relative_url }}"
     data-gallery="kobe-x"
     data-title="Kobe X"></a>

</div>

<!-- GLightbox (CDN) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox/dist/css/glightbox.min.css">
<script src="https://cdn.jsdelivr.net/npm/glightbox/dist/js/glightbox.min.js"></script>
<script>
  GLightbox({
    selector: '.glightbox',
    touchNavigation: true,
    loop: true
  });
</script>
