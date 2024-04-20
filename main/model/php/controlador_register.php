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
  $userPassword = $_POST["password"]; // Cambiado a $userPassword
  $direccion = $_POST["direccion"];
  $fechaNacimiento = date('Y-m-d', strtotime($_POST["fechaNacimiento"]));
  $telefono = $_POST["telefono"];
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
    } else {
        echo "Conexión exitosa";
    }

    // Consulta SQL para insertar los datos
    $sql = "INSERT INTO USUARIO (rut, correo, nombre, apellido, contrasena, direccion, fecha_de_nacimiento, telefono, region, nivel_educacional) VALUES ('$rut', '$correo', '$nombre', '$apellido', '$userPassword', '$direccion', '$fechaNacimiento', '$telefono', '$region', '$nivelEducacional')";

    // Ejecutar la consulta
    if ($conn->query($sql) === TRUE) {
      echo "Nuevo registro creado con éxito";
    } else {
      echo "Error: " . $sql . "<br>" . $conn->error;
    }

    // Cerrar la conexión
    $conn->close();
  }
}
?>