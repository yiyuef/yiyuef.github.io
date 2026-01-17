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
    align-items:start;
  }
  @media (max-width: 900px){
    .shoe-grid{ grid-template-columns: repeat(2, minmax(0, 1fr)); }
  }
  @media (max-width: 520px){
    .shoe-grid{ grid-template-columns: repeat(1, minmax(0, 1fr)); }
  }

  /* 封面卡片（用 button，点击只负责展开/收起） */
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

  /* 右上角：数量角标 */
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
    pointer-events:none;
  }

  /* 展开区域：占满整行，出现在封面卡片下方 */
  .shoe-expand{
    grid-column: 1 / -1;
    border-radius: 14px;
    background: #f7f7f7;
    border: 1px solid rgba(0,0,0,0.06);
    padding: 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
  }

  /* 缩略图横向滑动条（手机可直接左右滑） */
  .thumb-row{
    display:flex;
    gap: 10px;
    overflow-x:auto;
    padding-bottom: 4px;
    -webkit-overflow-scrolling: touch;
    scroll-snap-type: x mandatory;
  }
  .thumb-row::-webkit-scrollbar{ height: 8px; }
  .thumb-row::-webkit-scrollbar-thumb{ background: rgba(0,0,0,0.15); border-radius: 999px; }

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

<div class="shoe-grid">

  <!-- ================= Kobe X（封面：展开/收起） ================= -->
  <button
    class="shoe-card shoe-toggle"
    type="button"
    data-target="kobe-x"
    aria-expanded="false"
    aria-controls="expand-kobe-x"
  >
    <img src="{{ '/assets/img/shoes/kobe-x/1.JPG' | relative_url }}" alt="Kobe X cover">
    <span class="shoe-count">5</span>
    <span class="shoe-label">Kobe X</span>
  </button>

  <!-- 展开区：默认收起（hidden） -->
  <div class="shoe-expand" id="expand-kobe-x" hidden>
    <p class="expand-hint">Click a thumbnail to view large.</p>

    <div class="thumb-row">
      <a class="thumb glightbox"
         href="{{ '/assets/img/shoes/kobe-x/1.JPG' | relative_url }}"
         data-gallery="kobe-x"
         data-title="Kobe X">
        <img src="{{ '/assets/img/shoes/kobe-x/1.JPG' | relative_url }}" alt="Kobe X 1">
      </a>

      <a class="thumb glightbox"
         href="{{ '/assets/img/shoes/kobe-x/2.JPG' | relative_url }}"
         data-gallery="kobe-x"
         data-title="Kobe X">
        <img src="{{ '/assets/img/shoes/kobe-x/2.JPG' | relative_url }}" alt="Kobe X 2">
      </a>

      <a class="thumb glightbox"
         href="{{ '/assets/img/shoes/kobe-x/3.JPG' | relative_url }}"
         data-gallery="kobe-x"
         data-title="Kobe X">
        <img src="{{ '/assets/img/shoes/kobe-x/3.JPG' | relative_url }}" alt="Kobe X 3">
      </a>

      <a class="thumb glightbox"
         href="{{ '/assets/img/shoes/kobe-x/4.JPG' | relative_url }}"
         data-gallery="kobe-x"
         data-title="Kobe X">
        <img src="{{ '/assets/img/shoes/kobe-x/4.JPG' | relative_url }}" alt="Kobe X 4">
      </a>

      <a class="thumb glightbox"
         href="{{ '/assets/img/shoes/kobe-x/5.JPG' | relative_url }}"
         data-gallery="kobe-x"
         data-title="Kobe X">
        <img src="{{ '/assets/img/shoes/kobe-x/5.JPG' | relative_url }}"
         alt="Kobe X 5">
      </a>
    </div>
  </div>

  <!-- 以后加新鞋：复制“button + div.expand”，把 data-target / id / 图片路径换掉即可 -->
  <!-- ================= Vomero Plus（封面：展开/收起） ================= -->
  <button
    class="shoe-card shoe-toggle"
    type="button"
    data-target="vomero-plus"
    aria-expanded="false"
    aria-controls="expand-vomero-plus"
  >
    <img src="{{ '/assets/img/shoes/vomero-plus/1.HEIC' | relative_url }}" alt="Vomero Plus cover">
    <span class="shoe-count">5</span>
    <span class="shoe-label">Vomero Plus</span>
  </button>

  <div class="shoe-expand" id="expand-vomero-plus" hidden>
    <p class="expand-hint">Click a thumbnail to view large.</p>

    <div class="thumb-row">
      <a class="thumb glightbox"
        href="{{ '/assets/img/shoes/vomero-plus/1.HEIC' | relative_url }}"
        data-gallery="vomero-plus"
        data-title="Vomero Plus"
        <img src="{{ '/assets/img/shoes/vomero-plus/1.HEIC' | relative_url }}" alt="Vomero Plus 1">
      </a>

      <a class="thumb glightbox"
        href="{{ '/assets/img/shoes/vomero-plus/2.HEIC' | relative_url }}"
        data-gallery="vomero-plus"
        data-title="Vomero Plus"
        <img src="{{ '/assets/img/shoes/vomero-plus/2.HEIC' | relative_url }}" alt="Vomero Plus 2">
      </a>

      <a class="thumb glightbox"
        href="{{ '/assets/img/shoes/vomero-plus/3.HEIC' | relative_url }}"
        data-gallery="vomero-plus"
        data-title="Vomero Plus"
        <img src="{{ '/assets/img/shoes/vomero-plus/3.HEIC' | relative_url }}" alt="Vomero Plus 3">
      </a>

      <a class="thumb glightbox"
        href="{{ '/assets/img/shoes/vomero-plus/4.HEIC' | relative_url }}"
        data-gallery="vomero-plus"
        data-title="Vomero Plus"
        <img src="{{ '/assets/img/shoes/vomero-plus/4.HEIC' | relative_url }}" alt="Vomero Plus 4">
      </a>

      <a class="thumb glightbox"
        href="{{ '/assets/img/shoes/vomero-plus/5.HEIC' | relative_url }}"
        data-gallery="vomero-plus"
        data-title="Vomero Plus"
        <img src="{{ '/assets/img/shoes/vomero-plus/5.HEIC' | relative_url }}" alt="Vomero Plus 5">
      </a>
    </div>
  </div>


</div>

<!-- 大图预览：只在点缩略图时触发 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox/dist/css/glightbox.min.css">
<script src="https://cdn.jsdelivr.net/npm/glightbox/dist/js/glightbox.min.js"></script>
<script>
  // 1) 缩略图点开大图
  GLightbox({
    selector: '.glightbox',
    touchNavigation: true,
    loop: true
  });

  // 2) 封面点击：展开/收起（默认一次只展开一个）
  document.querySelectorAll('.shoe-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const key = btn.dataset.target;
      const panel = document.getElementById('expand-' + key);
      const isOpen = !panel.hasAttribute('hidden');

      // 先收起其它展开区（你想允许多个同时展开的话，把这段删掉即可）
      document.querySelectorAll('.shoe-expand').forEach(p => p.setAttribute('hidden', ''));
      document.querySelectorAll('.shoe-toggle').forEach(b => b.setAttribute('aria-expanded', 'false'));

      // 再决定当前是展开还是收起
      if (!isOpen) {
        panel.removeAttribute('hidden');
        btn.setAttribute('aria-expanded', 'true');
        // 可选：展开后滚动到展开区，体验更像“下方展开”
        panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      } else {
        panel.setAttribute('hidden', '');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  });
</script>
