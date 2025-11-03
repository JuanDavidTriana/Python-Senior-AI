# Clase 3 - CRUD SQL: Consultas reales para la gestión de datos

## 📋 Objetivos de aprendizaje

- Ejecutar operaciones básicas: **insertar**, **consultar**, **actualizar** y **eliminar**
- Comprender y aplicar **filtros**, **ordenamientos** y **consultas seguras**
- Implementar buenas prácticas en la escritura de SQL con apoyo de IA

## 📚 Contenidos

### 1. Operaciones CRUD básicas

#### INSERT - Insertar datos
Permite agregar nuevos registros a una tabla.

```sql
-- Sintaxis básica
INSERT INTO tabla (columna1, columna2, columna3)
VALUES (valor1, valor2, valor3);

-- Insertar múltiples registros
INSERT INTO tabla (columna1, columna2)
VALUES 
    (valor1a, valor2a),
    (valor1b, valor2b),
    (valor1c, valor2c);
```

#### SELECT - Consultar datos
Recupera información de una o más tablas.

```sql
-- Seleccionar todas las columnas
SELECT * FROM tabla;

-- Seleccionar columnas específicas
SELECT columna1, columna2 FROM tabla;

-- Consultas con alias
SELECT columna1 AS nombre_nuevo FROM tabla;
```

#### UPDATE - Actualizar datos
Modifica registros existentes en una tabla.

```sql
-- Sintaxis básica
UPDATE tabla
SET columna1 = nuevo_valor
WHERE condicion;

-- Actualizar múltiples columnas
UPDATE tabla
SET columna1 = valor1, columna2 = valor2
WHERE condicion;
```

#### DELETE - Eliminar datos
Elimina registros de una tabla.

```sql
-- Eliminar registros específicos
DELETE FROM tabla
WHERE condicion;

-- ⚠️ CUIDADO: Esto elimina TODOS los registros
DELETE FROM tabla;
```

### 2. Filtros con WHERE

Los filtros permiten seleccionar registros que cumplan ciertas condiciones.

#### Operadores relacionales
- `=` : Igual
- `!=` o `<>` : Diferente
- `>` : Mayor que
- `<` : Menor que
- `>=` : Mayor o igual
- `<=` : Menor o igual

#### Operadores lógicos
- `AND` : Todas las condiciones deben cumplirse
- `OR` : Al menos una condición debe cumplirse
- `NOT` : Niega una condición

#### Otros operadores útiles
- `BETWEEN` : Rango de valores
- `IN` : Lista de valores
- `LIKE` : Búsqueda de patrones
- `IS NULL` / `IS NOT NULL` : Valores nulos

```sql
-- Ejemplos de filtros
SELECT * FROM estudiantes WHERE edad >= 18;
SELECT * FROM estudiantes WHERE edad BETWEEN 18 AND 25;
SELECT * FROM estudiantes WHERE nombre LIKE 'A%';
SELECT * FROM estudiantes WHERE ciudad IN ('Madrid', 'Barcelona', 'Valencia');
SELECT * FROM estudiantes WHERE email IS NOT NULL;
```

### 3. Ordenamiento y límites

#### ORDER BY - Ordenar resultados
```sql
-- Orden ascendente (por defecto)
SELECT * FROM estudiantes ORDER BY nombre;
SELECT * FROM estudiantes ORDER BY nombre ASC;

-- Orden descendente
SELECT * FROM estudiantes ORDER BY edad DESC;

-- Ordenar por múltiples columnas
SELECT * FROM estudiantes ORDER BY ciudad ASC, nombre ASC;
```

#### LIMIT - Limitar resultados
```sql
-- Obtener los primeros 10 registros
SELECT * FROM estudiantes LIMIT 10;

-- Paginación: saltar registros y limitar
SELECT * FROM estudiantes LIMIT 10 OFFSET 20; -- Registros 21-30
```

### 4. Buenas prácticas de escritura SQL con IA

#### ✅ Detección de consultas ineficientes

**Problemas comunes:**
1. **SELECT * en tablas grandes**: Especifica solo las columnas necesarias
2. **Falta de índices**: Consultas lentas en columnas sin índice
3. **WHERE sin índices**: Filtros en columnas no indexadas
4. **Subconsultas no optimizadas**: Usar JOINs cuando sea posible

**Ejemplo de optimización:**
```sql
-- ❌ Ineficiente
SELECT * FROM estudiantes WHERE UPPER(nombre) = 'JUAN';

-- ✅ Eficiente
SELECT id, nombre, email FROM estudiantes WHERE nombre = 'Juan';
```

#### 🔑 Sugerencias de índices o claves

```sql
-- Crear índices en columnas frecuentemente consultadas
CREATE INDEX idx_estudiante_email ON estudiantes(email);
CREATE INDEX idx_libro_isbn ON libros(isbn);

-- Índices compuestos para consultas múltiples
CREATE INDEX idx_estudiante_ciudad_edad ON estudiantes(ciudad, edad);
```

#### 🛡️ Consultas seguras

**Prevención de SQL Injection:**
```python
# ❌ NUNCA hagas esto
query = f"SELECT * FROM usuarios WHERE email = '{email}'"

# ✅ Usa parámetros preparados
query = "SELECT * FROM usuarios WHERE email = %s"
cursor.execute(query, (email,))
```

**Otras buenas prácticas:**
- Usa transacciones para operaciones múltiples
- Implementa manejo de errores
- Valida datos antes de insertar
- Usa constraints (UNIQUE, NOT NULL, FOREIGN KEY)
- Documenta consultas complejas


## 📖 Recursos adicionales

- [Documentación oficial de PostgreSQL](https://www.postgresql.org/docs/)
- [MySQL Reference Manual](https://dev.mysql.com/doc/)

## 💡 Consejos

- Siempre haz **backup** antes de ejecutar DELETE o UPDATE masivos
- Usa **transacciones** para operaciones críticas
- Prueba consultas en un entorno de desarrollo primero
- Documenta tus consultas complejas
- Utiliza IA para revisar y optimizar tu SQL

---

**¡Buena suerte con tu práctica de SQL! 🎯**
