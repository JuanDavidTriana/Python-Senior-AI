# Clase 2 - Modelado Lógico y Físico de Bases de Datos

## 📋 Objetivos

1. **Traducir requisitos funcionales a un modelo relacional correcto**
   - Identificar entidades y sus atributos
   - Determinar las relaciones entre entidades
   - Aplicar normalización para evitar redundancia

2. **Crear los scripts de base de datos y depurar errores comunes**
   - Construcción de tablas con sintaxis correcta
   - Implementación de restricciones y validaciones
   - Identificación y corrección de errores típicos

## 🎯 Actividades

- Construcción guiada de tablas con `CREATE TABLE`
- Asistencia con IA para sugerencias de relaciones, claves e índices
- Revisión cruzada: validar que el modelo resuelve realmente el problema planteado

---

## 🔗 Tipos de Relaciones entre Tablas

### 1. Relación Uno a Uno (1:1)

**Definición:** Cada registro de la tabla A se relaciona con exactamente un registro de la tabla B, y viceversa.

**Ejemplo conceptual:**
- Una **Persona** tiene exactamente un **Pasaporte**
- Un **Pasaporte** pertenece a exactamente una **Persona**

**Características:**
- Se implementa con una clave foránea (FK) con restricción `UNIQUE`
- La FK puede estar en cualquiera de las dos tablas
- Útil para separar información sensible o poco frecuente

**Diagrama:**
```
Persona (1) ←→ (1) Pasaporte
```

**Cuándo usar:**
- Separar datos sensibles (ej: datos médicos, financieros)
- Optimizar consultas cuando algunos datos se consultan raramente
- Extender una tabla existente sin modificarla

---

### 2. Relación Uno a Muchos (1:N)

**Definición:** Un registro de la tabla A puede relacionarse con múltiples registros de la tabla B, pero cada registro de B se relaciona con solo uno de A.

**Ejemplo conceptual:**
- Un **Cliente** puede tener muchos **Pedidos**
- Un **Pedido** pertenece a un solo **Cliente**

**Características:**
- La FK se coloca en el lado "muchos" (tabla hija)
- Es la relación más común en bases de datos
- No requiere restricción `UNIQUE` en la FK

**Diagrama:**
```
Cliente (1) ←→ (N) Pedidos
```

**Cuándo usar:**
- Relaciones jerárquicas (departamento → empleados)
- Propiedad o pertenencia (autor → libros)
- Agrupación (categoría → productos)

---

### 3. Relación Muchos a Muchos (N:M)

**Definición:** Múltiples registros de la tabla A pueden relacionarse con múltiples registros de la tabla B.

**Ejemplo conceptual:**
- Un **Estudiante** puede inscribirse en muchos **Cursos**
- Un **Curso** puede tener muchos **Estudiantes**

**Características:**
- Se implementa mediante una **tabla intermedia** (tabla puente)
- La tabla intermedia contiene las FK de ambas tablas
- La clave primaria compuesta suele ser la combinación de ambas FK
- Puede contener atributos adicionales de la relación

**Diagrama:**
```
Estudiante (N) ←→ Inscripciones ←→ (M) Curso
```

**Cuándo usar:**
- Relaciones de asignación (empleados ↔ proyectos)
- Etiquetado (artículos ↔ etiquetas)
- Permisos (usuarios ↔ roles)

---

## 🔑 Conceptos Clave

### Clave Primaria (Primary Key - PK)
- Identifica únicamente cada registro en una tabla
- No puede ser NULL
- No puede repetirse
- Puede ser simple (un campo) o compuesta (varios campos)

**Ejemplo:** `id_cliente`, `numero_factura`

### Clave Foránea (Foreign Key - FK)
- Campo que referencia la PK de otra tabla
- Establece y mantiene la integridad referencial
- Puede ser NULL (dependiendo de la lógica de negocio)
- Puede repetirse (en relaciones 1:N)

**Ejemplo:** `id_cliente` en la tabla `Pedidos` que referencia `id_cliente` en la tabla `Clientes`

### Índices
- Estructuras que mejoran la velocidad de las consultas
- Se crean automáticamente en PK y FK (en algunos DBMS)
- Pueden crearse manualmente en campos frecuentemente consultados

**Tipos:**
- **Único (UNIQUE):** No permite valores duplicados
- **No único:** Permite duplicados
- **Compuesto:** Sobre múltiples columnas

---

## ⚠️ Errores Comunes y Soluciones

### 1. Violación de Integridad Referencial
**Error:** Intentar insertar una FK que no existe en la tabla referenciada.

**Solución:**
- Insertar primero los registros en la tabla padre
- Verificar que el valor FK existe antes de insertarlo

### 2. Tipo de Dato Incompatible
**Error:** La FK y la PK tienen tipos de datos diferentes.

**Solución:**
- Asegurar que ambos campos tienen el mismo tipo y tamaño
- Ejemplo: Si PK es `INT`, FK debe ser `INT` también

### 3. Eliminar Registro Padre con Hijos
**Error:** Intentar eliminar un registro que tiene dependencias.

**Solución:**
- Usar `ON DELETE CASCADE` para eliminar en cascada
- Usar `ON DELETE SET NULL` para anular referencias
- Eliminar primero los registros hijos

### 4. Ausencia de PK
**Error:** Crear tabla sin clave primaria.

**Solución:**
- Siempre definir una PK (preferiblemente auto-incremental)
- Usar claves compuestas cuando sea necesario

### 5. Normalización Insuficiente
**Error:** Redundancia de datos y anomalías de actualización.

**Solución:**
- Aplicar formas normales (1FN, 2FN, 3FN)
- Separar información en tablas relacionadas

---

## 📊 Ejemplos Prácticos

### Sistema de E-commerce Simplificado

**Entidades identificadas:**
1. **Clientes:** Personas que compran
2. **Productos:** Artículos en venta
3. **Categorías:** Clasificación de productos
4. **Pedidos:** Órdenes de compra
5. **Detalles de Pedido:** Productos específicos en cada pedido

**Relaciones:**
- Cliente → Pedido: **1:N** (un cliente puede hacer muchos pedidos)
- Categoría → Producto: **1:N** (una categoría contiene muchos productos)
- Pedido → Detalle_Pedido: **1:N** (un pedido tiene muchos detalles)
- Producto → Detalle_Pedido: **1:N** (un producto puede estar en muchos detalles)
- Pedido ↔ Producto: **N:M** (a través de Detalle_Pedido)

---

## 🎓 Sistema de Gestión Académica

**Entidades identificadas:**
1. **Estudiantes:** Personas que estudian
2. **Cursos:** Materias disponibles
3. **Profesores:** Docentes
4. **Inscripciones:** Registro de estudiantes en cursos
5. **Perfiles:** Información adicional de estudiantes

**Relaciones:**
- Estudiante → Perfil: **1:1** (cada estudiante tiene un perfil único)
- Profesor → Curso: **1:N** (un profesor imparte varios cursos)
- Estudiante ↔ Curso: **N:M** (a través de Inscripciones)

---

## 🛠️ Mejores Prácticas

1. **Nomenclatura consistente:**
   - Usar snake_case o camelCase de forma consistente
   - Nombres descriptivos (evitar abreviaturas confusas)
   - Prefijos claros para FK: `id_cliente`, `cliente_id`

2. **Diseño escalable:**
   - Pensar en el crecimiento futuro
   - Evitar columnas "por si acaso"
   - Usar tipos de datos apropiados

3. **Documentación:**
   - Comentar tablas y columnas complejas
   - Mantener diagramas ER actualizados
   - Documentar reglas de negocio

4. **Integridad de datos:**
   - Usar constraints (CHECK, NOT NULL, UNIQUE)
   - Definir valores DEFAULT cuando corresponda
   - Implementar triggers para validaciones complejas

5. **Performance:**
   - Crear índices en columnas de búsqueda frecuente
   - No sobre-indexar (impacta en INSERT/UPDATE)
   - Considerar particionamiento para tablas grandes

---

## 📚 Recursos Adicionales

- [Ver ejemplos SQL prácticos](./ejemplos_relaciones.sql)
- Herramientas de diseño: [dbdiagram.io](https://dbdiagram.io/), [draw.io](https://draw.io)

---

## 🚀 Siguiente Paso

Revisa el archivo `ejemplos_relaciones.sql` para ver la implementación práctica de todos estos conceptos con ejemplos ejecutables.

---
