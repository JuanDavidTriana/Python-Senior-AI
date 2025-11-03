-- ============================================
-- CLASE 4: Simulación de operación real
-- Consultas SQL asistidas
-- ============================================

-- ============================================
-- CREACIÓN DE BASE DE DATOS Y TABLAS
-- ============================================

-- Crear base de datos
CREATE DATABASE IF NOT EXISTS empresa_db;
USE empresa_db;

-- Tabla: Departamentos
CREATE TABLE departamentos (
    id_departamento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    presupuesto DECIMAL(10, 2),
    ubicacion VARCHAR(100)
);

-- Tabla: Empleados
CREATE TABLE empleados (
    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(20),
    fecha_contratacion DATE,
    salario DECIMAL(10, 2),
    id_departamento INT,
    id_jefe INT,
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento),
    FOREIGN KEY (id_jefe) REFERENCES empleados(id_empleado)
);

-- Tabla: Clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    empresa VARCHAR(100),
    ciudad VARCHAR(50),
    pais VARCHAR(50),
    email VARCHAR(100),
    telefono VARCHAR(20)
);

-- Tabla: Productos
CREATE TABLE productos (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2),
    stock INT,
    categoria VARCHAR(50)
);

-- Tabla: Ventas
CREATE TABLE ventas (
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    id_empleado INT,
    id_producto INT,
    cantidad INT,
    fecha_venta DATE,
    total DECIMAL(10, 2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- ============================================
-- INSERCIÓN DE DATOS DE EJEMPLO
-- ============================================

-- Insertar departamentos
INSERT INTO departamentos (nombre, presupuesto, ubicacion) VALUES
('Ventas', 150000.00, 'Madrid'),
('Marketing', 100000.00, 'Barcelona'),
('Tecnología', 200000.00, 'Madrid'),
('Recursos Humanos', 80000.00, 'Valencia'),
('Finanzas', 120000.00, 'Madrid');

-- Insertar empleados
INSERT INTO empleados (nombre, apellido, email, telefono, fecha_contratacion, salario, id_departamento, id_jefe) VALUES
('Carlos', 'García', 'carlos.garcia@empresa.com', '600111222', '2020-01-15', 4500.00, 1, NULL),
('Ana', 'Martínez', 'ana.martinez@empresa.com', '600222333', '2020-03-20', 3800.00, 2, NULL),
('Luis', 'Rodríguez', 'luis.rodriguez@empresa.com', '600333444', '2019-06-10', 5200.00, 3, NULL),
('María', 'López', 'maria.lopez@empresa.com', '600444555', '2021-02-14', 3500.00, 1, 1),
('Pedro', 'Sánchez', 'pedro.sanchez@empresa.com', '600555666', '2021-05-08', 3200.00, 2, 2),
('Laura', 'Fernández', 'laura.fernandez@empresa.com', '600666777', '2020-09-12', 4800.00, 3, 3),
('Javier', 'González', 'javier.gonzalez@empresa.com', '600777888', '2022-01-20', 2900.00, 4, NULL),
('Carmen', 'Ruiz', 'carmen.ruiz@empresa.com', '600888999', '2021-11-05', 4200.00, 5, NULL);

-- Insertar clientes
INSERT INTO clientes (nombre, empresa, ciudad, pais, email, telefono) VALUES
('Tech Solutions SA', 'Tech Solutions', 'Madrid', 'España', 'contacto@techsolutions.es', '911234567'),
('Innovate Corp', 'Innovate', 'Barcelona', 'España', 'info@innovate.es', '932345678'),
('Global Traders', 'Global Traders', 'Valencia', 'España', 'ventas@globaltraders.es', '963456789'),
('Digital Services', 'Digital', 'Sevilla', 'España', 'hello@digital.es', '954567890'),
('Cloud Systems', 'Cloud Systems', 'Bilbao', 'España', 'support@cloudsystems.es', '944678901');

-- Insertar productos
INSERT INTO productos (nombre, descripcion, precio, stock, categoria) VALUES
('Laptop Pro 15', 'Portátil profesional de 15 pulgadas', 1200.00, 50, 'Informática'),
('Mouse Inalámbrico', 'Mouse ergonómico sin cables', 25.00, 200, 'Accesorios'),
('Teclado Mecánico', 'Teclado gaming RGB', 80.00, 100, 'Accesorios'),
('Monitor 27 4K', 'Monitor profesional 4K', 450.00, 30, 'Informática'),
('Webcam HD', 'Cámara web Full HD', 65.00, 150, 'Accesorios'),
('Auriculares Bluetooth', 'Auriculares inalámbricos', 95.00, 80, 'Audio'),
('Disco SSD 1TB', 'Unidad de estado sólido', 120.00, 120, 'Almacenamiento'),
('Router WiFi 6', 'Router de alta velocidad', 150.00, 60, 'Redes');

-- Insertar ventas
INSERT INTO ventas (id_cliente, id_empleado, id_producto, cantidad, fecha_venta, total) VALUES
(1, 1, 1, 5, '2024-10-01', 6000.00),
(2, 1, 4, 3, '2024-10-05', 1350.00),
(3, 4, 2, 10, '2024-10-08', 250.00),
(1, 4, 7, 8, '2024-10-12', 960.00),
(4, 1, 3, 5, '2024-10-15', 400.00),
(5, 4, 6, 4, '2024-10-18', 380.00),
(2, 1, 8, 2, '2024-10-20', 300.00),
(3, 4, 5, 6, '2024-10-22', 390.00),
(1, 1, 1, 2, '2024-10-25', 2400.00),
(4, 4, 4, 1, '2024-10-28', 450.00);

-- ============================================
-- EJERCICIO 1: CONSULTAS BÁSICAS
-- ============================================

-- 1.1 Mostrar todos los empleados
SELECT * FROM empleados;

-- 1.2 Empleados con salario mayor a 4000€
SELECT nombre, apellido, salario 
FROM empleados 
WHERE salario > 4000;

-- 1.3 Empleados ordenados por salario descendente
SELECT nombre, apellido, salario 
FROM empleados 
ORDER BY salario DESC;

-- 1.4 Empleados contratados después de 2020
SELECT nombre, apellido, fecha_contratacion 
FROM empleados 
WHERE fecha_contratacion > '2020-12-31';

-- 1.5 Empleados cuyos nombres empiezan con 'L'
SELECT nombre, apellido 
FROM empleados 
WHERE nombre LIKE 'L%';

-- ============================================
-- EJERCICIO 2: CONSULTAS CON JOIN
-- ============================================

-- 2.1 Empleados con su departamento
SELECT e.nombre, e.apellido, d.nombre AS departamento
FROM empleados e
INNER JOIN departamentos d ON e.id_departamento = d.id_departamento;

-- 2.2 Empleados con su jefe
SELECT e.nombre AS empleado, e.apellido, j.nombre AS jefe
FROM empleados e
LEFT JOIN empleados j ON e.id_jefe = j.id_empleado;

-- 2.3 Ventas con información completa
SELECT v.id_venta, c.nombre AS cliente, e.nombre AS vendedor, 
       p.nombre AS producto, v.cantidad, v.total, v.fecha_venta
FROM ventas v
INNER JOIN clientes c ON v.id_cliente = c.id_cliente
INNER JOIN empleados e ON v.id_empleado = e.id_empleado
INNER JOIN productos p ON v.id_producto = p.id_producto;

-- 2.4 Departamentos con su número de empleados
SELECT d.nombre AS departamento, COUNT(e.id_empleado) AS num_empleados
FROM departamentos d
LEFT JOIN empleados e ON d.id_departamento = e.id_departamento
GROUP BY d.id_departamento, d.nombre;

-- ============================================
-- EJERCICIO 3: CONSULTAS DE AGREGACIÓN
-- ============================================

-- 3.1 Total de empleados por departamento
SELECT d.nombre AS departamento, COUNT(e.id_empleado) AS total_empleados
FROM departamentos d
LEFT JOIN empleados e ON d.id_departamento = e.id_departamento
GROUP BY d.id_departamento, d.nombre;

-- 3.2 Salario promedio por departamento
SELECT d.nombre AS departamento, AVG(e.salario) AS salario_promedio
FROM departamentos d
INNER JOIN empleados e ON d.id_departamento = e.id_departamento
GROUP BY d.id_departamento, d.nombre;

-- 3.3 Total de ventas por producto
SELECT p.nombre AS producto, SUM(v.total) AS total_vendido
FROM productos p
INNER JOIN ventas v ON p.id_producto = v.id_producto
GROUP BY p.id_producto, p.nombre
ORDER BY total_vendido DESC;

-- 3.4 Ventas totales por mes
SELECT DATE_FORMAT(fecha_venta, '%Y-%m') AS mes, 
       SUM(total) AS total_mes
FROM ventas
GROUP BY DATE_FORMAT(fecha_venta, '%Y-%m')
ORDER BY mes;

-- 3.5 Cliente con más compras
SELECT c.nombre, COUNT(v.id_venta) AS num_compras, SUM(v.total) AS total_gastado
FROM clientes c
INNER JOIN ventas v ON c.id_cliente = v.id_cliente
GROUP BY c.id_cliente, c.nombre
ORDER BY total_gastado DESC
LIMIT 1;

-- ============================================
-- EJERCICIO 4: SUBCONSULTAS Y CTEs
-- ============================================

-- 4.1 Empleados que ganan más que el promedio
SELECT nombre, apellido, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);

-- 4.2 Departamento con mayor presupuesto
SELECT nombre, presupuesto
FROM departamentos
WHERE presupuesto = (SELECT MAX(presupuesto) FROM departamentos);

-- 4.3 Productos que nunca se han vendido
SELECT nombre
FROM productos
WHERE id_producto NOT IN (SELECT DISTINCT id_producto FROM ventas);

-- 4.4 CTE: Ventas por empleado
WITH ventas_empleado AS (
    SELECT e.nombre, e.apellido, SUM(v.total) AS total_ventas
    FROM empleados e
    INNER JOIN ventas v ON e.id_empleado = v.id_empleado
    GROUP BY e.id_empleado, e.nombre, e.apellido
)
SELECT * FROM ventas_empleado
ORDER BY total_ventas DESC;

-- 4.5 CTE: Ranking de productos más vendidos
WITH ranking_productos AS (
    SELECT p.nombre, SUM(v.cantidad) AS cantidad_vendida,
           RANK() OVER (ORDER BY SUM(v.cantidad) DESC) AS ranking
    FROM productos p
    INNER JOIN ventas v ON p.id_producto = v.id_producto
    GROUP BY p.id_producto, p.nombre
)
SELECT * FROM ranking_productos
WHERE ranking <= 3;

-- ============================================
-- EJERCICIO 5: CONSULTAS MAL ESCRITAS (PARA CORREGIR)
-- ============================================

-- ERROR 1: SELECT * innecesario
-- ❌ MAL:
SELECT * FROM empleados WHERE id_departamento = 1;
-- ✅ BIEN:
SELECT nombre, apellido, salario FROM empleados WHERE id_departamento = 1;

-- ERROR 2: JOIN sin índices y filtrado tardío
-- ❌ MAL:
SELECT e.nombre, d.nombre
FROM empleados e, departamentos d
WHERE e.id_departamento = d.id_departamento AND e.salario > 4000;
-- ✅ BIEN:
SELECT e.nombre, d.nombre
FROM empleados e
INNER JOIN departamentos d ON e.id_departamento = d.id_departamento
WHERE e.salario > 4000;

-- ERROR 3: Subconsulta innecesaria
-- ❌ MAL:
SELECT nombre FROM empleados WHERE id_departamento IN 
(SELECT id_departamento FROM departamentos WHERE nombre = 'Ventas');
-- ✅ BIEN:
SELECT e.nombre FROM empleados e
INNER JOIN departamentos d ON e.id_departamento = d.id_departamento
WHERE d.nombre = 'Ventas';

-- ERROR 4: COUNT(*) sin necesidad
-- ❌ MAL:
SELECT COUNT(*) FROM empleados WHERE id_departamento = 1;
-- ✅ BIEN (si hay índice en id_departamento):
SELECT COUNT(id_empleado) FROM empleados WHERE id_departamento = 1;

-- ============================================
-- CONSULTAS DE OPTIMIZACIÓN Y RENDIMIENTO
-- ============================================

-- Crear índices para mejorar rendimiento
CREATE INDEX idx_empleados_departamento ON empleados(id_departamento);
CREATE INDEX idx_empleados_salario ON empleados(salario);
CREATE INDEX idx_ventas_fecha ON ventas(fecha_venta);
CREATE INDEX idx_ventas_cliente ON ventas(id_cliente);

-- Ejemplo de EXPLAIN para analizar consultas
EXPLAIN SELECT e.nombre, d.nombre
FROM empleados e
INNER JOIN departamentos d ON e.id_departamento = d.id_departamento
WHERE e.salario > 4000;

-- ============================================
-- CONSULTAS AVANZADAS PARA PRÁCTICA
-- ============================================

-- 1. Top 3 empleados con mejores ventas en octubre 2024
SELECT e.nombre, e.apellido, SUM(v.total) AS total_ventas
FROM empleados e
INNER JOIN ventas v ON e.id_empleado = v.id_empleado
WHERE v.fecha_venta BETWEEN '2024-10-01' AND '2024-10-31'
GROUP BY e.id_empleado, e.nombre, e.apellido
ORDER BY total_ventas DESC
LIMIT 3;

-- 2. Productos con stock bajo (menos de 100 unidades)
SELECT nombre, stock, categoria
FROM productos
WHERE stock < 100
ORDER BY stock ASC;

-- 3. Ingresos totales por categoría de producto
SELECT p.categoria, SUM(v.total) AS ingresos_totales
FROM productos p
INNER JOIN ventas v ON p.id_producto = v.id_producto
GROUP BY p.categoria
ORDER BY ingresos_totales DESC;

-- 4. Empleados sin ventas registradas
SELECT e.nombre, e.apellido, d.nombre AS departamento
FROM empleados e
LEFT JOIN ventas v ON e.id_empleado = v.id_empleado
INNER JOIN departamentos d ON e.id_departamento = d.id_departamento
WHERE v.id_venta IS NULL;

-- 5. Análisis de ventas: promedio, máximo y mínimo
SELECT 
    AVG(total) AS venta_promedio,
    MAX(total) AS venta_maxima,
    MIN(total) AS venta_minima,
    SUM(total) AS total_general
FROM ventas;

-- ============================================
-- FIN DEL SCRIPT
-- ============================================
