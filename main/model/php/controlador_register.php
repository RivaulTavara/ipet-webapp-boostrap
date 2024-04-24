<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

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
    echo 'Por favor, rellene todos los campos.';
  } else {
    $servername = "localhost";
    $username = "root";
    $dbPassword = ""; // Cambiado a $dbPassword
    $dbname = "ipet";

    // Create connection
    $conn = new mysqli($servername, $username, $dbPassword, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("La conexión ha fallado: " . $conn->connect_error);
    }

    // Consulta SQL para insertar los datos
    $sql = "INSERT INTO USUARIO (rut, correo, nombre, apellido, contrasena, direccion, fecha_de_nacimiento, telefono, region, nivel_educacional) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

    $stmt = $conn->prepare($sql);
    $stmt->bind_param('ssssssssss', $rut, $correo, $nombre, $apellido, $userPassword, $direccion, $fechaNacimiento, $telefono, $region, $nivelEducacional);

    // Ejecutar la consulta
    if ($stmt->execute()) {
      // Iniciar la sesión
      if (session_status() == PHP_SESSION_NONE) {
        session_start();
      }

      // Establecer $_SESSION['rut'] y $_SESSION['NOMBRE']
      $_SESSION['rut'] = $rut;
      $_SESSION['NOMBRE'] = $nombre;

      // Redirigir a usuario.php
      header("Location: ../../usuario.html");
      exit;
    } else {
      echo "Error: " . $stmt->error;
    }

    // Cerrar la conexión
    $conn->close();
  }
}
?>