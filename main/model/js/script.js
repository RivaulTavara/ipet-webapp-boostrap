document.addEventListener('DOMContentLoaded', function() {
    var botones = document.querySelectorAll('.fas.fa-expand');

    botones.forEach(function(boton) {
        boton.addEventListener('click', function(event) {
            event.preventDefault();

            var imagenDeFondo = window.getComputedStyle(boton.closest('.part-1'), '::before').backgroundImage;
            var urlImagen = imagenDeFondo.slice(5, -2);
            var modal = document.createElement('div');
            modal.classList.add('modal');

            var contenidoModal = document.createElement('div');
            contenidoModal.classList.add('contenidoModal');

            var imagen = document.createElement('img');
            imagen.src = urlImagen;
            imagen.style.width = '440px';
            imagen.style.height = '480px';

            contenidoModal.appendChild(imagen);
            modal.appendChild(contenidoModal);

            modal.addEventListener('click', function(event) {
                if (event.target === modal) {
                    document.body.removeChild(modal);
                }
            });

            document.body.appendChild(modal);
        });
    });
});