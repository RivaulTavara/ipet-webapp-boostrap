<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Iniciar la sesión
session_start();

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

?>