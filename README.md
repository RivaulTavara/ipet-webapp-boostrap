Este es un carrito de compras hecho usando HTML5, CSS3 y Boostrap 5
- "Main" contiene los archivos principales de html
- "Documentacion" contiene los requerimientos de la evaluacion
- "SRC" contiene las imagenes y demás recursos de el carrito de compras 

REQUERIMIENTOS:

1.Crear bosquejo o “mockup” para el análisis de las nuevas funcionalidades requeridas por el cliente.

2. Agregar un menú que permita acceder a las distintas páginas solicitadas.

3. Mejorar la portada del sitio modificando la imagen de portada por un carrusel de imágenes que muestre los productos destacados, acompañado de una descripción y precio de venta (de al menos 3 productos).

4. Incluir una galería de imágenes (de al menos 6 productos) que permita a los visitantes ver todos los productos disponibles hasta ese momento. Cada imagen debe mostrar: imagen del producto, descripción, precio, stock y marca.

5. Construir una página para el registro de nuevos usuarios que cumpla con los siguientes requerimientos solicitados por la Fundación para recopilar información acerca de los postulantes que desean adoptar una mascota:

· Información como texto: Rut, nombre, apellido, correo, fecha de nacimiento y teléfono

· Información seleccionable:Región y nivel educacional (Doctor, Magíster, Profesional, etc)

6. Construir los formularios de los datos maestros o mantenedores requeridos para el proyecto y definidos en el modelo de datos.

7. Escoger los inputs adecuados a los tipos de datos definidos en cada una de las tablas y/o modelo de datos.

8. Considere que las páginas deben ser correctamente visualizado tanto en la versión web como en la versión móvil del sitio. (Responsiva)

9. Aplique estilos CSS propios o bien utilice el apoyo de un framework CSS para lograr que el formulario posea una apariencia acorde al resto del sitio.


[MYSQL]

Para el formulario de registro, los campos se mapearán a las columnas de la base de datos MySQL de la siguiente manera:

- Rut (rut): mapeado a la columna `rut` en la tabla `usuarios`
- Nombre (nombre): mapeado a la columna `nombre` en la tabla `usuarios`
- Apellido (apellido): mapeado a la columna `apellido` en la tabla `usuarios`
- Correo (correo): mapeado a la columna `correo` en la tabla `usuarios`
- Fecha de nacimiento (fechaNacimiento): mapeado a la columna `fecha_nacimiento` en la tabla `usuarios`
- Teléfono (telefono): mapeado a la columna `telefono` en la tabla `usuarios`
- Región (region): mapeado a la columna `region` en la tabla `usuarios`
- Nivel educacional (nivelEducacional): mapeado a la columna `nivel_educacional` en la tabla `usuarios`