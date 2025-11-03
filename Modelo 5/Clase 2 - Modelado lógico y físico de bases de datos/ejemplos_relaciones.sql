-- ============================================================================
-- EJEMPLOS PRÁCTICOS DE RELACIONES ENTRE TABLAS
-- Curso: Python Senior AI - Modelo 5
-- Clase 2: Modelado Lógico y Físico de Bases de Datos
-- ============================================================================

-- Crear base de datos para los ejemplos
CREATE DATABASE IF NOT EXISTS EjemplosRelaciones;
USE EjemplosRelaciones;

-- ============================================================================
-- EJEMPLO 1: RELACIÓN UNO A UNO (1:1)
-- Caso: Persona y Pasaporte
-- ============================================================================

-- Tabla principal: Personas
CREATE TABLE Personas (
    id_persona INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_email (email)
);

-- Tabla relacionada 1:1: Pasaportes
CREATE TABLE Pasaportes (
    id_pasaporte INT AUTO_INCREMENT PRIMARY KEY,
    numero_pasaporte VARCHAR(20) UNIQUE NOT NULL,
    pais_emision VARCHAR(50) NOT NULL,
    fecha_emision DATE NOT NULL,
    fecha_expiracion DATE NOT NULL,
    id_persona INT UNIQUE NOT NULL, -- UNIQUE garantiza la relación 1:1
    FOREIGN KEY (id_persona) REFERENCES Personas(id_persona)
        ON DELETE CASCADE  -- Si se elimina la persona, se elimina el pasaporte
        ON UPDATE CASCADE, -- Si se actualiza el id_persona, se actualiza aquí también
    INDEX idx_numero_pasaporte (numero_pasaporte),
    CONSTRAINT chk_fecha_expiracion CHECK (fecha_expiracion > fecha_emision)
);

-- Insertar datos de ejemplo
INSERT INTO Personas (nombre, apellido, fecha_nacimiento, email) VALUES
('Juan', 'Pérez', '1990-05-15', 'juan.perez@email.com'),
('María', 'González', '1985-08-22', 'maria.gonzalez@email.com'),
('Carlos', 'Rodríguez', '1992-03-10', 'carlos.rodriguez@email.com');

INSERT INTO Pasaportes (numero_pasaporte, pais_emision, fecha_emision, fecha_expiracion, id_persona) VALUES
('AB123456', 'Colombia', '2020-01-15', '2030-01-14', 1),
('CD789012', 'México', '2019-06-20', '2029-06-19', 2),
('EF345678', 'Argentina', '2021-11-05', '2031-11-04', 3);

-- Consulta para ver la relación 1:1
SELECT 
    p.nombre,
    p.apellido,
    pas.numero_pasaporte,
    pas.pais_emision,
    pas.fecha_expiracion
FROM Personas p
INNER JOIN Pasaportes pas ON p.id_persona = pas.id_persona;

-- ============================================================================
-- EJEMPLO 2: RELACIÓN UNO A MUCHOS (1:N)
-- Caso: Cliente y Pedidos (E-commerce)
-- ============================================================================

-- Tabla padre: Clientes
CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(200) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    direccion TEXT,
    ciudad VARCHAR(100),
    pais VARCHAR(50) DEFAULT 'Colombia',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    INDEX idx_email_cliente (email),
    INDEX idx_ciudad (ciudad)
);

-- Tabla hija: Pedidos
CREATE TABLE Pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    numero_pedido VARCHAR(50) UNIQUE NOT NULL,
    id_cliente INT NOT NULL, -- FK sin UNIQUE permite múltiples pedidos por cliente (1:N)
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('Pendiente', 'Procesando', 'Enviado', 'Entregado', 'Cancelado') DEFAULT 'Pendiente',
    total DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    notas TEXT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
        ON DELETE RESTRICT  -- No permite eliminar un cliente con pedidos
        ON UPDATE CASCADE,
    INDEX idx_numero_pedido (numero_pedido),
    INDEX idx_fecha_pedido (fecha_pedido),
    INDEX idx_estado (estado),
    CONSTRAINT chk_total_positivo CHECK (total >= 0)
);

-- Insertar datos de ejemplo
INSERT INTO Clientes (nombre_completo, email, telefono, direccion, ciudad) VALUES
('Ana Martínez', 'ana.martinez@email.com', '3001234567', 'Calle 123 #45-67', 'Bogotá'),
('Pedro Sánchez', 'pedro.sanchez@email.com', '3009876543', 'Carrera 45 #12-34', 'Medellín'),
('Laura Torres', 'laura.torres@email.com', '3005556677', 'Avenida 7 #89-12', 'Cali');

INSERT INTO Pedidos (numero_pedido, id_cliente, estado, total, notas) VALUES
('PED-2024-001', 1, 'Entregado', 150000.00, 'Entrega rápida solicitada'),
('PED-2024-002', 1, 'Procesando', 85000.00, NULL),
('PED-2024-003', 2, 'Enviado', 220000.00, 'Envío estándar'),
('PED-2024-004', 1, 'Pendiente', 95000.00, 'Pago contra entrega'),
('PED-2024-005', 3, 'Entregado', 340000.00, NULL);

-- Consulta para ver la relación 1:N
-- Mostrar clientes con todos sus pedidos
SELECT 
    c.nombre_completo,
    c.ciudad,
    COUNT(p.id_pedido) AS total_pedidos,
    SUM(p.total) AS total_gastado,
    GROUP_CONCAT(p.numero_pedido ORDER BY p.fecha_pedido) AS pedidos
FROM Clientes c
LEFT JOIN Pedidos p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente, c.nombre_completo, c.ciudad
ORDER BY total_gastado DESC;

-- Consulta: Pedidos de un cliente específico
SELECT 
    p.numero_pedido,
    p.fecha_pedido,
    p.estado,
    p.total,
    c.nombre_completo AS cliente
FROM Pedidos p
INNER JOIN Clientes c ON p.id_cliente = c.id_cliente
WHERE c.id_cliente = 1
ORDER BY p.fecha_pedido DESC;

-- ============================================================================
-- EJEMPLO 3: RELACIÓN MUCHOS A MUCHOS (N:M)
-- Caso: Estudiantes y Cursos (Sistema Académico)
-- ============================================================================

-- Primera tabla: Estudiantes
CREATE TABLE Estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    codigo_estudiante VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    carrera VARCHAR(100),
    semestre INT DEFAULT 1,
    fecha_ingreso DATE NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    INDEX idx_codigo_estudiante (codigo_estudiante),
    INDEX idx_carrera (carrera),
    CONSTRAINT chk_semestre CHECK (semestre BETWEEN 1 AND 10)
);

-- Segunda tabla: Cursos
CREATE TABLE Cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    codigo_curso VARCHAR(20) UNIQUE NOT NULL,
    nombre_curso VARCHAR(150) NOT NULL,
    creditos INT NOT NULL,
    descripcion TEXT,
    cupo_maximo INT DEFAULT 30,
    id_profesor INT,
    INDEX idx_codigo_curso (codigo_curso),
    CONSTRAINT chk_creditos CHECK (creditos > 0),
    CONSTRAINT chk_cupo CHECK (cupo_maximo > 0)
);

-- Tabla de profesores (para completar el ejemplo)
CREATE TABLE Profesores (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100),
    email VARCHAR(150) UNIQUE NOT NULL
);

-- Agregar la FK a Cursos después de crear Profesores
ALTER TABLE Cursos
ADD FOREIGN KEY (id_profesor) REFERENCES Profesores(id_profesor)
    ON DELETE SET NULL
    ON UPDATE CASCADE;

-- TABLA INTERMEDIA para la relación N:M
CREATE TABLE Inscripciones (
    id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_curso INT NOT NULL,
    fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nota_final DECIMAL(3, 2) DEFAULT NULL,
    estado ENUM('Inscrito', 'Aprobado', 'Reprobado', 'Retirado') DEFAULT 'Inscrito',
    asistencia_porcentaje INT DEFAULT 0,
    -- Claves foráneas a ambas tablas
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    -- Clave primaria compuesta (alternativa a id_inscripcion)
    -- O restricción UNIQUE para evitar inscripciones duplicadas
    UNIQUE KEY uk_estudiante_curso (id_estudiante, id_curso),
    INDEX idx_estado (estado),
    CONSTRAINT chk_nota CHECK (nota_final IS NULL OR (nota_final >= 0 AND nota_final <= 5)),
    CONSTRAINT chk_asistencia CHECK (asistencia_porcentaje BETWEEN 0 AND 100)
);

-- Insertar datos de ejemplo
INSERT INTO Profesores (nombre, apellido, especialidad, email) VALUES
('Roberto', 'García', 'Matemáticas', 'roberto.garcia@universidad.edu'),
('Sandra', 'López', 'Programación', 'sandra.lopez@universidad.edu'),
('Miguel', 'Hernández', 'Bases de Datos', 'miguel.hernandez@universidad.edu');

INSERT INTO Estudiantes (codigo_estudiante, nombre, apellido, email, carrera, semestre, fecha_ingreso) VALUES
('EST-2024-001', 'Sofía', 'Ramírez', 'sofia.ramirez@estudiante.edu', 'Ingeniería de Sistemas', 3, '2023-01-15'),
('EST-2024-002', 'Diego', 'Morales', 'diego.morales@estudiante.edu', 'Ingeniería de Sistemas', 4, '2022-07-20'),
('EST-2024-003', 'Valentina', 'Castro', 'valentina.castro@estudiante.edu', 'Ingeniería Industrial', 2, '2023-07-15'),
('EST-2024-004', 'Andrés', 'Vargas', 'andres.vargas@estudiante.edu', 'Ingeniería de Sistemas', 3, '2023-01-15');

INSERT INTO Cursos (codigo_curso, nombre_curso, creditos, descripcion, cupo_maximo, id_profesor) VALUES
('MAT-301', 'Cálculo III', 4, 'Cálculo multivariable y ecuaciones diferenciales', 35, 1),
('PROG-401', 'Programación Avanzada', 3, 'Paradigmas de programación y patrones de diseño', 30, 2),
('BD-301', 'Bases de Datos', 3, 'Diseño y administración de bases de datos relacionales', 40, 3),
('PROG-201', 'Estructuras de Datos', 4, 'Algoritmos y estructuras de datos fundamentales', 30, 2);

-- Inscribir estudiantes en cursos (relación N:M)
INSERT INTO Inscripciones (id_estudiante, id_curso, nota_final, estado, asistencia_porcentaje) VALUES
-- Sofía inscrita en 3 cursos
(1, 1, 4.5, 'Aprobado', 95),
(1, 2, NULL, 'Inscrito', 85),
(1, 3, 3.8, 'Aprobado', 90),
-- Diego inscrito en 2 cursos
(2, 2, 4.2, 'Aprobado', 88),
(2, 3, NULL, 'Inscrito', 92),
-- Valentina inscrita en 2 cursos
(3, 1, NULL, 'Inscrito', 80),
(3, 4, 3.5, 'Aprobado', 87),
-- Andrés inscrito en 3 cursos
(4, 2, NULL, 'Inscrito', 78),
(4, 3, NULL, 'Inscrito', 91),
(4, 4, 4.0, 'Aprobado', 93);

-- CONSULTAS PARA LA RELACIÓN N:M

-- 1. Ver todos los estudiantes de un curso específico
SELECT 
    c.codigo_curso,
    c.nombre_curso,
    e.codigo_estudiante,
    CONCAT(e.nombre, ' ', e.apellido) AS estudiante,
    i.fecha_inscripcion,
    i.estado,
    i.nota_final
FROM Cursos c
INNER JOIN Inscripciones i ON c.id_curso = i.id_curso
INNER JOIN Estudiantes e ON i.id_estudiante = e.id_estudiante
WHERE c.codigo_curso = 'BD-301'
ORDER BY e.apellido;

-- 2. Ver todos los cursos de un estudiante específico
SELECT 
    e.codigo_estudiante,
    CONCAT(e.nombre, ' ', e.apellido) AS estudiante,
    c.codigo_curso,
    c.nombre_curso,
    c.creditos,
    CONCAT(p.nombre, ' ', p.apellido) AS profesor,
    i.estado,
    i.nota_final
FROM Estudiantes e
INNER JOIN Inscripciones i ON e.id_estudiante = i.id_estudiante
INNER JOIN Cursos c ON i.id_curso = c.id_curso
LEFT JOIN Profesores p ON c.id_profesor = p.id_profesor
WHERE e.codigo_estudiante = 'EST-2024-001'
ORDER BY c.codigo_curso;

-- 3. Reporte completo: estudiantes, cursos inscritos y promedios
SELECT 
    e.codigo_estudiante,
    CONCAT(e.nombre, ' ', e.apellido) AS estudiante,
    e.carrera,
    COUNT(i.id_curso) AS total_cursos,
    SUM(CASE WHEN i.estado = 'Aprobado' THEN 1 ELSE 0 END) AS cursos_aprobados,
    ROUND(AVG(CASE WHEN i.nota_final IS NOT NULL THEN i.nota_final END), 2) AS promedio,
    SUM(CASE WHEN i.nota_final IS NOT NULL THEN c.creditos ELSE 0 END) AS creditos_cursados
FROM Estudiantes e
LEFT JOIN Inscripciones i ON e.id_estudiante = i.id_estudiante
LEFT JOIN Cursos c ON i.id_curso = c.id_curso
GROUP BY e.id_estudiante, e.codigo_estudiante, e.nombre, e.apellido, e.carrera
ORDER BY promedio DESC;

-- 4. Cursos con su cantidad de estudiantes inscritos
SELECT 
    c.codigo_curso,
    c.nombre_curso,
    CONCAT(p.nombre, ' ', p.apellido) AS profesor,
    COUNT(i.id_estudiante) AS estudiantes_inscritos,
    c.cupo_maximo,
    (c.cupo_maximo - COUNT(i.id_estudiante)) AS cupos_disponibles
FROM Cursos c
LEFT JOIN Inscripciones i ON c.id_curso = i.id_curso
LEFT JOIN Profesores p ON c.id_profesor = p.id_profesor
GROUP BY c.id_curso, c.codigo_curso, c.nombre_curso, c.cupo_maximo, p.nombre, p.apellido
ORDER BY estudiantes_inscritos DESC;

-- ============================================================================
-- EJEMPLO 4: COMBINACIÓN DE RELACIONES (Sistema E-commerce Completo)
-- ============================================================================

-- Tabla: Categorías (1:N con Productos)
CREATE TABLE Categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre_categoria VARCHAR(100) UNIQUE NOT NULL,
    descripcion TEXT,
    activa BOOLEAN DEFAULT TRUE,
    INDEX idx_nombre_categoria (nombre_categoria)
);

-- Tabla: Productos (N:1 con Categorías)
CREATE TABLE Productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    codigo_producto VARCHAR(50) UNIQUE NOT NULL,
    nombre_producto VARCHAR(200) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    id_categoria INT NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    INDEX idx_codigo_producto (codigo_producto),
    INDEX idx_nombre_producto (nombre_producto),
    INDEX idx_categoria (id_categoria),
    CONSTRAINT chk_precio_positivo CHECK (precio > 0),
    CONSTRAINT chk_stock_positivo CHECK (stock >= 0)
);

-- Tabla: DetallesPedidos (N:M entre Pedidos y Productos)
CREATE TABLE DetallesPedidos (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    INDEX idx_pedido (id_pedido),
    INDEX idx_producto (id_producto),
    CONSTRAINT chk_cantidad_positiva CHECK (cantidad > 0),
    CONSTRAINT chk_precio_unitario_positivo CHECK (precio_unitario > 0)
);

-- Insertar datos de ejemplo
INSERT INTO Categorias (nombre_categoria, descripcion) VALUES
('Electrónicos', 'Dispositivos y accesorios electrónicos'),
('Ropa', 'Vestimenta y accesorios de moda'),
('Libros', 'Libros físicos y digitales'),
('Deportes', 'Artículos deportivos y fitness');

INSERT INTO Productos (codigo_producto, nombre_producto, descripcion, precio, stock, id_categoria) VALUES
('ELEC-001', 'Laptop HP 15"', 'Laptop Intel i5, 8GB RAM, 256GB SSD', 2500000, 15, 1),
('ELEC-002', 'Mouse Inalámbrico', 'Mouse ergonómico con batería recargable', 45000, 50, 1),
('ROPA-001', 'Camiseta Deportiva', 'Camiseta de algodón, varios colores', 35000, 100, 2),
('LIBRO-001', 'Clean Code', 'Libro sobre buenas prácticas de programación', 120000, 25, 3),
('DEP-001', 'Pelota de Fútbol', 'Pelota profesional tamaño 5', 80000, 30, 4);

-- Insertar detalles de pedidos (productos en cada pedido)
INSERT INTO DetallesPedidos (id_pedido, id_producto, cantidad, precio_unitario, subtotal) VALUES
-- Pedido 1 (Ana)
(1, 2, 1, 45000, 45000),
(1, 3, 3, 35000, 105000),
-- Pedido 2 (Ana)
(2, 4, 1, 120000, 120000),
-- Pedido 3 (Pedro)
(3, 1, 1, 2500000, 2500000),
(3, 2, 2, 45000, 90000),
-- Pedido 4 (Ana)
(4, 5, 1, 80000, 80000),
-- Pedido 5 (Laura)
(5, 1, 1, 2500000, 2500000),
(5, 3, 2, 35000, 70000);

-- CONSULTAS AVANZADAS DEL SISTEMA COMPLETO

-- 1. Reporte completo de un pedido con todos sus productos
SELECT 
    p.numero_pedido,
    p.fecha_pedido,
    p.estado,
    c.nombre_completo AS cliente,
    prod.codigo_producto,
    prod.nombre_producto,
    cat.nombre_categoria,
    dp.cantidad,
    dp.precio_unitario,
    dp.subtotal
FROM Pedidos p
INNER JOIN Clientes c ON p.id_cliente = c.id_cliente
INNER JOIN DetallesPedidos dp ON p.id_pedido = dp.id_pedido
INNER JOIN Productos prod ON dp.id_producto = prod.id_producto
INNER JOIN Categorias cat ON prod.id_categoria = cat.id_categoria
WHERE p.numero_pedido = 'PED-2024-001'
ORDER BY dp.id_detalle;

-- 2. Productos más vendidos
SELECT 
    prod.codigo_producto,
    prod.nombre_producto,
    cat.nombre_categoria,
    SUM(dp.cantidad) AS total_vendido,
    COUNT(DISTINCT dp.id_pedido) AS numero_pedidos,
    SUM(dp.subtotal) AS ingresos_totales
FROM Productos prod
INNER JOIN DetallesPedidos dp ON prod.id_producto = dp.id_producto
INNER JOIN Categorias cat ON prod.id_categoria = cat.id_categoria
GROUP BY prod.id_producto, prod.codigo_producto, prod.nombre_producto, cat.nombre_categoria
ORDER BY total_vendido DESC;

-- 3. Clientes con mayor compra por categoría
SELECT 
    c.nombre_completo,
    cat.nombre_categoria,
    COUNT(DISTINCT p.id_pedido) AS pedidos,
    SUM(dp.cantidad) AS productos_comprados,
    SUM(dp.subtotal) AS total_gastado
FROM Clientes c
INNER JOIN Pedidos p ON c.id_cliente = p.id_cliente
INNER JOIN DetallesPedidos dp ON p.id_pedido = dp.id_pedido
INNER JOIN Productos prod ON dp.id_producto = prod.id_producto
INNER JOIN Categorias cat ON prod.id_categoria = cat.id_categoria
GROUP BY c.id_cliente, c.nombre_completo, cat.id_categoria, cat.nombre_categoria
ORDER BY c.nombre_completo, total_gastado DESC;

-- ============================================================================
-- PROCEDIMIENTOS ALMACENADOS ÚTILES
-- ============================================================================

-- Procedimiento para inscribir un estudiante en un curso con validaciones
DELIMITER //

CREATE PROCEDURE InscribirEstudiante(
    IN p_codigo_estudiante VARCHAR(20),
    IN p_codigo_curso VARCHAR(20)
)
BEGIN
    DECLARE v_id_estudiante INT;
    DECLARE v_id_curso INT;
    DECLARE v_cupo_actual INT;
    DECLARE v_cupo_maximo INT;
    DECLARE v_ya_inscrito INT;
    
    -- Obtener IDs
    SELECT id_estudiante INTO v_id_estudiante 
    FROM Estudiantes 
    WHERE codigo_estudiante = p_codigo_estudiante AND activo = TRUE;
    
    SELECT id_curso, cupo_maximo INTO v_id_curso, v_cupo_maximo
    FROM Cursos 
    WHERE codigo_curso = p_codigo_curso;
    
    -- Verificar que existan
    IF v_id_estudiante IS NULL THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Estudiante no encontrado o inactivo';
    END IF;
    
    IF v_id_curso IS NULL THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Curso no encontrado';
    END IF;
    
    -- Verificar si ya está inscrito
    SELECT COUNT(*) INTO v_ya_inscrito
    FROM Inscripciones
    WHERE id_estudiante = v_id_estudiante 
    AND id_curso = v_id_curso;
    
    IF v_ya_inscrito > 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El estudiante ya está inscrito en este curso';
    END IF;
    
    -- Verificar cupos disponibles
    SELECT COUNT(*) INTO v_cupo_actual
    FROM Inscripciones
    WHERE id_curso = v_id_curso;
    
    IF v_cupo_actual >= v_cupo_maximo THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'No hay cupos disponibles en este curso';
    END IF;
    
    -- Inscribir
    INSERT INTO Inscripciones (id_estudiante, id_curso)
    VALUES (v_id_estudiante, v_id_curso);
    
    SELECT 'Inscripción exitosa' AS mensaje;
END //

DELIMITER ;

-- Ejemplo de uso del procedimiento
-- CALL InscribirEstudiante('EST-2024-001', 'PROG-401');

-- ============================================================================
-- VISTAS ÚTILES
-- ============================================================================

-- Vista: Resumen de estudiantes con su carga académica
CREATE VIEW VistaEstudiantesCargaAcademica AS
SELECT 
    e.codigo_estudiante,
    CONCAT(e.nombre, ' ', e.apellido) AS nombre_completo,
    e.carrera,
    e.semestre,
    COUNT(i.id_curso) AS cursos_actuales,
    SUM(c.creditos) AS creditos_inscritos,
    ROUND(AVG(CASE WHEN i.nota_final IS NOT NULL THEN i.nota_final END), 2) AS promedio_historico
FROM Estudiantes e
LEFT JOIN Inscripciones i ON e.id_estudiante = i.id_estudiante
LEFT JOIN Cursos c ON i.id_curso = c.id_curso
WHERE e.activo = TRUE
GROUP BY e.id_estudiante, e.codigo_estudiante, e.nombre, e.apellido, e.carrera, e.semestre;

-- Usar la vista
SELECT * FROM VistaEstudiantesCargaAcademica
ORDER BY creditos_inscritos DESC;

-- Vista: Productos con su stock y ventas
CREATE VIEW VistaProductosInventario AS
SELECT 
    p.codigo_producto,
    p.nombre_producto,
    c.nombre_categoria,
    p.precio,
    p.stock,
    COALESCE(SUM(dp.cantidad), 0) AS total_vendido,
    COALESCE(COUNT(DISTINCT dp.id_pedido), 0) AS numero_ventas,
    p.activo
FROM Productos p
INNER JOIN Categorias c ON p.id_categoria = c.id_categoria
LEFT JOIN DetallesPedidos dp ON p.id_producto = dp.id_producto
GROUP BY p.id_producto, p.codigo_producto, p.nombre_producto, 
         c.nombre_categoria, p.precio, p.stock, p.activo;

-- Usar la vista
SELECT * FROM VistaProductosInventario
WHERE stock < 20
ORDER BY total_vendido DESC;

-- ============================================================================
-- TRIGGERS PARA INTEGRIDAD DE DATOS
-- ============================================================================

-- Trigger: Actualizar el total del pedido cuando se inserta un detalle
DELIMITER //

CREATE TRIGGER ActualizarTotalPedido_Insert
AFTER INSERT ON DetallesPedidos
FOR EACH ROW
BEGIN
    UPDATE Pedidos
    SET total = (
        SELECT SUM(subtotal)
        FROM DetallesPedidos
        WHERE id_pedido = NEW.id_pedido
    )
    WHERE id_pedido = NEW.id_pedido;
END //

CREATE TRIGGER ActualizarTotalPedido_Update
AFTER UPDATE ON DetallesPedidos
FOR EACH ROW
BEGIN
    UPDATE Pedidos
    SET total = (
        SELECT SUM(subtotal)
        FROM DetallesPedidos
        WHERE id_pedido = NEW.id_pedido
    )
    WHERE id_pedido = NEW.id_pedido;
END //

CREATE TRIGGER ActualizarTotalPedido_Delete
AFTER DELETE ON DetallesPedidos
FOR EACH ROW
BEGIN
    UPDATE Pedidos
    SET total = COALESCE((
        SELECT SUM(subtotal)
        FROM DetallesPedidos
        WHERE id_pedido = OLD.id_pedido
    ), 0)
    WHERE id_pedido = OLD.id_pedido;
END //

DELIMITER ;

-- ============================================================================
-- CONSULTAS DE ANÁLISIS Y REPORTES
-- ============================================================================

-- Análisis de ventas por categoría y mes
SELECT 
    DATE_FORMAT(p.fecha_pedido, '%Y-%m') AS mes,
    cat.nombre_categoria,
    COUNT(DISTINCT p.id_pedido) AS numero_pedidos,
    SUM(dp.cantidad) AS productos_vendidos,
    SUM(dp.subtotal) AS ingresos
FROM Pedidos p
INNER JOIN DetallesPedidos dp ON p.id_pedido = dp.id_pedido
INNER JOIN Productos prod ON dp.id_producto = prod.id_producto
INNER JOIN Categorias cat ON prod.id_categoria = cat.id_categoria
WHERE p.estado NOT IN ('Cancelado')
GROUP BY DATE_FORMAT(p.fecha_pedido, '%Y-%m'), cat.id_categoria, cat.nombre_categoria
ORDER BY mes DESC, ingresos DESC;

-- Top 5 estudiantes con mejor promedio
SELECT 
    e.codigo_estudiante,
    CONCAT(e.nombre, ' ', e.apellido) AS estudiante,
    e.carrera,
    COUNT(CASE WHEN i.estado = 'Aprobado' THEN 1 END) AS cursos_aprobados,
    ROUND(AVG(CASE WHEN i.estado = 'Aprobado' THEN i.nota_final END), 2) AS promedio,
    SUM(CASE WHEN i.estado = 'Aprobado' THEN c.creditos ELSE 0 END) AS creditos_aprobados
FROM Estudiantes e
INNER JOIN Inscripciones i ON e.id_estudiante = i.id_estudiante
INNER JOIN Cursos c ON i.id_curso = c.id_curso
WHERE i.nota_final IS NOT NULL
GROUP BY e.id_estudiante, e.codigo_estudiante, e.nombre, e.apellido, e.carrera
HAVING promedio >= 3.5
ORDER BY promedio DESC, creditos_aprobados DESC
LIMIT 5;

-- ============================================================================
-- FIN DE EJEMPLOS
-- ============================================================================

-- Para limpiar la base de datos de ejemplos:
-- DROP DATABASE IF EXISTS EjemplosRelaciones;
