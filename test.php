<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Registro</title>
</head>
<body>
<form action="main\model\php\test.php" method="post">
        <label for="rut">RUT:</label><br>
        <input type="text" id="rut" name="rut" ><br>
        <label for="correo">Correo:</label><br>
        <input type="email" id="correo" name="correo" ><br>
        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre" ><br>
        <label for="apellido">Apellido:</label><br>
        <input type="text" id="apellido" name="apellido" ><br>
        <label for="password">Contraseña:</label><br>
        <input type="password" id="password" name="password" ><br>
        <label for="fechaNacimiento">Fecha de Nacimiento:</label><br>
        <input type="date" id="fechaNacimiento" name="fechaNacimiento" ><br>
        <label for="telefono">Teléfono:</label><br>
        <input type="tel" id="telefono" name="telefono" ><br>
        <label for="region">Región:</label><br>
        <input type="text" id="region" name="region" ><br>
        <label for="nivelEducacional">Nivel Educacional:</label><br>
        <input type="text" id="nivelEducacional" name="nivelEducacional" ><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>