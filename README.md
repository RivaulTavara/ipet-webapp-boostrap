# Carrito de Compras

Este es un carrito de compras hecho usando HTML5, CSS3 y Boostrap 5.

## Estructura del Proyecto

- "Main" contiene los archivos principales de html.
- "Documentacion" contiene los requerimientos de la evaluacion.
- "SRC" contiene las imagenes y demás recursos de el carrito de compras.

## Requerimientos

1. Crear bosquejo o “mockup” para el análisis de las nuevas funcionalidades requeridas por el cliente.
2. Agregar un menú que permita acceder a las distintas páginas solicitadas.
3. Mejorar la portada del sitio modificando la imagen de portada por un carrusel de imágenes que muestre los productos destacados, acompañado de una descripción y precio de venta (de al menos 3 productos).
4. Incluir una galería de imágenes (de al menos 6 productos) que permita a los visitantes ver todos los productos disponibles hasta ese momento. Cada imagen debe mostrar: imagen del producto, descripción, precio, stock y marca.
5. Construir una página para el registro de nuevos usuarios que cumpla con los siguientes requerimientos solicitados por la Fundación para recopilar información acerca de los postulantes que desean adoptar una mascota:
    - Información como texto: Rut, nombre, apellido, correo, fecha de nacimiento y teléfono
    - Información seleccionable:Región y nivel educacional (Doctor, Magíster, Profesional, etc)
6. Construir los formularios de los datos maestros o mantenedores requeridos para el proyecto y definidos en el modelo de datos.
7. Escoger los inputs adecuados a los tipos de datos definidos en cada una de las tablas y/o modelo de datos.
8. Considere que las páginas deben ser correctamente visualizado tanto en la versión web como en la versión móvil del sitio. (Responsiva)
9. Aplique estilos CSS propios o bien utilice el apoyo de un framework CSS para lograr que el formulario posea una apariencia acorde al resto del sitio.

## Base de Datos

Para el formulario de registro, los campos se mapearán a las columnas de la base de datos MySQL de la siguiente manera:

- Rut (rut): mapeado a la columna `rut` en la tabla `usuarios`
- Nombre (nombre): mapeado a la columna `nombre` en la tabla `usuarios`

## PHP

En este proyecto, PHP se utiliza para manejar la lógica del servidor, incluyendo la interacción con la base de datos y la generación de páginas HTML dinámicas.

## Flujo de Datos del Registro

El flujo de datos del registro comienza cuando el usuario llena el formulario de registro en la página de registro. Cuando el usuario envía el formulario, los datos del formulario se envían a un script PHP en el servidor a través de una solicitud HTTP POST.

El script PHP recibe los datos del formulario, los valida para asegurarse de que cumplen con los requisitos necesarios (por ejemplo, que todos los campos requeridos están presentes, que el formato del correo electrónico es correcto, etc.), y luego inserta los datos en la base de datos.

Una vez que los datos se han insertado con éxito en la base de datos, el script PHP puede redirigir al usuario a una nueva página (por ejemplo, una página de "registro exitoso") y/o enviar una respuesta al navegador del usuario para confirmar que el registro fue exitoso.

Si ocurre un error en cualquier punto de este proceso (por ejemplo, si la validación de los datos del formulario falla, o si hay un problema al insertar los datos en la base de datos), el script PHP enviará una respuesta adecuada al navegador del usuario para informarle del error.
