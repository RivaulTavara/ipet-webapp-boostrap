<?php
$servername = "ipetdb.mysql.database.azure.com";
$username = "ipetadmin";
$dbPassword = "M3l0d1aFuerT3!42"; 
$dbname = "ipet";

// Initialize mysqli
$conn = mysqli_init();

// Set SSL options
mysqli_ssl_set($conn, NULL, NULL, "../sql/DigiCertGlobalRootCA.crt.pem", NULL, NULL);

// Establish the connection
mysqli_real_connect($conn, $servername, $username, $dbPassword, $dbname, 3306, MYSQLI_CLIENT_SSL);

// Check connection
if (mysqli_connect_errno()) {
    die('Falló la conexión: '.mysqli_connect_error().' ('.mysqli_connect_errno().')');
} 
?>