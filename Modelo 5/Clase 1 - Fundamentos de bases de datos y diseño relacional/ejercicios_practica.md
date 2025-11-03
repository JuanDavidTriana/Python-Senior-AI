# Ejercicios Prácticos - Fundamentos de Bases de Datos y Diseño Relacional

Este documento contiene ejercicios prácticos para reforzar los conceptos de bases de datos relacionales, diseño ER y PostgreSQL vistos en clase.

## Índice

- [Ejercicio 1: Sistema de Gestión de Tienda Online](#ejercicio-1-sistema-de-gestión-de-tienda-online)
- [Ejercicio 2: Sistema de Gestión Hospitalaria](#ejercicio-2-sistema-de-gestión-hospitalaria)
- [Ejercicio 3: Sistema de Cursos y Estudiantes](#ejercicio-3-sistema-de-cursos-y-estudiantes)
- [Ejercicio 4: Normalización y Optimización](#ejercicio-4-normalización-y-optimización)
- [Ejercicio 5: Restricciones y Validaciones](#ejercicio-5-restricciones-y-validaciones)

---

## Ejercicio 1: Sistema de Gestión de Tienda Online

### Descripción
Diseña una base de datos para una tienda online que venda productos electrónicos.

### Requisitos del negocio

1. **Productos**: Cada producto tiene un código único, nombre, descripción, precio y stock disponible.
2. **Categorías**: Los productos se organizan en categorías (computadoras, teléfonos, accesorios, etc.). Un producto puede pertenecer a múltiples categorías.
3. **Clientes**: Se registran con nombre, email único, teléfono y dirección de envío.
4. **Pedidos**: Los clientes realizan pedidos que contienen uno o más productos. Cada pedido tiene fecha, estado (pendiente, enviado, entregado, cancelado) y total.
5. **Detalle de pedido**: Cada línea del pedido incluye el producto, cantidad y precio unitario al momento de la compra.

### Restricciones específicas

- El precio de los productos debe ser mayor a 0.
- El stock no puede ser negativo.
- El email del cliente debe contener el símbolo '@'.
- La fecha del pedido no puede ser futura.
- La cantidad en el detalle del pedido debe ser al menos 1.
- El estado del pedido solo puede ser uno de los valores permitidos.

### Tareas

1. **Diseño conceptual**:
   - Identifica las entidades principales.
   - Define atributos para cada entidad con sus tipos de datos.
   - Establece las relaciones y cardinalidades entre entidades.
   - Crea un diagrama ER (usa Mermaid o PlantUML).

2. **Diseño lógico**:
   - Crea un diccionario de datos con todas las columnas, tipos, restricciones.
   - Define las claves primarias y foráneas.
   - Especifica restricciones NOT NULL, UNIQUE, CHECK, DEFAULT.

3. **Implementación SQL**:
   - Escribe el script SQL completo que cree todas las tablas.
   - Incluye índices para optimizar búsquedas frecuentes.
   - Inserta al menos 5 productos, 3 categorías, 3 clientes y 3 pedidos con sus detalles.

4. **Consultas de validación**:
   - Lista todos los productos con su categoría.
   - Muestra los pedidos de un cliente específico con el detalle completo.
   - Calcula el total vendido por categoría.
   - Encuentra los productos con stock bajo (menos de 10 unidades).

### Entregables

- `ejercicio1_tienda.sql`: Script completo ejecutable.
- `ejercicio1_diagrama_er`: Diagrama ER en formato Mermaid o imagen.
- `ejercicio1_consultas.sql`: Archivo con las 4 consultas solicitadas.

### Puntos extra (opcional)

- Implementa un trigger o constraint que actualice automáticamente el stock cuando se crea un pedido.
- Añade una tabla de `reseñas` donde los clientes pueden calificar productos (1-5 estrellas).
- Crea un índice único parcial para evitar múltiples pedidos "pendientes" del mismo cliente.

---

## Ejercicio 2: Sistema de Gestión Hospitalaria

### Descripción
Diseña una base de datos para gestionar pacientes, médicos y citas en un hospital.

### Requisitos del negocio

1. **Pacientes**: Identificados por DNI (único), con nombre completo, fecha de nacimiento, teléfono y dirección.
2. **Médicos**: Tienen matrícula profesional única, nombre, especialidad y teléfono de consultorio.
3. **Especialidades**: Catálogo de especialidades médicas (cardiología, pediatría, traumatología, etc.).
4. **Citas**: Relacionan un paciente con un médico en una fecha y hora específicas. Incluyen motivo de consulta y observaciones (opcional).
5. **Historias clínicas**: Cada paciente tiene una historia clínica con diagnósticos, tratamientos y fechas de registro.

### Restricciones específicas

- El DNI del paciente debe tener exactamente 8 dígitos.
- La matrícula del médico debe ser única.
- No se pueden agendar dos citas para el mismo médico en el mismo horario.
- La fecha de nacimiento del paciente debe ser anterior a hoy.
- La fecha de la cita no puede ser en el pasado.
- Un médico solo puede tener una especialidad principal.

### Tareas

1. **Diseño conceptual**:
   - Define entidades: Paciente, Médico, Especialidad, Cita, HistoriaClinica.
   - Establece relaciones: Médico-Especialidad (N:1), Paciente-Cita (1:N), Médico-Cita (1:N), Paciente-HistoriaClinica (1:N).
   - Crea el diagrama ER completo.

2. **Diseño lógico**:
   - Diccionario de datos con todas las tablas.
   - Define restricciones para DNI, matrícula, fechas.
   - Piensa en cómo evitar solapamiento de citas.

3. **Implementación SQL**:
   - Script SQL con creación de esquema `hospital`.
   - Incluye todas las restricciones solicitadas.
   - Datos de ejemplo: 3 especialidades, 5 médicos, 10 pacientes, 8 citas, 5 registros de historia clínica.

4. **Consultas de validación**:
   - Lista médicos con su especialidad.
   - Muestra todas las citas de un paciente ordenadas por fecha.
   - Encuentra los médicos más solicitados (con más citas).
   - Lista pacientes que tienen citas pendientes (futuras).

### Entregables

- `ejercicio2_hospital.sql`: Script completo.
- `ejercicio2_diagrama_er`: Diagrama ER.
- `ejercicio2_consultas.sql`: Las 4 consultas.

### Puntos extra (opcional)

- Añade una tabla de `tratamientos` y `medicamentos` relacionados con la historia clínica.
- Implementa un CHECK que valide que la edad del paciente sea coherente con especialidades pediátricas.
- Crea una vista que muestre el resumen de citas por mes y especialidad.

---

## Ejercicio 3: Sistema de Cursos y Estudiantes

### Descripción
Diseña una base de datos para una plataforma educativa que gestiona cursos, estudiantes e inscripciones.

### Requisitos del negocio

1. **Estudiantes**: Identificados por email único, con nombre, fecha de registro y país.
2. **Cursos**: Cada curso tiene código único, título, descripción, duración en horas y precio.
3. **Instructores**: Tienen nombre, biografía corta y especialidad. Un curso puede tener varios instructores y un instructor puede dar varios cursos (N:M).
4. **Inscripciones**: Relacionan estudiantes con cursos, con fecha de inscripción, progreso (0-100%) y estado (activo, completado, abandonado).
5. **Módulos**: Los cursos se dividen en módulos con título, orden y duración.
6. **Evaluaciones**: Cada estudiante puede tener calificaciones por módulo (0-100 puntos).

### Restricciones específicas

- El email del estudiante debe ser único y contener '@'.
- El precio del curso debe ser mayor o igual a 0.
- La duración en horas debe ser positiva.
- El progreso de la inscripción debe estar entre 0 y 100.
- El estado de inscripción solo puede ser: 'activo', 'completado', 'abandonado'.
- La calificación debe estar entre 0 y 100.
- El orden de los módulos debe ser un entero positivo.

### Tareas

1. **Diseño conceptual**:
   - Identifica 6 entidades: Estudiante, Curso, Instructor, Inscripcion, Modulo, Evaluacion.
   - Define relaciones: Estudiante-Inscripcion-Curso (N:M con atributos), Curso-Instructor (N:M), Curso-Modulo (1:N), Estudiante-Evaluacion-Modulo (N:M con nota).
   - Crea el diagrama ER.

2. **Diseño lógico**:
   - Tablas necesarias: estudiante, curso, instructor, curso_instructor, inscripcion, modulo, evaluacion.
   - Define todas las PK, FK y restricciones.

3. **Implementación SQL**:
   - Script completo con esquema `plataforma_educativa`.
   - Datos: 5 estudiantes, 3 cursos, 4 instructores, 8 módulos, 6 inscripciones, 10 evaluaciones.

4. **Consultas de validación**:
   - Lista todos los cursos con sus instructores.
   - Muestra las inscripciones activas con progreso mayor al 50%.
   - Calcula el promedio de calificaciones por estudiante.
   - Encuentra los cursos más populares (con más inscripciones).

### Entregables

- `ejercicio3_cursos.sql`: Script SQL completo.
- `ejercicio3_diagrama_er`: Diagrama ER.
- `ejercicio3_consultas.sql`: Las 4 consultas.

### Puntos extra (opcional)

- Añade una tabla de `certificados` que se generen automáticamente cuando un estudiante complete un curso con promedio >= 70.
- Implementa lógica para que el progreso se calcule automáticamente según los módulos completados.
- Crea índices compuestos para optimizar búsquedas por estado y progreso.

---

## Ejercicio 4: Normalización y Optimización

### Descripción
Se te proporciona un diseño de tabla desnormalizado. Tu tarea es normalizarlo a 3FN.

### Tabla original (NO normalizada)

```sql
CREATE TABLE pedidos_clientes (
  id SERIAL PRIMARY KEY,
  cliente_nombre VARCHAR(100),
  cliente_email VARCHAR(100),
  cliente_telefono VARCHAR(20),
  cliente_ciudad VARCHAR(50),
  producto_nombre VARCHAR(200),
  producto_categoria VARCHAR(50),
  producto_precio NUMERIC(10,2),
  cantidad INT,
  fecha_pedido DATE,
  total_pedido NUMERIC(10,2)
);
```

### Problemas identificados

- Redundancia: datos del cliente y producto se repiten en cada pedido.
- Anomalías de actualización: si cambia el email del cliente, hay que actualizar múltiples filas.
- Anomalías de inserción: no puedo registrar un producto sin pedido.
- Anomalías de eliminación: si elimino un pedido, pierdo información del producto.
- `total_pedido` es un dato derivado (cantidad × precio).

### Tareas

1. **Normalización**:
   - Descompón la tabla en entidades separadas: Cliente, Producto, Categoria, Pedido, DetallePedido.
   - Asegura que cumple 1FN, 2FN y 3FN.
   - Documenta qué problemas se solucionan con cada forma normal.

2. **Diseño normalizado**:
   - Crea el esquema completo con todas las tablas necesarias.
   - Define PK, FK y restricciones adecuadas.
   - Elimina datos derivados (o conviértelos en campos calculados).

3. **Implementación**:
   - Escribe el script SQL con el diseño normalizado.
   - Inserta los mismos datos de ejemplo pero en las tablas normalizadas.

4. **Consultas equivalentes**:
   - Escribe una consulta que reproduzca la vista de la tabla original usando JOINs.
   - Compara el espacio utilizado (número de filas totales) entre ambos diseños.

### Entregables

- `ejercicio4_normalizacion.sql`: Script con diseño normalizado.
- `ejercicio4_analisis.md`: Documento que explique paso a paso la normalización.
- `ejercicio4_comparacion.sql`: Consultas que demuestren equivalencia.

### Puntos extra (opcional)

- Crea índices para optimizar la consulta de reconstrucción.
- Implementa una vista materializada que replique la tabla original para consultas rápidas.
- Mide el tiempo de ejecución de consultas en ambos diseños.

---

## Ejercicio 5: Restricciones y Validaciones

### Descripción
Practica la implementación de restricciones complejas usando CHECK, triggers y validaciones avanzadas.

### Escenario: Sistema de Reservas de Hotel

**Entidades básicas**: Hotel, Habitacion, Cliente, Reserva.

### Restricciones a implementar

1. **CHECK básicos**:
   - El precio de la habitación debe ser mayor a 0.
   - La capacidad de la habitación debe ser entre 1 y 10 personas.
   - La calificación del hotel debe ser entre 1 y 5 estrellas.
   - La fecha de check-out debe ser posterior a la fecha de check-in.

2. **UNIQUE compuestos**:
   - No puede haber dos habitaciones con el mismo número en el mismo hotel.
   - No puede haber dos reservas activas para la misma habitación en fechas solapadas.

3. **CHECK con subconsultas o lógica compleja**:
   - El número de huéspedes en una reserva no puede exceder la capacidad de la habitación.
   - No se pueden hacer reservas con más de 1 año de anticipación.
   - La fecha de check-in no puede ser en el pasado.

4. **DEFAULT inteligentes**:
   - Fecha de reserva por defecto: fecha actual.
   - Estado de reserva por defecto: 'confirmada'.
   - Check-out por defecto: check-in + 1 día.

5. **Índices únicos parciales**:
   - Solo una reserva "activa" por habitación en fechas específicas.

### Tareas

1. **Diseño**:
   - Define las 4 tablas con todos sus atributos.
   - Documenta cada restricción que vas a implementar.

2. **Implementación SQL**:
   - Script completo con todas las restricciones.
   - Incluye comentarios explicando cada CHECK y constraint.

3. **Pruebas**:
   - Crea un conjunto de INSERTs que:
     - ✅ Pasen todas las validaciones (casos válidos).
     - ❌ Fallen por cada tipo de restricción (casos inválidos).
   - Documenta el resultado esperado de cada prueba.

4. **Validación**:
   - Intenta insertar una reserva con check-out antes que check-in → debe fallar.
   - Intenta reservar una habitación ya ocupada en las mismas fechas → debe fallar.
   - Intenta crear una habitación con capacidad 0 → debe fallar.
   - Inserta reservas válidas que no solapen → debe funcionar.

### Entregables

- `ejercicio5_hotel.sql`: Script con todas las restricciones.
- `ejercicio5_pruebas.sql`: Script con casos de prueba comentados.
- `ejercicio5_resultados.md`: Documento con capturas o explicación de cada prueba.

### Puntos extra (opcional)

- Implementa un trigger que envíe una notificación (simulada con un INSERT en tabla `log`) cuando se crea una reserva.
- Añade una función que calcule automáticamente el precio total de la reserva según noches y precio de habitación.
- Crea un CHECK que valide que el email del cliente tenga formato válido (regex básico).

---

## Consejos para Resolver los Ejercicios

1. **Lee todos los requisitos** antes de empezar a diseñar.
2. **Empieza simple**: identifica entidades obvias y luego refina.
3. **Normaliza desde el inicio**: evita redundancias desde el diseño conceptual.
4. **Usa restricciones abundantes**: NOT NULL, CHECK, UNIQUE son tus aliados.
5. **Piensa en índices**: columnas de FK y búsquedas frecuentes.
6. **Prueba todo**: inserta datos válidos e inválidos para verificar restricciones.
7. **Documenta decisiones**: comenta por qué elegiste ciertos tipos o restricciones.
8. **Usa herramientas**: pgAdmin, DBeaver o psql para ejecutar y verificar.

---

## Recursos Adicionales

- Documentación oficial de PostgreSQL: https://www.postgresql.org/docs/
- Tutorial de normalización: https://www.studytonight.com/dbms/database-normalization.php
- Herramienta para diagramas ER: https://drawsql.app/ (DrawSQL)
- SQL Style Guide: https://www.sqlstyle.guide/

---

## Entrega de Ejercicios

Para cada ejercicio crea una carpeta con el formato `ejercicioN_nombre/` que contenga:

```
ejercicio1_tienda/
  ├── ejercicio1_tienda.sql
  ├── ejercicio1_diagrama_er.png (o .puml/.mmd)
  ├── ejercicio1_consultas.sql
  └── ejercicio1_notas.md (opcional, con decisiones de diseño)
```


**¿Dudas?**: ¿Dudas?: Recuerda que puedes usar IA como asistente (ver sección 6 del README principal), pero siempre valida con el checklist y prueba ejecutando el código. También puedes ver la **clase 1 del módulo 5** para reforzar los conceptos.

---

¡Buena suerte y a practicar! 🚀
