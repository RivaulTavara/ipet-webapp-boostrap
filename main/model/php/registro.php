<?php

    $servidor="localhost";
    $usuario="root";
    $clave="";
    $basedeDatos="ipet";

    $enlace=mysqli_connect($servidor, $usuario, $clave, $basedeDatos);



    $rut = $_POST['rut'];
    $correo = $_POST['correo'];
    $nombre = $_POST['nombre'];
    $apellido = $_POST['apellido'];
    $contrasena = $_POST['password'];
    $direccion = $_POST['direccion'];
    $fecha = $_POST['fecha'];
    $telefono = $_POST['telefono'];
    $region = $_POST['region'];
    $niveleducacional = $_POST['nivelEducacional'];

    $sql="INSERT INTO usuario (rut, correo, nombre, apellido, contrasena, direccion, fecha_de_nacimiento, telefono, region, nivel_educacional) VALUES ('$rut', '$correo', '$nombre', '$apellido', '$contrasena', '$direccion', '$fecha', '$telefono', '$region', '$niveleducacional')";

    if ($enlace->query($sql) === TRUE) {
        echo "Datos agregados correctamente";
    } else {
        echo "Error: " . $sql . "<br>" . $enlace->error;
    }

    $conn->close();

?>