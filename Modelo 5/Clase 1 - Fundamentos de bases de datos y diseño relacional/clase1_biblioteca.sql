-- Clase 1: Fundamentos de Bases de Datos y Diseño Relacional
-- Script: clase1_biblioteca.sql
-- Objetivo: Crear un esquema de biblioteca en PostgreSQL con PK/FK, restricciones, datos de ejemplo e inspecciones.
-- Requisitos: PostgreSQL 12+

-- 0) Opcional: crear base de datos (ejecutar con un superusuario)
-- CREATE DATABASE clase1;
-- \c clase1

-- 1) Crear esquema dedicado
CREATE SCHEMA IF NOT EXISTS biblioteca AUTHORIZATION CURRENT_USER;
SET search_path TO biblioteca, public;

-- 2) Tipos y utilidades (si hiciera falta)
-- Ninguno por ahora

-- 3) Tablas

-- 3.1) AUTOR
CREATE TABLE IF NOT EXISTS autor (
    id          BIGSERIAL PRIMARY KEY,
    nombre      VARCHAR(150) NOT NULL,
    nacionalidad VARCHAR(100),
    CONSTRAINT uq_autor_nombre_nacionalidad UNIQUE (nombre, nacionalidad)
);

-- 3.2) USUARIO (lector)
CREATE TABLE IF NOT EXISTS usuario (
    id          BIGSERIAL PRIMARY KEY,
    nombre      VARCHAR(150) NOT NULL,
    email       VARCHAR(255) NOT NULL,
    CONSTRAINT uq_usuario_email UNIQUE (email),
    CONSTRAINT ck_usuario_email_formato CHECK (position('@' in email) > 1)
);

-- 3.3) LIBRO
CREATE TABLE IF NOT EXISTS libro (
    id          BIGSERIAL PRIMARY KEY,
    titulo      VARCHAR(200) NOT NULL,
    anio        INT CHECK (anio >= 0 AND anio <= EXTRACT(YEAR FROM CURRENT_DATE)::INT),
    id_autor    BIGINT NOT NULL,
    CONSTRAINT fk_libro_autor FOREIGN KEY (id_autor) REFERENCES autor(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- 3.4) PRESTAMO
CREATE TABLE IF NOT EXISTS prestamo (
    id              BIGSERIAL PRIMARY KEY,
    id_libro        BIGINT NOT NULL,
    id_usuario      BIGINT NOT NULL,
    fecha_inicio    DATE NOT NULL DEFAULT CURRENT_DATE,
    fecha_fin       DATE,
    CONSTRAINT fk_prestamo_libro FOREIGN KEY (id_libro) REFERENCES libro(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_prestamo_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT ck_prestamo_fechas CHECK (fecha_fin IS NULL OR fecha_fin >= fecha_inicio)
);

-- 4) Índices útiles (además de PK/UK)
CREATE INDEX IF NOT EXISTS idx_libro_titulo ON libro (titulo);
CREATE INDEX IF NOT EXISTS idx_prestamo_usuario ON prestamo (id_usuario);
CREATE INDEX IF NOT EXISTS idx_prestamo_libro ON prestamo (id_libro);

-- 5) Datos de ejemplo
INSERT INTO autor (nombre, nacionalidad) VALUES
    ('Gabriel García Márquez', 'Colombia'),
    ('Jorge Luis Borges', 'Argentina'),
    ('Isabel Allende', 'Chile')
ON CONFLICT DO NOTHING;

INSERT INTO usuario (nombre, email) VALUES
    ('Ana Pérez', 'ana.perez@example.com'),
    ('Luis Gómez', 'luis.gomez@example.com')
ON CONFLICT DO NOTHING;

INSERT INTO libro (titulo, anio, id_autor)
SELECT 'Cien años de soledad', 1967, a.id FROM autor a WHERE a.nombre = 'Gabriel García Márquez' AND a.nacionalidad='Colombia'
ON CONFLICT DO NOTHING;

INSERT INTO libro (titulo, anio, id_autor)
SELECT 'El Aleph', 1949, a.id FROM autor a WHERE a.nombre = 'Jorge Luis Borges' AND a.nacionalidad='Argentina'
ON CONFLICT DO NOTHING;

INSERT INTO libro (titulo, anio, id_autor)
SELECT 'La casa de los espíritus', 1982, a.id FROM autor a WHERE a.nombre = 'Isabel Allende' AND a.nacionalidad='Chile'
ON CONFLICT DO NOTHING;

INSERT INTO prestamo (id_libro, id_usuario, fecha_inicio, fecha_fin)
SELECT l.id, u.id, DATE '2025-10-01', DATE '2025-10-10'
FROM libro l CROSS JOIN usuario u
WHERE l.titulo = 'Cien años de soledad' AND u.email='ana.perez@example.com'
ON CONFLICT DO NOTHING;

INSERT INTO prestamo (id_libro, id_usuario, fecha_inicio)
SELECT l.id, u.id, DATE '2025-10-05'
FROM libro l CROSS JOIN usuario u
WHERE l.titulo = 'El Aleph' AND u.email='luis.gomez@example.com'
ON CONFLICT DO NOTHING;

-- 6) Consultas de verificación
-- 6.1) Conteos
SELECT 'autores' AS tabla, COUNT(*) FROM autor
UNION ALL
SELECT 'usuarios', COUNT(*) FROM usuario
UNION ALL
SELECT 'libros', COUNT(*) FROM libro
UNION ALL
SELECT 'prestamos', COUNT(*) FROM prestamo;

-- 6.2) Join para ver préstamos con detalle
SELECT p.id AS prestamo_id, l.titulo, u.nombre AS usuario, p.fecha_inicio, p.fecha_fin
FROM prestamo p
JOIN libro l   ON l.id = p.id_libro
JOIN usuario u ON u.id = p.id_usuario
ORDER BY p.id;

-- 6.3) Libros por autor
SELECT a.nombre AS autor, COUNT(*) AS cantidad_libros
FROM autor a
LEFT JOIN libro l ON l.id_autor = a.id
GROUP BY a.nombre
ORDER BY cantidad_libros DESC;

-- 6.4) Prestamos activos (sin fecha_fin)
SELECT p.*
FROM prestamo p
WHERE p.fecha_fin IS NULL;

-- 7) Ejemplos de errores comunes (comentados) y cómo evitarlos
-- 7.1) Insertar libro con id_autor inexistente → violación de FK
-- INSERT INTO libro (titulo, anio, id_autor) VALUES ('Libro inválido', 2020, 999999);

-- 7.2) Email inválido → viola CHECK del formato
-- INSERT INTO usuario (nombre, email) VALUES ('Usuario Malo', 'sin-arroba');

-- 7.3) fecha_fin < fecha_inicio → viola CHECK de fechas
-- INSERT INTO prestamo (id_libro, id_usuario, fecha_inicio, fecha_fin)
-- VALUES (1, 1, DATE '2025-10-10', DATE '2025-10-01');

-- 8) Limpieza opcional (para repetir pruebas)
-- TRUNCATE prestamo, libro, usuario, autor RESTART IDENTITY CASCADE;
