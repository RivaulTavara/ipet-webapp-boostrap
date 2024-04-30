<?php
session_start();
include 'config.php';

$email = $_POST['email'];
$password = $_POST['password'];

// Prepare statement
$stmt = $conn->prepare("SELECT * FROM users WHERE email = ?");
$stmt->bind_param("s", $email);

$stmt->execute();

$result = $stmt->get_result();
$user = $result->fetch_assoc();

$response = array();


if (password_verify($password, $user['password'])) {
    // Inicio de sesión exitoso
    $_SESSION['rut'] = $user['rut'];
    echo json_encode(['success' => true]);
} else {
    // Inicio de sesión fallido
    echo json_encode(['error' => 'Contraseña incorrecta.']);
}


$stmt->close();
$conn->close();

// Send response to client
header('Content-Type: application/json');
echo json_encode($response);
?>