<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Iniciar la sesión
session_start();

// Aquí puedes acceder a $_SESSION['rut']
$rut = $_SESSION['rut'];

// Conectar a la base de datos
$db = new mysqli('localhost', 'root', '', 'ipet');

// Verificar la conexión
if ($db->connect_error) {
    die("La conexión falló: " . $db->connect_error);
}

// Obtener los datos del usuario
$sql = "SELECT * FROM USUARIO WHERE RUT = ?";
$stmt = $db->prepare($sql);
$stmt->bind_param('s', $_SESSION['rut']);
$stmt->execute();
$result = $stmt->get_result();
$user = $result->fetch_assoc();



// Imprimir los datos del usuario en formato HTML
echo "<div class=\"form-login\" style=\"margin-top: 100px;\" id=\"datos-usuario\">" .
     "<div class=\"text-center\">" .
     "<div class=\"container\">" .
     "<h1>🐶😺</h1>" .
     "<h2>!Bienvenido a la familia IPet!</h2>" .
     "<div style=\"font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; font-size: large; text-align: center; padding-bottom: 50px;\" class=\"mt-5\">" .
     "<p>RUT: " . ($user['rut'] ?? 'No disponible') . "</p>" .
     "<p>Correo: " . ($user['correo'] ?? 'No disponible') . "</p>" .
     "<p>Nombre: " . ($user['nombre'] ?? 'No disponible') . " " . ($user['apellido'] ?? 'No disponible') . "</p>" .
     "<p>Dirección: " . ($user['direccion'] ?? 'No disponible') . "</p>" .
     "<p>Fecha de Nacimiento: " . ($user['fecha_de_nacimiento'] ?? 'No disponible') . "</p>" .
     "<p>Teléfono: " . ($user['telefono'] ?? 'No disponible') . "</p>" .
     "<p>Región: " . ($user['region'] ?? 'No disponible') . "</p>" .
     "<p>Nivel Educacional: " . ($user['nivel_educacional'] ?? 'No disponible') . "</p>" .
     "</div>" .
     "</div>" . 
     "</div>" .
     "</div>";
?>