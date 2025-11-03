# 📝 EJERCICIOS PRÁCTICOS - CLASE 4
## Consultas SQL Asistidas con IA

---

## 🎯 Instrucciones Generales

1. **Usa la IA como tu asistente**: Antes de escribir cada consulta, describe en lenguaje natural lo que necesitas.
2. **Ejecuta las consultas**: Prueba cada consulta en tu entorno SQL.
3. **Verifica los resultados**: Comprueba que obtienes los datos esperados.
4. **Optimiza**: Si la consulta funciona pero es lenta o compleja, pide ayuda a la IA para optimizarla.

---

## 📚 PARTE 1: TRADUCCIÓN DE LENGUAJE NATURAL A SQL

### Ejercicio 1.1: Consultas Básicas de Selección

Traduce las siguientes peticiones a consultas SQL:

**1.** "Muéstrame todos los empleados que trabajan en Madrid"

```sql
-- Tu respuesta aquí:


```

**2.** "Lista los productos que cuestan más de 100 euros"

```sql
-- Tu respuesta aquí:


```

**3.** "Necesito ver los 5 clientes más recientes ordenados por fecha"

```sql
-- Tu respuesta aquí:


```

**4.** "Quiero saber cuántos empleados hay en cada ciudad"

```sql
-- Tu respuesta aquí:


```

**5.** "Muéstrame todos los productos de la categoría 'Informática' que tengan menos de 50 unidades en stock"

```sql
-- Tu respuesta aquí:


```

---

### Ejercicio 1.2: Consultas con Relaciones

Traduce estas peticiones más complejas:

**6.** "Necesito ver el nombre de cada empleado junto con el nombre de su departamento y su salario, pero solo los que ganan más de 3500 euros"

```sql
-- Tu respuesta aquí:


```

**7.** "Muéstrame todas las ventas realizadas, incluyendo el nombre del cliente, el producto vendido y el nombre del vendedor"

```sql
-- Tu respuesta aquí:


```

**8.** "Quiero ver qué empleados no tienen jefe asignado"

```sql
-- Tu respuesta aquí:


```

**9.** "Lista todos los departamentos que tienen más de 1 empleado"

```sql
-- Tu respuesta aquí:


```

**10.** "Necesito saber qué productos se vendieron en octubre de 2024 y cuántas unidades de cada uno"

```sql
-- Tu respuesta aquí:


```

---

## 🔍 PARTE 2: DETECCIÓN Y CORRECCIÓN DE ERRORES

### Ejercicio 2.1: Encuentra y Corrige los Errores

Las siguientes consultas tienen errores. **Identifica el problema** y **escribe la versión corregida**.

**Error 1:**
```sql
-- ❌ Consulta con error:
SELECT nombre, apellido 
FROM empleados 
WHERE departamento = 'Ventas';
```

**Problema identificado:**
```
-- Escribe aquí cuál es el error:


```

**Consulta corregida:**
```sql
-- ✅ Tu corrección aquí:


```

---

**Error 2:**
```sql
-- ❌ Consulta con error:
SELECT e.nombre, d.nombre
FROM empleados e
JOIN departamentos d;
```

**Problema identificado:**
```
-- Escribe aquí cuál es el error:


```

**Consulta corregida:**
```sql
-- ✅ Tu corrección aquí:


```

---

**Error 3:**
```sql
-- ❌ Consulta con error:
SELECT COUNT(nombre) AS total
FROM empleados
WHERE salario > 4000
GROUP BY departamento;
```

**Problema identificado:**
```
-- Escribe aquí cuál es el error:


```

**Consulta corregida:**
```sql
-- ✅ Tu corrección aquí:


```

---

**Error 4:**
```sql
-- ❌ Consulta con error:
SELECT productos.nombre, SUM(ventas.total)
FROM productos, ventas
WHERE productos.id_producto = ventas.id_producto
ORDER BY total DESC;
```

**Problema identificado:**
```
-- Escribe aquí cuál es el error:


```

**Consulta corregida:**
```sql
-- ✅ Tu corrección aquí:


```

---

**Error 5:**
```sql
-- ❌ Consulta con error:
SELECT e.nombre, e.salario
FROM empleados e
WHERE e.salario > AVG(salario);
```

**Problema identificado:**
```
-- Escribe aquí cuál es el error:


```

**Consulta corregida:**
```sql
-- ✅ Tu corrección aquí:


```

---

## ⚡ PARTE 3: OPTIMIZACIÓN DE CONSULTAS

### Ejercicio 3.1: Mejora el Rendimiento

Para cada consulta, escribe una **versión optimizada** que sea más eficiente.

**Consulta 1: Demasiado genérica**
```sql
-- Original (ineficiente):
SELECT * 
FROM empleados 
WHERE id_departamento = 1;
```

**Tu versión optimizada:**
```sql
-- Optimizada:


-- Explica por qué es mejor:
```

---

**Consulta 2: JOIN implícito (antiguo estilo)**
```sql
-- Original (ineficiente):
SELECT e.nombre, d.nombre
FROM empleados e, departamentos d
WHERE e.id_departamento = d.id_departamento;
```

**Tu versión optimizada:**
```sql
-- Optimizada:


-- Explica por qué es mejor:
```

---

**Consulta 3: Subconsulta innecesaria**
```sql
-- Original (ineficiente):
SELECT nombre, salario
FROM empleados
WHERE id_departamento IN (
    SELECT id_departamento 
    FROM departamentos 
    WHERE ubicacion = 'Madrid'
);
```

**Tu versión optimizada:**
```sql
-- Optimizada:


-- Explica por qué es mejor:
```

---

**Consulta 4: Agregación sin índices**
```sql
-- Original (puede ser lenta con muchos datos):
SELECT fecha_venta, COUNT(*) as total_ventas
FROM ventas
GROUP BY fecha_venta;
```

**Tu versión optimizada:**
```sql
-- Optimizada (incluye creación de índice si es necesario):


-- Explica qué optimizaciones aplicaste:
```

---

## 🚀 PARTE 4: DESAFÍOS AVANZADOS

### Desafío 4.1: Análisis de Ventas

**Escribe una consulta que muestre:**
- El nombre del empleado
- El total de ventas que ha realizado
- El número de transacciones
- El promedio de venta por transacción
- Solo empleados con más de 2 ventas
- Ordenado por total de ventas descendente

```sql
-- Tu consulta aquí:




```

---

### Desafío 4.2: Reporte de Departamentos

**Crea una consulta que genere un reporte con:**
- Nombre del departamento
- Número de empleados
- Salario promedio del departamento
- Salario total del departamento
- Presupuesto del departamento
- Diferencia entre presupuesto y salario total
- Solo departamentos con al menos 1 empleado

```sql
-- Tu consulta aquí:




```

---

### Desafío 4.3: Productos Rentables

**Identifica los productos más rentables mostrando:**
- Nombre del producto
- Categoría
- Precio unitario
- Total de unidades vendidas
- Ingresos totales generados
- Ordenado por ingresos descendente
- Solo los top 5

```sql
-- Tu consulta aquí:




```

---

### Desafío 4.4: Empleados Estrella

**Encuentra los mejores vendedores usando:**
- CTE (Common Table Expression) para calcular totales por empleado
- RANK() o ROW_NUMBER() para clasificarlos
- Incluye: nombre, apellido, departamento, total vendido, ranking
- Muestra solo el top 3

```sql
-- Tu consulta aquí (usa WITH para el CTE):




```

---

### Desafío 4.5: Análisis Temporal

**Crea un análisis de ventas por mes mostrando:**
- Mes (formato YYYY-MM)
- Total de ventas del mes
- Número de transacciones
- Ticket promedio
- Comparación con el mes anterior (usa funciones de ventana como LAG)

```sql
-- Tu consulta aquí:




```

---

## 🎓 PARTE 5: PROYECTO INTEGRADOR

### Ejercicio Final: Dashboard de Gestión

**Crea 3 consultas para un dashboard ejecutivo:**

#### Consulta 1: KPIs Generales
```sql
-- Muestra en una sola consulta:
-- - Total de empleados
-- - Total de clientes
-- - Total de productos
-- - Total de ventas realizadas
-- - Ingresos totales
-- Pista: Usa subconsultas en el SELECT




```

#### Consulta 2: Top Performers
```sql
-- Lista los mejores en cada categoría:
-- - Top 3 empleados por ventas
-- - Top 3 productos más vendidos
-- - Top 3 clientes que más compran
-- Pista: Usa UNION ALL o múltiples CTEs




```

#### Consulta 3: Alertas y Recomendaciones
```sql
-- Identifica situaciones que requieren atención:
-- - Productos con stock bajo (menos de 50 unidades)
-- - Departamentos con presupuesto insuficiente (salarios > 80% del presupuesto)
-- - Empleados sin ventas en el último mes
-- Pista: Usa UNION ALL para combinar diferentes alertas




```

---

## 💡 CONSEJOS PARA USAR LA IA

### ✅ Buenas Prácticas

1. **Sé específico**: "Muéstrame empleados con salario > 4000 del departamento de Ventas"
2. **Menciona las tablas**: "Necesito unir las tablas empleados y departamentos"
3. **Indica el formato**: "Ordena por salario descendente"
4. **Pide explicación**: "Explica qué hace cada parte de esta consulta"
5. **Solicita alternativas**: "¿Hay una forma más eficiente de hacer esto?"

### ❌ Evita

1. Ser vago: "Dame datos de empleados" (¿qué datos?, ¿todos?, ¿con qué condiciones?)
2. No revisar el resultado: Siempre verifica que la consulta hace lo que esperabas
3. Copiar sin entender: Asegúrate de comprender cada parte de la consulta
4. Ignorar el contexto: Menciona la estructura de tus tablas si es relevante

---

---

## 📚 RECURSOS DE APOYO

- **Archivo SQL base**: `ejemplos_sql.sql`
- **Documentación**: `README.md`
- **IA recomendada**: ChatGPT, Claude, GitHub Copilot
- **Herramientas**: MySQL Workbench, DBeaver, phpMyAdmin

---

## 🏆 BONUS: Retos Extra

### Reto 1: Función Personalizada
Crea una función o procedimiento almacenado para calcular el total de ventas de un empleado.

### Reto 2: Vista Materializada
Crea una vista que muestre información consolidada de ventas por departamento.

### Reto 3: Trigger
Crea un trigger que actualice automáticamente el stock cuando se registre una venta.

---

**¡Éxito en tus ejercicios! 🚀**

*Recuerda: La IA es tu asistente, pero tú eres quien aprende y toma las decisiones.*
