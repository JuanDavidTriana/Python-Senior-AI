-- ============================================================================
-- CLASE 3: CRUD SQL - Consultas reales para la gestión de datos
-- Script de apoyo con ejemplos prácticos
-- ============================================================================

-- ============================================================================
-- 1. CREACIÓN DE LA BASE DE DATOS Y TABLAS
-- ============================================================================

-- Crear la base de datos (descomentar según tu SGBD)
-- CREATE DATABASE gestion_academica;
-- USE gestion_academica;

-- Tabla de estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    edad INTEGER CHECK(edad >= 16 AND edad <= 100),
    ciudad VARCHAR(100),
    fecha_registro DATE DEFAULT CURRENT_DATE
);

-- Tabla de libros
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(150) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    año_publicacion INTEGER CHECK(año_publicacion >= 1000 AND año_publicacion <= 2100),
    disponible BOOLEAN DEFAULT TRUE
);

-- ============================================================================
-- 2. OPERACIÓN INSERT - Insertar datos
-- ============================================================================

-- Insertar estudiantes uno por uno
INSERT INTO estudiantes (nombre, email, edad, ciudad)
VALUES ('Juan Pérez', 'juan.perez@email.com', 22, 'Madrid');

INSERT INTO estudiantes (nombre, email, edad, ciudad)
VALUES ('María García', 'maria.garcia@email.com', 20, 'Barcelona');

-- Insertar múltiples registros a la vez (más eficiente)
INSERT INTO estudiantes (nombre, email, edad, ciudad) VALUES
    ('Carlos López', 'carlos.lopez@email.com', 25, 'Valencia'),
    ('Ana Martínez', 'ana.martinez@email.com', 19, 'Madrid'),
    ('Luis Rodríguez', 'luis.rodriguez@email.com', 23, 'Sevilla'),
    ('Elena Sánchez', 'elena.sanchez@email.com', 21, 'Barcelona'),
    ('Pedro Gómez', 'pedro.gomez@email.com', 24, 'Valencia'),
    ('Laura Torres', 'laura.torres@email.com', 20, 'Madrid'),
    ('Miguel Ruiz', 'miguel.ruiz@email.com', 26, 'Bilbao'),
    ('Sofía Díaz', 'sofia.diaz@email.com', 18, 'Barcelona');

-- Insertar libros
INSERT INTO libros (titulo, autor, isbn, año_publicacion, disponible) VALUES
    ('Cien años de soledad', 'Gabriel García Márquez', '978-0307474728', 1967, TRUE),
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', '978-8420412146', 1605, TRUE),
    ('El principito', 'Antoine de Saint-Exupéry', '978-0156012195', 1943, TRUE),
    ('1984', 'George Orwell', '978-0451524935', 1949, FALSE),
    ('El código Da Vinci', 'Dan Brown', '978-0307474278', 2003, TRUE),
    ('Harry Potter y la piedra filosofal', 'J.K. Rowling', '978-8478884452', 1997, FALSE),
    ('Crónica de una muerte anunciada', 'Gabriel García Márquez', '978-0307387660', 1981, TRUE),
    ('La sombra del viento', 'Carlos Ruiz Zafón', '978-8408093886', 2001, TRUE),
    ('El alquimista', 'Paulo Coelho', '978-0061122415', 1988, TRUE),
    ('Rayuela', 'Julio Cortázar', '978-8420471624', 1963, TRUE);

-- ============================================================================
-- 3. OPERACIÓN SELECT - Consultar datos
-- ============================================================================

-- Seleccionar todos los registros
SELECT * FROM estudiantes;
SELECT * FROM libros;

-- Seleccionar columnas específicas
SELECT nombre, email FROM estudiantes;
SELECT titulo, autor, año_publicacion FROM libros;

-- Seleccionar con alias (renombrar columnas en el resultado)
SELECT 
    nombre AS "Nombre Completo",
    email AS "Correo Electrónico",
    edad AS "Edad (años)"
FROM estudiantes;

-- Contar registros
SELECT COUNT(*) AS total_estudiantes FROM estudiantes;
SELECT COUNT(*) AS total_libros FROM libros;

-- ============================================================================
-- 4. FILTROS CON WHERE
-- ============================================================================

-- Operadores relacionales
SELECT * FROM estudiantes WHERE edad = 20;
SELECT * FROM estudiantes WHERE edad > 21;
SELECT * FROM estudiantes WHERE edad >= 21;
SELECT * FROM estudiantes WHERE edad < 22;
SELECT * FROM estudiantes WHERE ciudad != 'Madrid';
SELECT * FROM estudiantes WHERE ciudad <> 'Madrid'; -- Alternativa

-- Operadores lógicos (AND, OR, NOT)
SELECT * FROM estudiantes WHERE edad > 20 AND ciudad = 'Madrid';
SELECT * FROM estudiantes WHERE ciudad = 'Madrid' OR ciudad = 'Barcelona';
SELECT * FROM estudiantes WHERE NOT ciudad = 'Madrid';
SELECT * FROM estudiantes WHERE edad BETWEEN 20 AND 23;

-- Operador IN (lista de valores)
SELECT * FROM estudiantes WHERE ciudad IN ('Madrid', 'Barcelona', 'Valencia');
SELECT * FROM libros WHERE año_publicacion IN (1967, 1943, 2003);

-- Operador LIKE (búsqueda de patrones)
SELECT * FROM estudiantes WHERE nombre LIKE 'A%';        -- Empieza con A
SELECT * FROM estudiantes WHERE nombre LIKE '%ez';       -- Termina con ez
SELECT * FROM estudiantes WHERE nombre LIKE '%ar%';      -- Contiene ar
SELECT * FROM estudiantes WHERE email LIKE '%@email.com'; -- Dominio específico

SELECT * FROM libros WHERE titulo LIKE '%muerte%';
SELECT * FROM libros WHERE autor LIKE 'Gabriel%';

-- Operador BETWEEN (rangos)
SELECT * FROM estudiantes WHERE edad BETWEEN 18 AND 22;
SELECT * FROM libros WHERE año_publicacion BETWEEN 1950 AND 2000;

-- Valores NULL
SELECT * FROM estudiantes WHERE ciudad IS NULL;
SELECT * FROM estudiantes WHERE ciudad IS NOT NULL;

-- Consultas sobre booleanos
SELECT * FROM libros WHERE disponible = TRUE;
SELECT * FROM libros WHERE disponible = FALSE;

-- ============================================================================
-- 5. ORDENAMIENTO CON ORDER BY
-- ============================================================================

-- Orden ascendente (por defecto)
SELECT * FROM estudiantes ORDER BY nombre;
SELECT * FROM estudiantes ORDER BY nombre ASC;
SELECT * FROM estudiantes ORDER BY edad ASC;

-- Orden descendente
SELECT * FROM estudiantes ORDER BY edad DESC;
SELECT * FROM libros ORDER BY año_publicacion DESC;

-- Ordenar por múltiples columnas
SELECT * FROM estudiantes ORDER BY ciudad ASC, nombre ASC;
SELECT * FROM estudiantes ORDER BY edad DESC, nombre ASC;

-- Combinar filtros con ordenamiento
SELECT * FROM estudiantes 
WHERE edad > 20 
ORDER BY edad DESC;

SELECT * FROM libros 
WHERE disponible = TRUE 
ORDER BY año_publicacion DESC;

-- ============================================================================
-- 6. LÍMITES CON LIMIT
-- ============================================================================

-- Obtener los primeros N registros
SELECT * FROM estudiantes LIMIT 5;
SELECT * FROM libros LIMIT 3;

-- Combinar ORDER BY con LIMIT
SELECT * FROM estudiantes ORDER BY edad DESC LIMIT 3;  -- Los 3 más mayores
SELECT * FROM libros ORDER BY año_publicacion ASC LIMIT 5;  -- Los 5 más antiguos

-- Paginación con LIMIT y OFFSET
SELECT * FROM estudiantes LIMIT 3 OFFSET 0;  -- Página 1 (registros 1-3)
SELECT * FROM estudiantes LIMIT 3 OFFSET 3;  -- Página 2 (registros 4-6)
SELECT * FROM estudiantes LIMIT 3 OFFSET 6;  -- Página 3 (registros 7-9)

-- ============================================================================
-- 7. OPERACIÓN UPDATE - Actualizar datos
-- ============================================================================

-- Actualizar un solo campo
UPDATE libros 
SET disponible = FALSE 
WHERE id = 1;

-- Actualizar múltiples campos
UPDATE estudiantes 
SET edad = 23, ciudad = 'Zaragoza' 
WHERE id = 5;

-- Actualizar con condiciones
UPDATE libros 
SET disponible = TRUE 
WHERE año_publicacion < 1980;

UPDATE estudiantes 
SET ciudad = 'Madrid' 
WHERE ciudad = 'Valencia' AND edad > 23;

-- ⚠️ Cuidado: Sin WHERE actualiza TODOS los registros
-- UPDATE libros SET disponible = TRUE;  -- Esto afectaría TODOS los libros

-- ============================================================================
-- 8. OPERACIÓN DELETE - Eliminar datos
-- ============================================================================

-- Eliminar registros específicos
DELETE FROM estudiantes WHERE id = 10;

-- Eliminar con condiciones
DELETE FROM libros WHERE año_publicacion < 1950;

-- Eliminar registros que cumplan múltiples condiciones
DELETE FROM estudiantes 
WHERE edad < 18 OR ciudad IS NULL;

-- ⚠️ PELIGRO: Sin WHERE elimina TODOS los registros
-- DELETE FROM libros;  -- Esto borraría TODA la tabla

-- ============================================================================
-- 9. CONSULTAS AVANZADAS Y COMBINADAS
-- ============================================================================

-- Consultar con funciones agregadas
SELECT ciudad, COUNT(*) AS cantidad_estudiantes 
FROM estudiantes 
GROUP BY ciudad;

SELECT ciudad, AVG(edad) AS edad_promedio 
FROM estudiantes 
GROUP BY ciudad;

-- Subconsultas
SELECT * FROM estudiantes 
WHERE edad > (SELECT AVG(edad) FROM estudiantes);

SELECT * FROM libros 
WHERE año_publicacion = (SELECT MAX(año_publicacion) FROM libros);

-- Consultas con DISTINCT (valores únicos)
SELECT DISTINCT ciudad FROM estudiantes;
SELECT DISTINCT autor FROM libros;

-- Contar con filtros
SELECT COUNT(*) AS libros_disponibles 
FROM libros 
WHERE disponible = TRUE;

SELECT COUNT(*) AS estudiantes_madrid 
FROM estudiantes 
WHERE ciudad = 'Madrid';

-- Búsquedas complejas
SELECT titulo, autor, año_publicacion
FROM libros
WHERE (autor LIKE '%García%' OR autor LIKE '%Cortázar%')
  AND año_publicacion BETWEEN 1960 AND 1990
ORDER BY año_publicacion DESC;

-- ============================================================================
-- 10. BUENAS PRÁCTICAS Y SEGURIDAD
-- ============================================================================

-- Crear índices para mejorar el rendimiento
CREATE INDEX idx_estudiante_ciudad ON estudiantes(ciudad);
CREATE INDEX idx_estudiante_email ON estudiantes(email);
CREATE INDEX idx_libro_isbn ON libros(isbn);
CREATE INDEX idx_libro_autor ON libros(autor);

-- Ver índices creados (SQLite)
-- SELECT * FROM sqlite_master WHERE type = 'index';

-- Transacciones para operaciones múltiples
BEGIN TRANSACTION;
    UPDATE libros SET disponible = FALSE WHERE id = 3;
    INSERT INTO estudiantes (nombre, email, edad, ciudad) 
    VALUES ('Test Usuario', 'test@email.com', 20, 'Test');
COMMIT;

-- Rollback si algo sale mal
BEGIN TRANSACTION;
    DELETE FROM estudiantes WHERE edad < 20;
    -- Si algo sale mal:
ROLLBACK;

-- ============================================================================
-- 11. CONSULTAS DE MANTENIMIENTO
-- ============================================================================

-- Ver estructura de las tablas
PRAGMA table_info(estudiantes);
PRAGMA table_info(libros);

-- Contar registros totales
SELECT 
    (SELECT COUNT(*) FROM estudiantes) AS total_estudiantes,
    (SELECT COUNT(*) FROM libros) AS total_libros;

-- Estadísticas de la base de datos
SELECT 
    MIN(edad) AS edad_minima,
    MAX(edad) AS edad_maxima,
    AVG(edad) AS edad_promedio,
    COUNT(*) AS total_estudiantes
FROM estudiantes;

SELECT 
    MIN(año_publicacion) AS libro_mas_antiguo,
    MAX(año_publicacion) AS libro_mas_reciente,
    COUNT(*) AS total_libros,
    SUM(CASE WHEN disponible = TRUE THEN 1 ELSE 0 END) AS libros_disponibles
FROM libros;

-- ============================================================================
-- 12. EJEMPLOS DE CONSULTAS PARA EL EJERCICIO PRÁCTICO
-- ============================================================================

-- 1. Estudiantes de una ciudad específica mayores de 20 años
SELECT nombre, email, edad 
FROM estudiantes 
WHERE ciudad = 'Madrid' AND edad > 20 
ORDER BY edad DESC;

-- 2. Libros publicados en un rango de años
SELECT titulo, autor, año_publicacion 
FROM libros 
WHERE año_publicacion BETWEEN 1980 AND 2000 
ORDER BY año_publicacion;

-- 3. Buscar libros cuyo título contenga una palabra
SELECT titulo, autor 
FROM libros 
WHERE titulo LIKE '%muerte%' OR titulo LIKE '%vida%';

-- 4. Contar estudiantes por ciudad
SELECT ciudad, COUNT(*) AS cantidad 
FROM estudiantes 
GROUP BY ciudad 
ORDER BY cantidad DESC;

-- 5. Libros no disponibles
SELECT titulo, autor, isbn 
FROM libros 
WHERE disponible = FALSE;

-- 6. Los 3 estudiantes más jóvenes
SELECT nombre, edad, ciudad 
FROM estudiantes 
ORDER BY edad ASC 
LIMIT 3;

-- 7. Autores con más de un libro
SELECT autor, COUNT(*) AS cantidad_libros 
FROM libros 
GROUP BY autor 
HAVING COUNT(*) > 1;

-- 8. Actualizar disponibilidad de libros antiguos
UPDATE libros 
SET disponible = TRUE 
WHERE año_publicacion < 1970;

-- 9. Eliminar estudiantes sin ciudad asignada
DELETE FROM estudiantes 
WHERE ciudad IS NULL OR ciudad = '';

-- 10. Búsqueda combinada con múltiples criterios
SELECT 
    e.nombre,
    e.email,
    e.ciudad,
    e.edad
FROM estudiantes e
WHERE e.edad BETWEEN 20 AND 25
  AND e.ciudad IN ('Madrid', 'Barcelona')
  AND e.email LIKE '%@email.com'
ORDER BY e.ciudad, e.edad;

-- ============================================================================
-- NOTAS FINALES
-- ============================================================================

/*
RECORDATORIOS IMPORTANTES:

1. Siempre usa WHERE en UPDATE y DELETE para evitar modificar toda la tabla
2. Haz backup antes de operaciones destructivas
3. Usa transacciones para operaciones críticas
4. Crea índices en columnas que consultas frecuentemente
5. Valida datos antes de insertar
6. Usa parámetros preparados en tu código (prevención de SQL injection)
7. Documenta consultas complejas
8. Prueba en un entorno de desarrollo primero

TIPS DE OPTIMIZACIÓN:

- Evita SELECT * cuando solo necesitas algunas columnas
- Usa índices en columnas de WHERE, ORDER BY y JOIN
- Limita resultados con LIMIT cuando sea apropiado
- Usa EXPLAIN para analizar el rendimiento de consultas complejas
- Normaliza tu base de datos para reducir redundancia

¡Practica estas consultas y experimenta con tus propias variaciones!
*/
