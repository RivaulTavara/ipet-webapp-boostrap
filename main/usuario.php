<?php
include 'model/php/user_view.php';
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <title>IPet</title>
    <link rel="stylesheet" href="style.css">
  </head>   
<body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" style="background-color: var(--navbar-color);">
        <div class="container-fluid">
          <a class="navbar-brand no-transition" href="main.html" style="font-size: xx-large;">
            <img src="src/logo.png" alt="IPet" width="35px" height="35px">
            IPet
        </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link"  href="main.html#productos" style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Productos Destacados</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="main.html#galeria" style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Galería de Productos</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="inicioSesion.html" style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Iniciar Sesión</a>
              <li class="nav-item">
                <a class="nav-link" href="registro.html" style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Registro de Usuarios</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#pie-pag" style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">¿Quiénes somos?</a>
              </li>
              <li class="nav-item d-none d-md-block">
                <a class="nav-link" href="carrito.html">
                  <i class="fas fa-shopping-cart" style="list-style: none; padding-left: 400px; "></i>
                </a>
              </li>              
              <li class="nav-item d-block d-md-none">
                <a class="nav-link" href="carrito.html">
                  <i class="fas fa-shopping-cart"></i>
                </a>
              </li>
              </ul>
          </div>
        </div>
      </nav>

      <div class="form-login" style="margin-top: 100px;">
        <div class="text-center">
        <div class="container">
            <h1>🐶😺</h1>
            <h2>Bienvenido, <?php echo (isset($user['nombre']) ? $user['nombre'] : '') . ' ' . (isset($user['apellido']) ? $user['apellido'] : ''). '!' ; ?></h2>
            <p>RUT: <?php echo $user['rut']; ?></p>
            <p>Correo: <?php echo $user['correo']; ?></p>
            <p>Nombre(s): <?php echo $user['nombre']; ?></p>
            <p>Apellido: <?php echo $user['apellido']; ?></p>
            <p>Dirección: <?php echo $user['direccion']; ?></p>
            <p>Fecha de Nacimiento: <?php echo $user['fecha_de_nacimiento']; ?></p>
            <p>Teléfono: <?php echo $user['telefono']; ?></p>
            <p>Región: <?php echo $user['region']; ?></p>
            <p>Nivel Educacional: <?php echo $user['nivel_educacional']; ?></p>
            <!-- Aquí puedes agregar más detalles del usuario -->
        </div> 
        </div>
      </div>
      
      <footer id="pie-pag">
      <div class="container mt-5">
        <div class="row">
          <div class="col-md-6">
            <h5>¿Quiénes somos?</h5>
            <p>Somos una tienda en línea especializada en productos para mascotas. Nuestro objetivo es brindar a los dueños de mascotas los mejores productos y servicios para el cuidado y bienestar de sus compañeros peludos.</p>
          </div>
          <div class="col-md-6">
            <h5>Contacto</h5>
            <p>Dirección: 1153 Las Calilas, Santiago, Chile</p>
            <p>Teléfono: +56983672634</p>
            <p>Email: fullinfo@ipet.cl</p>
          </div>
        </div>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <hr>
            <p class="text-center">© 2022 iPet. Todos los derechos reservados.</p>
          </div>
        </div>
      </div>
    </footer>
</body>
</html>