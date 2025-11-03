
# 🎓 Ejercicios Prácticos - Modelado de Bases de Datos

## Instrucciones Generales

Para cada ejercicio debes:
1. **Identificar las entidades** principales del sistema
2. **Definir los atributos** de cada entidad (tipos de datos apropiados)
3. **Determinar las relaciones** entre entidades (1:1, 1:N, N:M)
4. **Crear el diagrama ER** (puede ser a mano o con herramientas)
5. **Escribir los scripts SQL** con `CREATE TABLE`
6. **Insertar datos de prueba** (al menos 3-5 registros por tabla)
7. **Escribir consultas** para validar las relaciones

---

## 📚 Nivel Básico

### Ejercicio 1: Sistema de Biblioteca Personal

**Contexto:**  
Necesitas crear una base de datos para administrar tu biblioteca personal.

**Requisitos funcionales:**
- Registrar **libros** con título, autor, ISBN, año de publicación, editorial y número de páginas
- Cada libro pertenece a una **categoría** (ficción, no ficción, ciencia, historia, etc.)
- Una categoría puede tener muchos libros
- Los libros pueden estar en diferentes **estados**: disponible, prestado, extraviado

**Tareas:**
1. Identifica las entidades necesarias
2. Define las relaciones entre ellas
3. Crea las tablas con sus restricciones
4. Inserta al menos 10 libros de diferentes categorías
5. Escribe consultas para:
   - Listar todos los libros de una categoría específica
   - Contar cuántos libros hay por categoría
   - Buscar libros por autor

**Pistas:**
- ¿Qué tipo de relación existe entre Categoría y Libro?
- ¿Qué campos deberían ser obligatorios (NOT NULL)?
- ¿Necesitas índices en algún campo?

---

### Ejercicio 2: Sistema de Registro de Vehículos

**Contexto:**  
El gobierno necesita un sistema para registrar vehículos y sus propietarios.

**Requisitos funcionales:**
- Cada **vehículo** tiene placa, marca, modelo, año, color y tipo (auto, moto, camión)
- Cada vehículo pertenece a un único **propietario** actual
- Los **propietarios** tienen nombre, apellido, documento de identidad, dirección y teléfono
- Un propietario puede tener múltiples vehículos
- Se debe registrar la fecha de registro del vehículo

**Tareas:**
1. Diseña el modelo ER
2. Crea las tablas correspondientes
3. Define correctamente las claves primarias y foráneas
4. Inserta datos de ejemplo:
   - 5 propietarios
   - 8 vehículos (algunos propietarios con varios vehículos)
5. Escribe consultas para:
   - Listar todos los vehículos de un propietario
   - Encontrar propietarios con más de 2 vehículos
   - Buscar vehículos por marca y modelo

**Desafío adicional:**
- Agrega una tabla de **multas** relacionada con vehículos
- Cada multa tiene fecha, monto, descripción e indica si está pagada

---

### Ejercicio 3: Sistema de Citas Médicas

**Contexto:**  
Una clínica necesita gestionar citas entre pacientes y médicos.

**Requisitos funcionales:**
- Los **pacientes** tienen nombre, apellido, documento, fecha de nacimiento, teléfono y email
- Los **médicos** tienen nombre, apellido, especialidad, número de licencia y teléfono
- Se deben agendar **citas** que incluyen: fecha, hora, duración, motivo y estado (pendiente, confirmada, cancelada, completada)
- Cada cita es entre un paciente y un médico
- Un paciente puede tener múltiples citas (con el mismo u otros médicos)
- Un médico puede atender múltiples pacientes

**Tareas:**
1. Identifica el tipo de relación entre Pacientes, Médicos y Citas
2. Crea el modelo de datos apropiado
3. Implementa las tablas con todas las restricciones necesarias
4. Inserta datos de prueba:
   - 4 médicos de diferentes especialidades
   - 10 pacientes
   - 15 citas distribuidas entre los médicos
5. Escribe consultas para:
   - Ver todas las citas de un paciente específico
   - Ver la agenda de un médico para una fecha específica
   - Listar citas pendientes de confirmación
   - Encontrar pacientes que han tenido más de 3 citas

**Pistas:**
- ¿Las citas son una tabla intermedia en una relación N:M?
- ¿Qué restricciones CHECK puedes agregar para validar datos?

---

## 🚀 Nivel Intermedio

### Ejercicio 4: Sistema de Gestión de Hotel

**Contexto:**  
Un hotel necesita gestionar reservaciones, habitaciones y huéspedes.

**Requisitos funcionales:**
- El hotel tiene múltiples **habitaciones** con número, tipo (simple, doble, suite), precio por noche, capacidad máxima y estado (disponible, ocupada, mantenimiento)
- Los **huéspedes** se registran con nombre, apellido, documento, nacionalidad, teléfono y email
- Las **reservaciones** incluyen fecha de entrada, fecha de salida, número de huéspedes, estado (reservada, check-in, check-out, cancelada) y total a pagar
- Una reservación puede incluir múltiples habitaciones
- Una habitación puede tener múltiples reservaciones en diferentes fechas
- Se debe evitar que una habitación se reserve dos veces para las mismas fechas

**Tareas:**
1. Diseña un modelo que maneje correctamente las relaciones N:M
2. Crea todas las tablas necesarias (incluyendo tablas intermedias)
3. Implementa restricciones para garantizar integridad de datos
4. Inserta datos de ejemplo:
   - 15 habitaciones de diferentes tipos
   - 8 huéspedes
   - 10 reservaciones (algunas con múltiples habitaciones)
5. Escribe consultas para:
   - Listar habitaciones disponibles para un rango de fechas
   - Ver el historial de reservaciones de un huésped
   - Calcular los ingresos totales del mes
   - Encontrar las habitaciones más reservadas
6. **Desafío:** Crea un procedimiento almacenado para hacer una nueva reservación con validaciones

**Pistas:**
- Necesitarás una tabla intermedia ¿ReservacionHabitaciones?
- ¿Cómo evitarías reservaciones duplicadas para las mismas fechas?
- Considera usar triggers o constraints para validar fechas

---

### Ejercicio 5: Red Social Simple

**Contexto:**  
Diseña la base de datos para una red social básica.

**Requisitos funcionales:**
- Los **usuarios** tienen username (único), email (único), nombre, apellido, fecha de nacimiento, biografía, fecha de registro y foto de perfil
- Los usuarios pueden crear **publicaciones** (posts) con contenido de texto, fecha de publicación y contador de likes
- Los usuarios pueden **seguir** a otros usuarios (relación de seguidores)
- Los usuarios pueden **comentar** en publicaciones de otros usuarios
- Cada comentario tiene texto, fecha y pertenece a una publicación y un usuario
- Se debe poder identificar quién sigue a quién

**Tareas:**
1. Identifica todas las entidades y sus relaciones
2. Presta especial atención a la relación de "seguir" (un usuario sigue a muchos, y es seguido por muchos)
3. Crea el modelo completo con todas las tablas
4. Inserta datos de ejemplo:
   - 6 usuarios
   - Relaciones de seguimiento entre ellos
   - 12 publicaciones de diferentes usuarios
   - 20 comentarios en varias publicaciones
5. Escribe consultas para:
   - Listar todos los seguidores de un usuario
   - Listar todos los usuarios que sigue un usuario específico
   - Mostrar el feed de un usuario (publicaciones de quienes sigue)
   - Encontrar las publicaciones con más comentarios
   - Contar seguidores y seguidos de cada usuario

**Desafíos adicionales:**
- Implementa un sistema de **likes** en publicaciones
- Agrega la capacidad de que usuarios se envíen **mensajes directos**
- Crea una tabla de **hashtags** relacionada con publicaciones (N:M)

**Pistas:**
- La tabla de seguidores es una relación N:M de Usuarios consigo mismos
- Necesitarás una tabla intermedia con dos FK a la misma tabla (Usuarios)

---

### Ejercicio 6: Sistema de Gestión de Restaurante

**Contexto:**  
Un restaurante necesita gestionar su menú, pedidos y personal.

**Requisitos funcionales:**
- El **menú** tiene platos con nombre, descripción, categoría (entrada, plato fuerte, postre, bebida), precio y disponibilidad
- Los **ingredientes** se registran con nombre, unidad de medida, cantidad en stock y costo unitario
- Cada plato está compuesto por múltiples ingredientes (con cantidades específicas)
- Los **meseros** tienen nombre, apellido, turno (mañana, tarde, noche) y fecha de contratación
- Los **clientes** pueden hacer pedidos (nombre opcional, número de mesa)
- Los **pedidos** incluyen fecha y hora, número de mesa, mesero que atendió, estado (en preparación, servido, pagado) y total
- Cada pedido puede incluir múltiples platos del menú

**Tareas:**
1. Diseña el modelo completo identificando todas las relaciones
2. Crea las tablas con sus restricciones apropiadas
3. Implementa las tablas intermedias necesarias
4. Inserta datos de ejemplo:
   - 10 ingredientes
   - 8 platos del menú (con sus ingredientes)
   - 4 meseros
   - 15 pedidos con múltiples platos
5. Escribe consultas para:
   - Ver la receta completa de un plato (ingredientes y cantidades)
   - Calcular el costo de producción de un plato
   - Listar pedidos de un mesero específico
   - Encontrar los platos más vendidos
   - Verificar qué platos no se pueden preparar por falta de stock
6. **Desafío:** Crea un trigger que descuente del stock de ingredientes cuando se confirma un pedido

**Pistas:**
- Platos ↔ Ingredientes es N:M (tabla intermedia con cantidad)
- Pedidos ↔ Platos es N:M (tabla intermedia con cantidad de platos)
- Considera agregar un campo "porcentaje_ganancia" al menú

---

## 💪 Nivel Avanzado

### Ejercicio 7: Sistema de E-Learning Completo

**Contexto:**  
Crea una plataforma completa de cursos en línea similar a Udemy o Coursera.

**Requisitos funcionales:**
- **Instructores** pueden crear múltiples cursos
- **Estudiantes** pueden inscribirse en múltiples cursos
- Cada **curso** tiene título, descripción, precio, categoría, nivel (básico, intermedio, avanzado), idioma, requisitos previos y fecha de creación
- Los cursos están organizados en **secciones** (módulos)
- Cada sección contiene múltiples **lecciones**
- Las lecciones tienen título, descripción, tipo (video, lectura, quiz), duración, contenido y orden dentro de la sección
- Los estudiantes pueden dejar **reseñas** (calificación 1-5 y comentario) de los cursos completados
- Se debe registrar el **progreso** del estudiante (qué lecciones ha completado)
- Los estudiantes pueden marcar lecciones como **favoritas**
- Implementar un sistema de **certificados** que se generan al completar un curso

**Tareas:**
1. Diseña el modelo ER completo con todas las entidades y relaciones
2. Identifica correctamente todas las relaciones 1:1, 1:N y N:M
3. Crea todas las tablas necesarias con índices apropiados
4. Implementa constraints y validaciones de negocio
5. Inserta datos de ejemplo completos:
   - 3 instructores
   - 5 cursos con diferentes niveles
   - 15 secciones distribuidas en los cursos
   - 30 lecciones
   - 10 estudiantes
   - 25 inscripciones
   - Progreso de estudiantes
   - 15 reseñas
6. Escribe consultas avanzadas:
   - Calcular el promedio de calificación de cada curso
   - Ver el progreso porcentual de un estudiante en un curso
   - Listar los cursos más populares (más inscritos)
   - Encontrar estudiantes que han completado más de 3 cursos
   - Calcular ingresos totales por instructor
   - Mostrar lecciones pendientes de un estudiante en un curso
7. Crea vistas útiles:
   - Vista de cursos con su calificación promedio y número de estudiantes
   - Vista de progreso de estudiantes por curso
8. Implementa procedimientos almacenados:
   - Inscribir estudiante en curso (con validaciones)
   - Marcar lección como completada y actualizar progreso
   - Generar certificado si el curso está 100% completado

**Desafíos extra:**
- Sistema de **cupones de descuento**
- **Preguntas frecuentes (FAQ)** por curso
- Sistema de **discusiones** entre estudiantes (foros)
- **Logros/insignias** por completar ciertos hitos

---

### Ejercicio 8: Sistema Bancario

**Contexto:**  
Diseña la base de datos para un sistema bancario básico.

**Requisitos funcionales:**
- **Clientes** con información personal (nombre, apellido, documento, fecha de nacimiento, dirección, teléfono, email)
- Cada cliente puede tener múltiples **cuentas** (ahorro, corriente, nómina)
- Las cuentas tienen número de cuenta único, tipo, saldo, fecha de apertura y estado (activa, bloqueada, cerrada)
- Se debe registrar cada **transacción**: tipo (depósito, retiro, transferencia), monto, fecha, hora, descripción, saldo anterior y saldo posterior
- Las **transferencias** son un tipo especial de transacción que involucra dos cuentas (origen y destino)
- Los clientes pueden tener **tarjetas** asociadas a sus cuentas (débito, crédito)
- Las tarjetas tienen número, tipo, fecha de emisión, fecha de vencimiento, CVV y estado
- Implementar un sistema de **préstamos**: monto, tasa de interés, plazo (meses), fecha de aprobación, estado (solicitado, aprobado, rechazado, activo, pagado)
- Registrar los **pagos de préstamos** con fecha, monto e intereses

**Tareas:**
1. Crea un modelo robusto que garantice integridad financiera
2. Implementa todas las tablas con restricciones estrictas
3. Usa tipos de datos apropiados (DECIMAL para montos)
4. Asegura que no puedan haber saldos negativos (excepto si aplica)
5. Inserta datos de ejemplo:
   - 8 clientes
   - 12 cuentas (algunos clientes con múltiples cuentas)
   - 5 tarjetas
   - 30 transacciones variadas
   - 4 préstamos con sus pagos
6. Escribe consultas para:
   - Ver el historial de transacciones de una cuenta
   - Calcular el saldo total de un cliente (todas sus cuentas)
   - Listar transferencias entre cuentas
   - Encontrar clientes con préstamos activos
   - Calcular el saldo pendiente de un préstamo
   - Generar un estado de cuenta mensual
7. Crea triggers para:
   - Validar que hay saldo suficiente antes de un retiro
   - Actualizar automáticamente el saldo de la cuenta en cada transacción
   - Registrar transferencias en ambas cuentas (origen y destino)
8. Crea procedimientos almacenados:
   - Realizar transferencia entre cuentas
   - Procesar pago de préstamo
   - Consultar saldo disponible

**Consideraciones de seguridad:**
- Encriptar datos sensibles (puedes simular con comentarios)
- Auditoría de todas las operaciones
- Validaciones estrictas de montos y saldos

---

### Ejercicio 9: Sistema de Gestión de Proyectos (Estilo Jira/Trello)

**Contexto:**  
Diseña una herramienta de gestión de proyectos para equipos de desarrollo.

**Requisitos funcionales:**
- **Organizaciones** que contienen múltiples equipos y proyectos
- **Usuarios** con roles (administrador, manager, desarrollador, tester, viewer)
- **Proyectos** con nombre, descripción, fecha inicio, fecha fin estimada y estado
- Los proyectos están organizados en **tableros** (boards)
- Los tableros tienen **listas** (columnas): To Do, In Progress, Review, Done
- Las **tareas** (issues) tienen título, descripción, tipo (bug, feature, mejora), prioridad (baja, media, alta, crítica), estimación de tiempo, tiempo real trabajado
- Las tareas pueden tener **subtareas**
- Se deben registrar **comentarios** en las tareas
- Las tareas pueden tener **archivos adjuntos**
- Los usuarios pueden ser asignados a múltiples tareas
- Una tarea puede tener múltiples asignados
- Sistema de **etiquetas** (labels/tags) para categorizar tareas
- Registrar el **historial de cambios** de cada tarea (quién cambió qué y cuándo)
- Sistema de **sprints** (iteraciones) para metodologías ágiles

**Tareas:**
1. Diseña el modelo ER completo (será complejo)
2. Identifica todas las relaciones incluyendo auto-referencias
3. Crea todas las tablas con sus restricciones
4. Implementa índices para optimizar consultas frecuentes
5. Inserta datos de ejemplo:
   - 1 organización
   - 3 proyectos
   - 6 usuarios con diferentes roles
   - 3 tableros
   - 9 listas distribuidas en los tableros
   - 25 tareas en diferentes estados
   - 10 subtareas
   - 30 comentarios
   - 2 sprints
   - Asignaciones de usuarios a tareas
   - Etiquetas y relaciones
6. Escribe consultas complejas:
   - Ver todas las tareas de un usuario
   - Calcular el progreso de un proyecto
   - Listar tareas bloqueadas o críticas
   - Ver el workload de cada usuario
   - Generar reporte de productividad del sprint
   - Calcular tiempo real vs estimado por proyecto
7. Crea vistas:
   - Vista de dashboard por proyecto
   - Vista de tareas pendientes por usuario
   - Vista de métricas del sprint
8. Implementa triggers:
   - Registrar cambios en el historial automáticamente
   - Actualizar estado del proyecto cuando todas las tareas están completadas

---

## 🎯 Ejercicio Final Integrador

### Ejercicio 10: Marketplace Completo (Amazon/Mercado Libre)

**Contexto:**  
Diseña un marketplace completo que integre todos los conceptos aprendidos.

**Requisitos funcionales principales:**

**Módulo de Usuarios:**
- Usuarios con diferentes roles: comprador, vendedor, administrador
- Perfil de vendedor con información adicional (empresa, RUC/RFC, verificación)
- Sistema de direcciones múltiples por usuario
- Métodos de pago guardados

**Módulo de Productos:**
- Categorías jerárquicas (categoría → subcategoría → sub-subcategoría)
- Productos con múltiples imágenes
- Variantes de productos (talla, color, etc.)
- Atributos dinámicos según categoría
- Sistema de inventario por variante
- Descuentos y promociones

**Módulo de Ventas:**
- Carrito de compras persistente
- Órdenes de compra con múltiples productos
- Estados de orden (pendiente, pagada, enviada, entregada, cancelada)
- Sistema de envíos con tracking
- Métodos de pago
- Facturas

**Módulo de Reseñas y Calificaciones:**
- Reseñas de productos con fotos
- Calificación al vendedor
- Sistema de preguntas y respuestas en productos
- Votos útiles en reseñas

**Módulo Adicional:**
- Sistema de cupones y códigos de descuento
- Programa de puntos/recompensas
- Lista de deseos (wishlist)
- Comparador de productos
- Notificaciones al usuario
- Historial de búsquedas

**Tareas:**
1. Crea un documento de análisis identificando TODAS las entidades
2. Define un modelo ER completo y profesional
3. Implementa TODAS las tablas necesarias
4. Usa constraints avanzados (CHECK con subconsultas si es posible)
5. Crea índices estratégicos
6. Implementa al menos 5 vistas útiles
7. Crea al menos 5 procedimientos almacenados
8. Implementa triggers para lógica de negocio
9. Inserta un dataset realista y completo
10. Escribe 20+ consultas que demuestren todas las relaciones
11. Genera reportes de negocio:
    - Top productos más vendidos
    - Mejores vendedores
    - Análisis de ventas por categoría
    - Productos más buscados
    - Tasa de conversión de carrito a venta
    - Análisis de abandono de carrito

**Este ejercicio debe demostrar:**
- ✅ Dominio completo de relaciones 1:1, 1:N y N:M
- ✅ Uso correcto de constraints y validaciones
- ✅ Normalización apropiada
- ✅ Consultas complejas con múltiples JOINs
- ✅ Subconsultas y consultas agregadas
- ✅ Vistas, procedimientos y triggers
- ✅ Índices para optimización
- ✅ Pensamiento en escalabilidad

---


- **Diseño:** [dbdiagram.io](https://dbdiagram.io/), [draw.io](https://draw.io), [MySQL Workbench](https://www.mysql.com/products/workbench/)
- **Desarrollo:** MySQL, PostgreSQL, SQL Server
- **Testing:** Ejecuta tus scripts en un entorno de prueba
- **Validación:** Pide a un compañero que revise tu diseño

---

## 💡 Consejos Generales

1. **Lee cuidadosamente los requisitos** antes de empezar a diseñar
2. **Dibuja el diagrama ER primero** en papel o herramienta digital
3. **Normaliza tus tablas** para evitar redundancia
4. **Usa nombres descriptivos** para tablas y columnas
5. **Comenta tu código SQL** para explicar decisiones complejas
6. **Prueba tus constraints** intentando insertar datos inválidos
7. **Optimiza con índices** pero no sobre-indexes
8. **Documenta tus suposiciones** cuando los requisitos no sean claros
9. **Revisa tu trabajo** ejecutando todas las consultas
10. **Pide feedback** de tus compañeros o instructor

---

## 🚀 Desafío Extra

Si completas todos los ejercicios, intenta:

1. **Migración de datos:** Crea scripts para migrar datos entre versiones de tu esquema
2. **Optimización:** Usa EXPLAIN para analizar y optimizar tus consultas más lentas
3. **Seguridad:** Implementa roles y permisos SQL para diferentes tipos de usuarios
4. **Backup:** Crea scripts de backup y restore
5. **Testing:** Escribe tests para tus procedimientos almacenados
6. **Documentación:** Genera documentación automática de tu base de datos

---

**¡Buena suerte con los ejercicios!** 🎉

Recuerda: No hay una única solución correcta. Lo importante es que tu diseño sea coherente, escalable y resuelva los requisitos planteados.

---
