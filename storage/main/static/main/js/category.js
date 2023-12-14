let errorImages = document.querySelectorAll('.image');
    errorImages.forEach(function(image, index) {
        image.onerror = function() {
          image.src = image.src.replace("400x400.jpg", '420x420.png');
          image.onerror = function (){
            image.src = image.src.replace('420.png', '420.jpg');
            image.onerror = function (){
              image.src = image.src.replace('420.jpg', '420.jpeg');
              image.onerror = function (){
                image.src = image.src.replace('jpg.webp', 'jpeg.webp');
                }
            }
          }
        };
    });