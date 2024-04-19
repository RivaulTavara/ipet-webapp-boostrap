<?php
if(!empty($_POST["registro"])){
  if (!empty($_POST["nombre"]) or empty($_POST["apellido"] )or empty($_POST["contrasena"]) or empty($_POST["fechaNacimiento"]) or empty($_POST["telefono"])
   or empty($_POST["region"]) or empty($_POST["nivelEducacional"]) or empty($_POST["telefono"]) or empty($_POST["region"]) or empty($_POST["nivelEducacional"]) 
   or empty($_POST["rut"]) or empty($_POST["correo"])){
    echo 'Por favor, rellene todos los campos.';
  } else {

  }
}
?>