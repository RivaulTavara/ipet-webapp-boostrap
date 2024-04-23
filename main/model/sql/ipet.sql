-- Active: 1713539787748@@127.0.0.1@3306@ipet
DROP DATABASE IF EXISTS ipet;

CREATE DATABASE ipet;

USE ipet;

CREATE TABLE IF NOT EXISTS USUARIO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(12) NOT NULL UNIQUE,
    correo VARCHAR(255) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL,
    direccion VARCHAR(255),
    fecha_de_nacimiento DATE,
    telefono VARCHAR(20) NOT NULL UNIQUE,
    region VARCHAR(255),
    nivel_educacional VARCHAR(255),
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_login DATETIME DEFAULT NULL
);
CREATE TABLE IF NOT EXISTS PRODUCTO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS PEDIDO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES USUARIO(id)
);

CREATE TABLE IF NOT EXISTS ITEM_PEDIDO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES PEDIDO(id),
    FOREIGN KEY (producto_id) REFERENCES PRODUCTO(id)
);

INSERT INTO USUARIO (rut, correo, nombre, apellido, contrasena, direccion, fecha_de_nacimiento, telefono, region, nivel_educacional)
VALUES ('12345678-9', 'correo@example.com', 'Juan', 'Perez', 'contrasena123', 'Calle Falsa 123', '1980-01-01', '123456789', 'Region Metropolitana', 'Universitario');