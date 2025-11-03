# Clase 6 - Debug, Validación y Refactorización de Consultas Python ↔ PostgreSQL

## 📋 Descripción

Este proyecto implementa un sistema completo de gestión de vehículos y pagos utilizando Python y PostgreSQL. La clase se enfoca en garantizar la calidad, seguridad y robustez de las operaciones CRUD mediante técnicas de debugging, validación y el uso de IA para prevenir errores comunes.

## 🎯 Objetivos de la Clase Tutoría

### 1. Asegurar el Correcto Flujo de Datos
- Validar la integridad de datos entre Python y PostgreSQL
- Implementar manejo robusto de errores en todas las operaciones
- Garantizar transacciones seguras y consistentes
- Verificar tipos de datos y restricciones de la base de datos

### 2. Usar IA para Evitar Errores Comunes
- Prevención de errores de lógica mediante análisis asistido por IA
- Detección anticipada de problemas de tipos de datos
- Generación de código más seguro y eficiente
- Mejores prácticas en el manejo de conexiones y consultas

### 3. Optimización y Refactorización
- Mejorar el rendimiento de las consultas
- Aplicar principios de código limpio
- Implementar patrones de diseño apropiados
- Documentar el código de forma efectiva

## 🚀 Actividades Principales

### 1. Pruebas de Errores Comunes

#### a) Conexión Fallida
```python
# Escenarios a probar:
- Credenciales incorrectas
- Base de datos no disponible
- Timeout de conexión
- Problemas de red
```

**Soluciones implementadas:**
- Manejo de excepciones con `try-except`
- Mensajes de error descriptivos
- Reintentos automáticos
- Logging de errores

#### b) Claves Duplicadas
```python
# Casos de prueba:
- Inserción de ID duplicado
- Violación de restricción UNIQUE
- Conflictos en claves primarias
```

**Estrategias de manejo:**
- Validación previa a la inserción
- Uso de `ON CONFLICT` en PostgreSQL
- Mensajes claros al usuario
- Rollback de transacciones

#### c) Campos Nulos
```python
# Validaciones:
- Campos obligatorios (NOT NULL)
- Valores por defecto
- Validación de entrada del usuario
```

**Implementación:**
- Validación en el modelo de datos
- Constraints en la base de datos
- Mensajes de validación amigables

### 2. Revisión Asistida por IA: Flujo Completo CRUD

#### CREATE (Crear)
- ✅ Validación de datos de entrada
- ✅ Manejo de tipos de datos
- ✅ Prevención de inyección SQL
- ✅ Confirmación de creación exitosa

#### READ (Leer)
- ✅ Consultas parametrizadas
- ✅ Manejo de resultados vacíos
- ✅ Optimización de queries
- ✅ Formateo de datos de salida

#### UPDATE (Actualizar)
- ✅ Verificación de existencia previa
- ✅ Validación de datos actualizados
- ✅ Manejo de concurrencia
- ✅ Confirmación de actualización

#### DELETE (Eliminar)
- ✅ Verificación de dependencias
- ✅ Confirmación antes de eliminar
- ✅ Manejo de eliminación en cascada
- ✅ Logging de operaciones críticas

### 3. Generación de Código de Conexión Seguro con IA

#### Mejores Prácticas Implementadas:

**🔒 Seguridad:**
```python
- Uso de variables de entorno para credenciales
- Consultas parametrizadas (prevención de SQL injection)
- Validación y sanitización de inputs
- Manejo seguro de contraseñas
```

**⚡ Rendimiento:**
```python
- Pool de conexiones
- Reutilización de conexiones
- Cierre apropiado de recursos
- Uso de transacciones
```

**🛡️ Robustez:**
```python
- Manejo exhaustivo de excepciones
- Logging detallado
- Reintentos con backoff exponencial
- Timeouts configurables
```


## 🔧 Configuración del Proyecto

### Requisitos Previos
```bash
- Python 3.8+
- PostgreSQL 12+
- psycopg2
```

### Instalación

1. **Clonar el repositorio**
```powershell
git clone <repositorio>
cd "Clase 6 - Debug, validación y refactorización de consultas Python ↔ PostgreSQL"
```

2. **Crear entorno virtual**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Instalar dependencias**
```powershell
pip install psycopg2-binary python-dotenv
```

4. **Configurar base de datos**
```powershell
# Crear base de datos en PostgreSQL
psql -U postgres
CREATE DATABASE gestion_vehiculos;
\q

# Importar schema
psql -U postgres -d gestion_vehiculos -f drawSQL-pgsql-export-2025-10-28.sql
```

5. **Configurar variables de entorno**
```powershell
# Crear archivo .env
echo "DB_HOST=localhost" > .env
echo "DB_PORT=5432" >> .env
echo "DB_NAME=gestion_vehiculos" >> .env
echo "DB_USER=postgres" >> .env
echo "DB_PASSWORD=tu_password" >> .env
```

## 🧪 Pruebas y Validación

### Ejecutar el Programa
```powershell
python app.py
```

### Casos de Prueba Recomendados

1. **Prueba de Conexión**
   - Verificar conexión exitosa
   - Probar con credenciales incorrectas
   - Simular base de datos no disponible

2. **Prueba de CRUD Completo**
   - Crear registros válidos
   - Intentar crear duplicados
   - Leer registros existentes y no existentes
   - Actualizar con datos válidos e inválidos
   - Eliminar registros con y sin dependencias

3. **Prueba de Validaciones**
   - Campos nulos en campos obligatorios
   - Tipos de datos incorrectos
   - Valores fuera de rango
   - Formatos incorrectos

## 📊 Modelo de Datos

### Tablas Principales

**tipo_vehiculos**
- `id_tipo_vehiculo` (PK)
- `nombre`
- `descripcion`

**vehiculos**
- `id_vehiculo` (PK)
- `placa` (UNIQUE)
- `marca`
- `modelo`
- `anio`
- `color`
- `id_tipo_vehiculo` (FK)

**pagos**
- `id_pago` (PK)
- `id_vehiculo` (FK)
- `fecha_pago`
- `monto`
- `metodo_pago`
- `concepto`

## 🤖 Uso de IA en el Desarrollo

### Aplicaciones Prácticas

1. **Generación de Código**
   - Consultas SQL optimizadas
   - Funciones CRUD con manejo de errores
   - Validaciones de datos

2. **Detección de Errores**
   - Análisis estático de código
   - Identificación de vulnerabilidades
   - Sugerencias de mejoras

3. **Documentación**
   - Generación automática de docstrings
   - Comentarios explicativos
   - README y guías de uso

4. **Testing**
   - Casos de prueba exhaustivos
   - Datos de prueba realistas
   - Escenarios edge case

## 📝 Mejores Prácticas Aprendidas

### 1. Manejo de Conexiones
```python
✅ Usar context managers (with statement)
✅ Cerrar conexiones explícitamente
✅ Implementar pool de conexiones
❌ Dejar conexiones abiertas
❌ Conexiones globales sin control
```

### 2. Consultas SQL
```python
✅ Usar consultas parametrizadas
✅ Validar inputs antes de consultar
✅ Manejar excepciones específicas
❌ Concatenar strings en queries
❌ Ignorar errores silenciosamente
```

### 3. Validación de Datos
```python
✅ Validar en múltiples capas
✅ Mensajes de error descriptivos
✅ Logging de operaciones importantes
❌ Confiar ciegamente en el input
❌ Errores genéricos sin contexto
```

## 🔍 Debugging Efectivo

### Herramientas Utilizadas
- **Print statements estratégicos**
- **Logging con diferentes niveles**
- **Try-except con mensajes detallados**
- **Validación de tipos de datos**
- **Revisión de logs de PostgreSQL**

### Técnicas de IA para Debugging
- Análisis de stack traces
- Sugerencias de correcciones
- Explicación de errores
- Generación de pruebas unitarias

## 📚 Recursos Adicionales

- [Documentación de psycopg2](https://www.psycopg.org/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Python Database API Specification](https://peps.python.org/pep-0249/)
- [SQL Injection Prevention](https://owasp.org/www-community/attacks/SQL_Injection)

## 🎓 Conclusiones

Esta clase proporciona las herramientas y conocimientos necesarios para:

- ✅ Desarrollar aplicaciones Python-PostgreSQL robustas
- ✅ Prevenir y solucionar errores comunes
- ✅ Implementar código seguro y eficiente
- ✅ Utilizar IA como asistente en el desarrollo
- ✅ Aplicar mejores prácticas de la industria

