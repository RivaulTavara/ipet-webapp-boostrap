<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "ipet";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $rut = $_POST['rut'];
  $correo = $_POST['correo'];
  $nombre = $_POST['nombre'];
  $apellido = $_POST['apellido'];
  $contrasena = $_POST['password'];
  $fechaNacimiento = $_POST['fechaNacimiento'];
  $telefono = $_POST['telefono'];
  $region = $_POST['region'];
  $nivelEducacional = $_POST['nivelEducacional'];

  $sql = "INSERT INTO USUARIO (rut, correo, nombre, apellido, contrasena, fecha_de_nacimiento, telefono, region, nivel_educacional)
  VALUES ('$rut', '$correo', '$nombre', '$apellido', '$contrasena', '$fechaNacimiento', '$telefono', '$region', '$nivelEducacional')";

  if ($conn->query($sql) === TRUE) {
    $_SESSION['message'] = "Usuario registrado con éxito";
    $_SESSION['msg_type'] = "success";
  } else {
    $_SESSION['message'] = "Error: " . $sql . "<br>" . $conn->error;
    $_SESSION['msg_type'] = "danger";
  }
}

$conn->close();
?>