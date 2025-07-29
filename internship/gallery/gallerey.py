<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Image Gallery</title>
  <style>
    body { font-family: Arial; margin: 0; padding: 0; }
    .gallery { display: flex; flex-wrap: wrap; gap: 10px; padding: 10px; justify-content: center; }
    .gallery img { width: 200px; height: 150px; object-fit: cover; cursor: pointer; transition: transform 0.3s ease; }
    .gallery img:hover { transform: scale(1.05); }
    .lightbox { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); display: flex; justify-content: center; align-items: center; display: none; }
    .lightbox img { max-width: 90%; max-height: 90%; }
  </style>
</head>
<body>
  <div class="gallery">
    <img src="https://via.placeholder.com/200" onclick="openLightbox(this.src)">
    <img src="https://via.placeholder.com/201" onclick="openLightbox(this.src)">
    <img src="https://via.placeholder.com/202" onclick="openLightbox(this.src)">
  </div>
  <div class="lightbox" onclick="this.style.display='none'">
    <img id="lightbox-img">
  </div>
  <script>
    function openLightbox(src) {
      document.getElementById('lightbox-img').src = src;
      document.querySelector('.lightbox').style.display = 'flex';
    }
  </script>
</body>
</html>
