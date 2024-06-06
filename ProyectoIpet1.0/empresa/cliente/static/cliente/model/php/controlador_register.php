<?php
session_start(); // Mover esto al principio

include 'config.php';

if($_SERVER["REQUEST_METHOD"] == "POST"){
  // Recoger los datos del formulario
  $rut = $_POST["rut"];
  $correo = $_POST["correo"];
  $nombre = $_POST["nombre"];
  $apellido = $_POST["apellido"];
  $userPassword = password_hash($_POST["password"], PASSWORD_DEFAULT); // Hash de la contraseña
  $fechaNacimiento = date('Y-m-d', strtotime($_POST["fechaNacimiento"]));
  $telefono = $_POST["telefono"];
  $direccion = $_POST["direccion"];
  $region = $_POST["region"];
  $nivelEducacional = $_POST["nivelEducacional"];

  // Comprobar que todos los campos están llenos
  if (empty($rut) || empty($correo) || empty($nombre) || empty($apellido) || empty($userPassword) || empty($direccion) || empty($fechaNacimiento) || empty($telefono) || empty($region) || empty($nivelEducacional)) {
    echo json_encode(['error' => 'Por favor, rellene todos los campos.']);
  } else {
    // Consulta SQL para insertar los datos
    $sql = "INSERT INTO USUARIO (rut, correo, nombre, apellido, contrasena, direccion, fecha_de_nacimiento, telefono, region, nivel_educacional) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

    $stmt = $conn->prepare($sql);
    $stmt->bind_param('ssssssssss', $rut, $correo, $nombre, $apellido, $userPassword, $direccion, $fechaNacimiento, $telefono, $region, $nivelEducacional);

    // Ejecutar la consulta
    if ($stmt->execute()) {
      // Establecer las variables de sesión
      $_SESSION['rut'] = $rut;
      $_SESSION['NOMBRE'] = $nombre;

      // Redirigir al usuario a la página deseada
      header("Location: ../../usuario.html");

      // No olvides cerrar la conexión a la base de datos
      $conn->close();
    } else {
      echo json_encode(['error' => "Error: " . $stmt->error]);
    }
  }
}
?>