# 🎯 Ejercicios Prácticos - CRUD SQL

## Instrucciones Generales

- Crea un archivo llamado `ejercicio.sql` para escribir tus soluciones
- Ejecuta cada consulta y verifica que funcione correctamente
- Comenta tu código para explicar qué hace cada consulta
- Guarda capturas de pantalla de los resultados si es necesario

---

## 📝 Parte 1: Creación de Base de Datos (20 puntos)

### Ejercicio 1.1: Crear las tablas
Crea las siguientes tablas con sus restricciones:

**Tabla: estudiantes**
- `id`: Entero, clave primaria, autoincremental
- `nombre`: Texto (máximo 100 caracteres), obligatorio
- `apellido`: Texto (máximo 100 caracteres), obligatorio
- `email`: Texto (máximo 150 caracteres), obligatorio y único
- `edad`: Entero, debe estar entre 16 y 100
- `ciudad`: Texto (máximo 100 caracteres)
- `carrera`: Texto (máximo 150 caracteres)
- `semestre`: Entero, debe estar entre 1 y 10
- `promedio`: Decimal (precisión 3,2), debe estar entre 0.00 y 5.00
- `fecha_registro`: Fecha, por defecto la fecha actual
- `activo`: Booleano, por defecto TRUE

**Tabla: libros**
- `id`: Entero, clave primaria, autoincremental
- `titulo`: Texto (máximo 200 caracteres), obligatorio
- `autor`: Texto (máximo 150 caracteres), obligatorio
- `isbn`: Texto (máximo 20 caracteres), obligatorio y único
- `editorial`: Texto (máximo 100 caracteres)
- `año_publicacion`: Entero, debe estar entre 1000 y 2100
- `categoria`: Texto (máximo 50 caracteres)
- `numero_paginas`: Entero
- `precio`: Decimal (precisión 10,2)
- `disponible`: Booleano, por defecto TRUE
- `fecha_adquisicion`: Fecha

---

## ➕ Parte 2: Operaciones INSERT (15 puntos)

### Ejercicio 2.1: Insertar estudiantes
Inserta al menos **8 estudiantes** con datos variados. Asegúrate de incluir:
- Estudiantes de diferentes ciudades (al menos 4 ciudades distintas)
- Diferentes carreras (al menos 3 carreras)
- Rangos de edad entre 18 y 30 años
- Diferentes semestres (1 al 10)
- Promedios variados (3.0 a 5.0)

### Ejercicio 2.2: Insertar libros
Inserta al menos **10 libros** con datos variados. Incluye:
- Diferentes categorías: Ficción, No Ficción, Ciencia, Historia, Tecnología, Literatura
- Años de publicación variados (1950 - 2024)
- Al menos 3 libros NO disponibles
- Precios entre 15.00 y 150.00

### Ejercicio 2.3: Inserción múltiple
Inserta 3 estudiantes más usando una sola sentencia INSERT con múltiples valores.

---

## 🔍 Parte 3: Operaciones SELECT (25 puntos)

### Ejercicio 3.1: Consultas básicas
1. Selecciona todos los estudiantes
2. Selecciona solo el nombre, email y carrera de todos los estudiantes
3. Cuenta cuántos estudiantes hay en total
4. Cuenta cuántos libros hay disponibles

### Ejercicio 3.2: Filtros simples
1. Estudiantes mayores de 22 años
2. Libros publicados después del año 2000
3. Estudiantes de la ciudad "Madrid"
4. Libros con precio menor a 50.00
5. Estudiantes con promedio mayor o igual a 4.0

### Ejercicio 3.3: Filtros con operadores lógicos
1. Estudiantes de "Barcelona" O "Valencia" con edad mayor a 20
2. Libros de categoría "Ficción" Y disponibles
3. Estudiantes con promedio entre 3.5 y 4.5
4. Libros publicados entre 1980 y 2010

### Ejercicio 3.4: Búsquedas con LIKE
1. Estudiantes cuyo nombre empiece con "A"
2. Libros cuyo título contenga la palabra "historia" o "Historia"
3. Estudiantes con email del dominio "@gmail.com"
4. Autores cuyo apellido termine en "ez"

### Ejercicio 3.5: Consultas con IN
1. Estudiantes que cursan 1, 3 o 5 semestre
2. Libros de las categorías: "Ficción", "Ciencia", "Tecnología"
3. Estudiantes de las ciudades: "Madrid", "Barcelona", "Sevilla"

### Ejercicio 3.6: Valores NULL
1. Estudiantes que no tienen carrera asignada (NULL)
2. Libros que no tienen editorial asignada
3. Estudiantes que SÍ tienen ciudad asignada

---

## 📊 Parte 4: Ordenamiento y Límites (15 puntos)

### Ejercicio 4.1: Ordenamiento simple
1. Estudiantes ordenados alfabéticamente por nombre
2. Libros ordenados por precio de mayor a menor
3. Estudiantes ordenados por edad de menor a mayor
4. Libros ordenados por año de publicación (más recientes primero)

### Ejercicio 4.2: Ordenamiento múltiple
1. Estudiantes ordenados por ciudad (ascendente) y luego por promedio (descendente)
2. Libros ordenados por categoría (ascendente) y luego por título (ascendente)
3. Estudiantes ordenados por semestre (ascendente) y luego por nombre (ascendente)

### Ejercicio 4.3: Límites
1. Los 5 estudiantes con mejor promedio
2. Los 3 libros más caros
3. Los 5 libros más antiguos
4. Los primeros 4 estudiantes más jóvenes

### Ejercicio 4.4: Paginación
1. Muestra los estudiantes de 5 en 5 (primera página)
2. Muestra los estudiantes de 5 en 5 (segunda página)
3. Muestra los libros de 3 en 3 (tercera página)

---

## ✏️ Parte 5: Operaciones UPDATE (15 puntos)

### Ejercicio 5.1: Actualizaciones simples
1. Cambia el email de un estudiante específico (por su ID)
2. Actualiza el precio de un libro específico
3. Marca un libro como NO disponible
4. Actualiza la ciudad de un estudiante

### Ejercicio 5.2: Actualizaciones con condiciones
1. Aumenta el semestre en 1 para todos los estudiantes de "Ingeniería"
2. Aplica un descuento del 10% a todos los libros de categoría "Ficción"
3. Marca como NO disponibles todos los libros publicados antes de 1970
4. Actualiza a activo=FALSE todos los estudiantes con promedio menor a 3.0

### Ejercicio 5.3: Actualizaciones múltiples
1. Actualiza nombre Y email de un estudiante específico
2. Actualiza título, autor Y precio de un libro específico
3. Actualiza carrera Y semestre de estudiantes de una ciudad específica

---

## 🗑️ Parte 6: Operaciones DELETE (10 puntos)

### Ejercicio 6.1: Eliminaciones específicas
1. Elimina un estudiante por su ID
2. Elimina un libro por su ISBN
3. Elimina estudiantes que NO estén activos
4. Elimina libros con precio mayor a 200.00

### Ejercicio 6.2: Eliminaciones con múltiples condiciones
1. Elimina estudiantes menores de 18 años O sin carrera asignada
2. Elimina libros NO disponibles Y publicados antes de 1960
3. Elimina estudiantes de "Valencia" con promedio menor a 3.5

---

## 🚀 Parte 7: Consultas Avanzadas (20 puntos)

### Ejercicio 7.1: Funciones de agregación
1. Calcula el promedio de edad de todos los estudiantes
2. Encuentra el precio máximo y mínimo de los libros
3. Cuenta cuántos estudiantes hay por ciudad
4. Calcula el promedio académico por carrera
5. Suma el total de páginas de todos los libros disponibles

### Ejercicio 7.2: GROUP BY y HAVING
1. Agrupa estudiantes por ciudad y muestra solo las ciudades con más de 2 estudiantes
2. Agrupa libros por categoría y cuenta cuántos hay en cada una
3. Agrupa libros por autor y muestra solo los autores con más de 1 libro
4. Agrupa estudiantes por semestre y calcula el promedio académico de cada semestre

### Ejercicio 7.3: Subconsultas
1. Encuentra estudiantes con promedio mayor al promedio general
2. Lista libros con precio mayor al precio promedio
3. Encuentra el estudiante con el mejor promedio
4. Lista libros del año más reciente de publicación

### Ejercicio 7.4: Consultas complejas combinadas
1. Estudiantes de las 3 ciudades con más estudiantes, ordenados por promedio (descendente), primeros 10
2. Libros disponibles, de categorías con más de 2 libros, ordenados por precio (ascendente)
3. Estudiantes activos, de semestres impares (1,3,5,7,9), con promedio > 4.0, de "Madrid" o "Barcelona"

---

## 🔐 Parte 8: Índices y Optimización (10 puntos)

### Ejercicio 8.1: Crear índices
1. Crea un índice en la columna `email` de estudiantes
2. Crea un índice en la columna `isbn` de libros
3. Crea un índice compuesto en `ciudad` y `carrera` de estudiantes
4. Crea un índice en `categoria` de libros

### Ejercicio 8.2: Transacciones
1. Crea una transacción que:
   - Actualice el promedio de un estudiante
   - Marque un libro como NO disponible
   - Haz COMMIT si todo es correcto

2. Crea una transacción que:
   - Elimine estudiantes inactivos
   - Actualice precios de libros antiguos
   - Haz ROLLBACK para cancelar los cambios

---

## 🎁 BONUS: Ejercicios Extra (10 puntos adicionales)

### Bonus 1: Consultas creativas
1. Crea una consulta que liste estudiantes "destacados" (promedio > 4.5, activos, semestre > 5)
2. Lista los "libros clásicos" (publicados antes de 1980, disponibles, más de 200 páginas)
3. Encuentra estudiantes que están en su último semestre por carrera (máximo semestre de cada carrera)

### Bonus 2: Reportes
1. Genera un reporte con: Total estudiantes, promedio de edad, promedio académico general
2. Genera un reporte por categoría de libros: cantidad, precio promedio, precio total
3. Lista estudiantes con el formato: "Nombre Apellido - Carrera (Semestre X) - Promedio: X.XX"

### Bonus 3: Datos de prueba
1. Inserta 20 estudiantes adicionales usando un script automatizado
2. Inserta 15 libros más con datos realistas
3. Crea consultas para analizar la distribución de datos

---

## 📤 Entrega

1. **Archivo SQL**: `ejercicio.sql` con todas tus consultas comentadas
2. **Capturas**: Carpeta con screenshots de los resultados importantes
3. **Reporte**: Documento breve explicando los desafíos encontrados y cómo los resolviste

### Formato de entrega:
```
tu-nombre-apellido/
│
├── ejercicio.sql
├── capturas/
│   ├── parte1-creacion.png
│   ├── parte2-insert.png
│   ├── parte3-select.png
│   └── ...
└── reporte.pdf (o .md)
```

---

## 💡 Consejos

- ✅ **Prueba cada consulta** antes de pasar a la siguiente
- ✅ **Comenta tu código** para recordar qué hace cada parte
- ✅ **Usa nombres descriptivos** en alias y variables
- ✅ **Verifica los resultados** con SELECT antes de UPDATE o DELETE
- ✅ **Haz backup** de tu base de datos antes de operaciones destructivas
- ✅ **Consulta la documentación** cuando tengas dudas
- ✅ **Experimenta** con variaciones de las consultas
- ✅ **Pide ayuda** a la IA para optimizar consultas complejas

---

## 🆘 Recursos de Ayuda

- Revisa el archivo `README.md` para conceptos teóricos
- Consulta `apoyo.sql` para ejemplos de referencia
- Usa la documentación oficial de SQL
- Pide ayuda a tus compañeros o instructor

---

¡Mucha suerte y disfruta aprendiendo SQL! 🚀💪

**Recuerda**: La práctica hace al maestro. No te desanimes si algunas consultas no salen a la primera. ¡Sigue intentando! 🎯
