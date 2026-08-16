Estado: Proyecto académico completado.

# 🐾 iPet — E-commerce & Plataforma de Adopción de Mascotas

**iPet** es una aplicación web integral diseñada para la venta de productos para mascotas y la gestión de procesos de adopción animal. Combina un catálogo interactivo con carrito de compras y un flujo dinámico para la postulación e integración de nuevos adoptantes.

---

## 🛠️ Stack Tecnológico

- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5 (Diseño 100% Responsivo).
- **Backend:** Python.
- **Base de Datos:** MySQL.
- **Arquitectura / Herramientas:** Modelo Relacional, APIs / HTTP POST, Git & GitHub.

---

## 🚀 Características Principales

### 🛒 E-commerce & Carrito de Compras
* **Portada Dinámica:** Carrusel interactivo destacando productos estrella con descripciones y precios.
* **Catálogo & Galería:** Vista detallada de productos con gestión de *stock*, precios, marcas y descripciones.
* **Navegación Fluida:** Menú principal adaptativo con acceso rápido a las distintas secciones del sitio.

### 🐶 Módulo de Adopción & Registro
* **Formulario de Postulación:** Registro para postulantes de adopción con validaciones en cliente y servidor.
* **Captura de Datos Completa:** Recopilación de información personal, contacto, región y nivel educacional.
* **Mantenedores / Datos Maestros:** Formularios y vistas CRUD alineados con el modelo de datos relacional.

---

## ⚙️ Flujo de Datos & Backend

1. **Envío de Requerimientos:** El cliente interactúa con la interfaz web y envía formularios mediante peticiones `HTTP POST`.
2. **Validación en Servidor:** El backend Python valida la integridad y formato de los datos recibidos (correo, RUT, campos obligatorios).
3. **Persistencia de Datos:** Mapeo de la información e inserción directa en la base de datos MySQL (ej. tabla `usuarios`).
4. **Respuestas Dinámicas:** Manejo de excepciones, redirecciones de confirmación (*registro exitoso*) y retroalimentación de errores en tiempo real.

---

## 📱 Adaptabilidad (Responsive Design)

El sitio fue construido bajo un enfoque *Mobile-First*, garantizando una experiencia visual y funcional óptima tanto en dispositivos móviles como en pantallas de escritorio mediante **Bootstrap 5** y estilos CSS personalizados.

---
