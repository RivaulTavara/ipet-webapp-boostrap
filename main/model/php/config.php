<?php
$servername = "localhost";
$username = "root";
$dbPassword = ""; 
$dbname = "ipet";

// Create connection
$conn = new mysqli($servername, $username, $dbPassword, $dbname);

// Check connection
if ($conn->connect_error) {
    die("La conexión ha fallado: " . $conn->connect_error);
}
?>