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

if (password_verify($password, $user['password'])) {
    // Inicio de sesión exitoso
    $_SESSION['rut'] = $user['rut'];
    echo 'Inicio de sesión exitoso.';
} else {
    // Inicio de sesión fallido
    echo 'Contraseña incorrecta.';
}

$stmt->close();
$conn->close();
?>