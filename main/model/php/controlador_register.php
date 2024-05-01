<?php
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

  // Genera un valor para 'salt'. Esto es solo un ejemplo, debes generar un valor seguro para 'salt' en un entorno de producción.
  $salt = md5(uniqid(rand(), true));

  // Comprobar que todos los campos están llenos
  if (empty($rut) || empty($correo) || empty($nombre) || empty($apellido) || empty($userPassword) || empty($direccion) || empty($fechaNacimiento) || empty($telefono) || empty($region) || empty($nivelEducacional)) {
    echo json_encode(['error' => 'Por favor, rellene todos los campos.']);
  } else {
    // Consulta SQL para insertar los datos
    $sql = "INSERT INTO USUARIO (rut, correo, nombre, apellido, contrasena, salt, direccion, fecha_de_nacimiento, telefono, region, nivel_educacional) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

    $stmt = $conn->prepare($sql);
    $stmt->bind_param('sssssssssss', $rut, $correo, $nombre, $apellido, $userPassword, $salt, $direccion, $fechaNacimiento, $telefono, $region, $nivelEducacional);

    // Ejecutar la consulta
    if ($stmt->execute()) {
      // Iniciar la sesión
      if (session_status() == PHP_SESSION_NONE) {
        session_start();
      }

      // Establecer $_SESSION['rut'] y $_SESSION['NOMBRE']
      $_SESSION['rut'] = $rut;
      $_SESSION['NOMBRE'] = $nombre;

      // Devolver una respuesta exitosa
      echo json_encode(['success' => 'Registro exitoso.']);
    } else {
      echo json_encode(['error' => "Error: " . $stmt->error]);
    }
    
    header("Location: ../../usuario.html");
    // Cerrar la conexión
    $conn->close();
  }
}
?>