-- Active: 1713539787748@@127.0.0.1@3306@ipet
CREATE TABLE IF NOT EXISTS USUARIO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(12) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    direccion VARCHAR(255),
    fecha_de_nacimiento DATE,
    telefono VARCHAR(20),
    region VARCHAR(255),
    nivel_educacional VARCHAR(255),
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_login TIMESTAMP DEFAULT NULL,
    intentos_login INT DEFAULT 0,
    esta_bloqueado BOOLEAN DEFAULT false
);