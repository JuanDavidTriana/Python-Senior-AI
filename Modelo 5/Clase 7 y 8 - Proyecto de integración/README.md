# 📚 Sistema de Gestión Académica (SGA) — Proyecto de Integración# Sistema de Gestión Académica (SGA) — MVC (Python + PostgreSQL)



## 🎯 Clase 7 y 8: Proyecto de Integración + Mejores PrácticasEste proyecto implementa un SGA de consola siguiendo el patrón MVC:

- Modelo: Entidades y acceso a datos (CRUD con PostgreSQL)

### Objetivos de Aprendizaje- Vista: Menús y prompts en consola

- ✅ Aplicar todo lo aprendido en un **sistema funcional** con conexión real a base de datos- Controlador: Lógica de negocio y validaciones

- ✅ Validar, guardar y actualizar datos desde Python de forma **profesional**

- ✅ Implementar un **sistema completo** de gestión académica con:## Requisitos

  - Gestión de Alumnos, Docentes, Programas y Notas- Python 3.12+

  - Operaciones CRUD completas (Create, Read, Update, Delete)- PostgreSQL 14+

  - Validaciones robustas de datos

  - Menú interactivo y navegable## Configuración rápida

  - Conexión segura a PostgreSQL1. Crear y ajustar el archivo .env (a partir de .env.example):

- ✅ Aplicar **mejores prácticas** de desarrollo Python profesional   - DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

2. Crear la base de datos `sga_mvc` y ejecutar el script de esquema:

---   - app/db/schema.sql

3. Instalar dependencias.

## 🏗️ Arquitectura del Proyecto: Patrón MVC4. Ejecutar la app.



Este proyecto implementa un **Sistema de Gestión Académica (SGA)** siguiendo el **patrón de diseño MVC (Model-View-Controller)**, una arquitectura fundamental en desarrollo de software que separa las responsabilidades en capas bien definidas:## Instalación de dependencias

```powershell

```# Desde la carpeta sga_mvc

┌─────────────────────────────────────────────────────────┐python -m venv .venv ; .\.venv\Scripts\Activate.ps1 ; pip install -r requirements.txt

│                    VISTA (Views)                        │```

│              Interfaz de usuario (menús)                │

│                   app/views/menu.py                     │## Inicializar base de datos

└────────────────────┬────────────────────────────────────┘Crea la base de datos en PostgreSQL y ejecuta el esquema:

                     │```sql

                     ↓-- Ejecuta el contenido de app/db/schema.sql en tu servidor PostgreSQL

┌─────────────────────────────────────────────────────────┐```

│               CONTROLADOR (Controllers)                 │

│        Lógica de negocio y validaciones                │## Ejecutar

│         app/controllers/*_controller.py                 │```powershell

└────────────────────┬────────────────────────────────────┘# Desde la carpeta sga_mvc

                     │.\.venv\Scripts\Activate.ps1 ; python -m app.main

                     ↓```

┌─────────────────────────────────────────────────────────┐

│             REPOSITORIO (Repositories)                  │## Estructura

│          Acceso a datos y operaciones CRUD              │- app/db/connection.py: Conexión y pool a PostgreSQL (psycopg2)

│           app/repositories/*_repo.py                    │- app/db/schema.sql: Esquema relacional

└────────────────────┬────────────────────────────────────┘- app/models/: Entidades (dataclasses)

                     │- app/repositories/: CRUD por entidad

                     ↓- app/controllers/: Lógica de negocio

┌─────────────────────────────────────────────────────────┐- app/views/: Menús de consola

│                 MODELO (Models)                         │- app/utils/: Validadores y excepciones

│           Entidades de dominio (dataclasses)            │

│               app/models/*.py                           │## Reglas de negocio clave

└─────────────────────────────────────────────────────────┘- No se puede eliminar un docente si tiene programas asociados.

                     │- Correos de docentes y alumnos son únicos.

                     ↓- Mostrar promedio de calificaciones por estudiante.

┌─────────────────────────────────────────────────────────┐

│              BASE DE DATOS (PostgreSQL)                 │## Notas

│                    app/db/                              │- Usa `python-dotenv` para cargar variables desde `.env`.

└─────────────────────────────────────────────────────────┘- Si deseas Docker, agrega un `docker-compose.yml` con PostgreSQL (opcional).

```

### 📦 Capas de la Arquitectura

#### 1. **Vista (View)** - `app/views/`
- **Responsabilidad**: Interacción con el usuario
- **Implementación**: Menús interactivos en consola
- **Características**:
  - Menú principal navegable
  - Submenús por entidad (Docentes, Programas, Alumnos, Notas)
  - Manejo de entrada del usuario con validación de tipos
  - Mensajes de confirmación y error
  - Sistema de pausa para mejor UX

#### 2. **Controlador (Controller)** - `app/controllers/`
- **Responsabilidad**: Lógica de negocio y orquestación
- **Implementación**: Un controlador por entidad
- **Características**:
  - Validación de datos de entrada
  - Aplicación de reglas de negocio
  - Coordinación entre vista y repositorio
  - Manejo de excepciones personalizadas
  - Transformación de datos

#### 3. **Repositorio (Repository)** - `app/repositories/`
- **Responsabilidad**: Acceso a datos (capa de persistencia)
- **Implementación**: Patrón Repository para abstracción de BD
- **Características**:
  - Operaciones CRUD completas
  - Queries SQL parametrizadas (prevención de SQL Injection)
  - Transacciones automáticas con context managers
  - Mapeo de resultados SQL a objetos Python
  - Queries especiales (promedios, búsquedas por email, etc.)

#### 4. **Modelo (Model)** - `app/models/`
- **Responsabilidad**: Representación de entidades del dominio
- **Implementación**: Dataclasses de Python
- **Características**:
  - Clases de datos inmutables y tipadas
  - Representación clara del modelo de dominio
  - Sin lógica de negocio (solo estructura de datos)

---

## 🔑 Conceptos y Mejores Prácticas Aplicadas

### 1. **Patrón MVC (Model-View-Controller)**
- ✅ **Separación de responsabilidades**: Cada capa tiene un propósito claro
- ✅ **Mantenibilidad**: Cambios en una capa no afectan las demás
- ✅ **Testabilidad**: Cada componente se puede probar independientemente
- ✅ **Escalabilidad**: Fácil de extender con nuevas funcionalidades

### 2. **Patrón Repository**
```python
# Abstracción del acceso a datos
class AlumnoRepository:
    @staticmethod
    def create(nombre: str, correo: str, programa_id: int) -> Alumno:
        # Encapsula la lógica SQL
    
    @staticmethod
    def get_by_id(alumno_id: int) -> Optional[Alumno]:
        # Retorna objetos del dominio, no tuplas SQL
```
- ✅ Abstrae la lógica de acceso a datos
- ✅ Facilita cambios en la BD sin afectar la lógica de negocio
- ✅ Centraliza las queries SQL en un solo lugar

### 3. **Context Managers para Conexiones a BD**
```python
@contextmanager
def get_connection() -> Iterator[psycopg2.extensions.connection]:
    conn = psycopg2.connect(**get_db_params())
    try:
        yield conn
        conn.commit()  # Commit automático si no hay errores
    except Exception:
        conn.rollback()  # Rollback automático en caso de error
        raise
    finally:
        conn.close()  # Cierre garantizado de la conexión
```
- ✅ **Gestión automática de recursos**: Conexiones siempre se cierran
- ✅ **Transacciones seguras**: Commit/Rollback automáticos
- ✅ **Prevención de memory leaks**: No hay conexiones huérfanas

### 4. **Validaciones Robustas**
```python
# Validación de email con regex
def validate_email(email: str) -> None:
    if not EMAIL_REGEX.match(email or ""):
        raise DomainError("Correo electrónico inválido.")

# Validación de calificaciones
def validate_calificacion(value: float) -> None:
    f = float(value)
    if f < 0 or f > 5:
        raise DomainError("Calificación debe estar entre 0 y 5.")
```
- ✅ Validaciones a nivel de dominio
- ✅ Mensajes de error claros y específicos
- ✅ Prevención de datos inválidos en la BD

### 5. **Excepciones Personalizadas**
```python
class DomainError(Exception):
    """Error de validación o regla de negocio"""

class NotFoundError(Exception):
    """Recurso no encontrado"""

class IntegrityError(Exception):
    """Violación de integridad referencial"""
```
- ✅ **Semántica clara**: Cada excepción tiene un significado específico
- ✅ **Manejo granular**: Se pueden manejar diferentes errores de forma distinta
- ✅ **Mejor debugging**: Mensajes más informativos

### 6. **Type Hints (Tipado Estático)**
```python
def crear(nombre: str, correo: str, programa_id: int) -> Alumno:
    validate_email(correo)
    # ...
    
def listar() -> List[Alumno]:
    return AlumnoRepository.get_all()
```
- ✅ **Documentación implícita**: Los tipos documentan el código
- ✅ **Detección temprana de errores**: IDEs y linters detectan problemas
- ✅ **Mejor autocompletado**: IntelliSense más preciso

### 7. **Configuración con Variables de Entorno**
```python
# .env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sga_mvc
DB_USER=postgres
DB_PASSWORD=admin

# connection.py
load_dotenv()
def get_db_params() -> dict:
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "5432")),
        # ...
    }
```
- ✅ **Seguridad**: Credenciales fuera del código fuente
- ✅ **Flexibilidad**: Configuración diferente por entorno (dev, test, prod)
- ✅ **Mejores prácticas**: Seguimiento del principio 12-Factor App

### 8. **SQL Parametrizado (Prevención de SQL Injection)**
```python
# ❌ MAL - Vulnerable a SQL Injection
sql = f"SELECT * FROM alumnos WHERE id = {alumno_id}"

# ✅ BIEN - Parámetros seguros
sql = "SELECT * FROM alumnos WHERE id = %s"
cur.execute(sql, (alumno_id,))
```
- ✅ Protección contra ataques de inyección SQL
- ✅ Escapado automático de valores
- ✅ Rendimiento mejorado (prepared statements)

### 9. **Dataclasses para Modelos**
```python
from dataclasses import dataclass

@dataclass
class Alumno:
    id: int | None
    nombre: str
    correo: str
    programa_id: int
```
- ✅ **Menos boilerplate**: `__init__`, `__repr__`, `__eq__` automáticos
- ✅ **Inmutabilidad opcional**: `frozen=True` para objetos inmutables
- ✅ **Type hints integrados**: Validación de tipos desde Python 3.10+

### 10. **Decoradores para Manejo de Errores**
```python
def handle_action(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except (DomainError, IntegrityError, NotFoundError) as e:
            print(f"Error: {e}")
        except ValueError:
            print("Entrada inválida (tipo de dato).")
        finally:
            pause()
    return wrapper

@handle_action
def alumnos_crear():
    # Lógica sin try/except anidados
```
- ✅ **DRY (Don't Repeat Yourself)**: Manejo de errores centralizado
- ✅ **Código más limpio**: Sin try/except repetidos en cada función
- ✅ **Consistencia**: Mismo manejo de errores en toda la app

---

## 🗄️ Modelo de Datos

### Diagrama de Entidad-Relación

```
┌──────────────┐         ┌──────────────┐
│   DOCENTES   │         │  PROGRAMAS   │
├──────────────┤         ├──────────────┤
│ id (PK)      │←────────│ id (PK)      │
│ nombre       │   1:N   │ nombre       │
│ correo (UQ)  │         │ duracion     │
└──────────────┘         │ docente_id   │
                         └──────┬───────┘
                                │ 1:N
                                ↓
                         ┌──────────────┐
                         │   ALUMNOS    │
                         ├──────────────┤
                         │ id (PK)      │
                         │ nombre       │
                         │ correo (UQ)  │
                         │ programa_id  │
                         └──────┬───────┘
                                │ 1:N
                                ↓
                         ┌──────────────┐
                         │    NOTAS     │
                         ├──────────────┤
                         │ id (PK)      │
                         │ alumno_id    │
                         │ asignatura   │
                         │ calificacion │
                         └──────────────┘
```

### Reglas de Negocio e Integridad

1. **Docentes**
   - Correo único (UNIQUE constraint)
   - No se puede eliminar si tiene programas asociados (validación en controlador)

2. **Programas**
   - Debe tener una duración positiva (validación en controlador)
   - Puede tener o no un docente asignado (docente_id nullable)
   - Si se elimina el docente, docente_id se establece en NULL (ON DELETE SET NULL)

3. **Alumnos**
   - Correo único (UNIQUE constraint)
   - Debe estar asociado a un programa
   - Si se elimina el programa, se eliminan sus alumnos (ON DELETE CASCADE)

4. **Notas**
   - Calificación entre 0 y 5 (CHECK constraint)
   - Debe estar asociada a un alumno existente
   - Si se elimina el alumno, se eliminan sus notas (ON DELETE CASCADE)

---

## 🚀 Instalación y Configuración

### Requisitos Previos
- **Python 3.12+**
- **PostgreSQL 14+**
- **pip** (gestor de paquetes de Python)

### 1. Clonar/Descargar el Proyecto
```powershell
cd "c:\Users\juand\GitHub\Programas Dev Senior Code\Python Senior AI\Modelo 5\Clase 7 y 8 - Proyecto de integración\sga_mvc"
```

### 2. Crear Entorno Virtual
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar Dependencias
```powershell
pip install -r requirements.txt
```

**Dependencias instaladas:**
- `psycopg2-binary==2.9.9` - Adaptador PostgreSQL para Python
- `python-dotenv==1.0.1` - Carga de variables de entorno desde .env
- `rich==13.9.2` - Mejoras visuales para consola (opcional, para futuras mejoras)

### 4. Configurar Variables de Entorno

Crea un archivo `.env` basado en `.env.example`:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sga_mvc
DB_USER=postgres
DB_PASSWORD=tu_password_aqui
```

### 5. Crear Base de Datos

Conéctate a PostgreSQL y crea la base de datos:

```sql
CREATE DATABASE sga_mvc;
```

### 6. Inicializar el Esquema

Tienes dos opciones:

**Opción A: Desde la aplicación (recomendado)**
```powershell
python -m app.main
# Selecciona opción 5: "Inicializar BD (crear tablas)"
```

**Opción B: Manualmente desde PostgreSQL**
```sql
-- Ejecuta el contenido de app/db/schema.sql
\c sga_mvc
\i app/db/schema.sql
```

### 7. (Opcional) Cargar Datos de Prueba

Si existe un archivo `datos_prueba.sql`, puedes cargarlo:

```powershell
psql -U postgres -d sga_mvc -f datos_prueba.sql
```

---

## 🎮 Uso de la Aplicación

### Ejecutar el Sistema

```powershell
# Asegúrate de tener el entorno virtual activado
.\.venv\Scripts\Activate.ps1

# Ejecuta la aplicación
python -m app.main
```

### Navegación del Menú

```
=== Sistema de Gestión Académica (SGA) ===
1. Docentes
2. Programas
3. Alumnos
4. Notas
5. Inicializar BD (crear tablas)
6. Health Check BD
0. Salir
```

### Funcionalidades Principales

#### 1. **Gestión de Docentes**
- ✅ Crear nuevo docente (validación de email)
- ✅ Listar todos los docentes
- ✅ Actualizar información de docente
- ✅ Eliminar docente (validación de programas asociados)

#### 2. **Gestión de Programas**
- ✅ Crear programa con docente asignado (opcional)
- ✅ Listar todos los programas
- ✅ Actualizar programa y cambiar docente
- ✅ Eliminar programa

#### 3. **Gestión de Alumnos**
- ✅ Crear alumno asociado a un programa
- ✅ Listar todos los alumnos
- ✅ Actualizar información del alumno
- ✅ Eliminar alumno
- ✅ **Ver promedio de calificaciones** del alumno

#### 4. **Gestión de Notas**
- ✅ Crear nota para un alumno (validación 0-5)
- ✅ Listar notas por alumno
- ✅ Actualizar calificación
- ✅ Eliminar nota

#### 5. **Utilidades**
- ✅ **Health Check**: Verificar conexión a la base de datos
- ✅ **Inicializar BD**: Crear tablas automáticamente

---

## 📁 Estructura del Proyecto

```
sga_mvc/
├── .env                        # Variables de entorno (NO subir a Git)
├── .env.example                # Plantilla de configuración
├── requirements.txt            # Dependencias del proyecto
├── run.py                      # Punto de entrada alternativo
├── datos_prueba.sql            # Datos de ejemplo (opcional)
├── README.md                   # Este archivo
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada principal
│   │
│   ├── models/                 # 📦 CAPA DE MODELO
│   │   ├── __init__.py
│   │   ├── alumno.py           # Dataclass Alumno
│   │   ├── docente.py          # Dataclass Docente
│   │   ├── programa.py         # Dataclass Programa
│   │   └── nota.py             # Dataclass Nota
│   │
│   ├── repositories/           # 💾 CAPA DE ACCESO A DATOS
│   │   ├── __init__.py
│   │   ├── alumno_repo.py      # CRUD Alumnos
│   │   ├── docente_repo.py     # CRUD Docentes
│   │   ├── programa_repo.py    # CRUD Programas
│   │   └── nota_repo.py        # CRUD Notas
│   │
│   ├── controllers/            # 🎮 CAPA DE LÓGICA DE NEGOCIO
│   │   ├── __init__.py
│   │   ├── alumno_controller.py    # Lógica Alumnos
│   │   ├── docente_controller.py   # Lógica Docentes
│   │   ├── programa_controller.py  # Lógica Programas
│   │   └── nota_controller.py      # Lógica Notas
│   │
│   ├── views/                  # 🖥️ CAPA DE PRESENTACIÓN
│   │   ├── __init__.py
│   │   └── menu.py             # Menús interactivos
│   │
│   ├── db/                     # 🗄️ CONFIGURACIÓN DE BD
│   │   ├── connection.py       # Context manager de conexión
│   │   ├── init_db.py          # Inicialización de esquema
│   │   └── schema.sql          # DDL del esquema
│   │
│   └── utils/                  # 🛠️ UTILIDADES
│       ├── __init__.py
│       ├── exceptions.py       # Excepciones personalizadas
│       └── validators.py       # Validadores de dominio
```

---

## 🧪 Flujo de una Operación Completa

### Ejemplo: Crear un Alumno

```
USUARIO (Vista)
    ↓
[1] Ingresa datos: nombre, correo, programa_id
    ↓
MENÚ (app/views/menu.py)
    ↓
[2] Llama a AlumnoController.crear()
    ↓
CONTROLADOR (app/controllers/alumno_controller.py)
    ↓
[3] Valida email con validators.validate_email()
[4] Verifica que el programa exista en ProgramaRepository
[5] Verifica unicidad del email en AlumnoRepository
    ↓
REPOSITORIO (app/repositories/alumno_repo.py)
    ↓
[6] Ejecuta INSERT con SQL parametrizado
[7] Retorna objeto Alumno con ID generado
    ↓
CONTROLADOR
    ↓
[8] Retorna Alumno al menú
    ↓
MENÚ
    ↓
[9] Muestra mensaje de éxito al usuario
```

**Manejo de Errores en Cada Capa:**
- **Vista**: Captura ValueError (tipo de dato incorrecto)
- **Controlador**: Lanza DomainError (validación de negocio)
- **Repositorio**: Lanza IntegrityError (violación de constraints)

---

## 🎓 Conceptos Clave para Aprender

### 1. Separación de Responsabilidades
Cada capa tiene un propósito específico y no invade las responsabilidades de otras capas.

### 2. Abstracción
El controlador no sabe cómo se almacenan los datos, solo usa la interfaz del repositorio.

### 3. Inyección de Dependencias (Implícita)
Los repositorios reciben la conexión a través del context manager, no la crean ellos mismos.

### 4. Principio DRY (Don't Repeat Yourself)
Validaciones y lógica común centralizadas en `utils/`.

### 5. Fail Fast
Las validaciones se hacen lo antes posible en el flujo de ejecución.

### 6. Transacciones ACID
Todas las operaciones en la BD son atómicas, consistentes, aisladas y duraderas.

### 7. Manejo de Recursos
Context managers garantizan la liberación de recursos (conexiones, cursores).

---

## 🔍 Health Check y Debugging

### Verificar Conexión a BD
Desde el menú principal, opción **6: Health Check BD**

### Logs y Debugging
Para habilitar logs de SQL (debugging):
```python
# En app/db/connection.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `OperationalError: connection refused` | PostgreSQL no está corriendo | Inicia el servicio PostgreSQL |
| `DomainError: Correo inválido` | Email sin formato correcto | Verifica formato `user@domain.com` |
| `IntegrityError: duplicate key` | Email ya existe | Usa un email diferente |
| `NotFoundError: Programa no existe` | programa_id inválido | Verifica que el programa exista |

---

## 🚧 Mejoras Futuras (Ejercicios Propuestos)

1. **Agregar Logging Profesional**
   - Implementar `logging` en lugar de `print()`
   - Logs rotatorios por fecha
   - Diferentes niveles (DEBUG, INFO, WARNING, ERROR)

2. **Testing Automatizado**
   - Unit tests con `pytest`
   - Mocking de base de datos
   - Test de integración

3. **API REST con FastAPI**
   - Exponer funcionalidades como API REST
   - Documentación automática con Swagger
   - Autenticación JWT

4. **Interfaz Gráfica**
   - GUI con `tkinter` o `PyQt`
   - Interfaz web con Flask/Django

5. **Reportes y Estadísticas**
   - Generar PDFs con `reportlab`
   - Gráficos con `matplotlib`
   - Exportación a Excel

6. **Dockerización**
   - `Dockerfile` para la aplicación
   - `docker-compose.yml` con PostgreSQL
   - Orquestación completa

7. **Migraciones de BD**
   - Implementar `alembic` para migraciones
   - Versionado de esquema
   - Rollback de cambios

8. **Caché**
   - Implementar Redis para caché
   - Mejorar rendimiento de consultas frecuentes

---

## 📚 Referencias y Recursos

### Documentación Oficial
- [Python Official Documentation](https://docs.python.org/3/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)

### Patrones de Diseño
- [MVC Pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)

### Mejores Prácticas Python
- [PEP 8 – Style Guide](https://peps.python.org/pep-0008/)
- [The Zen of Python (PEP 20)](https://peps.python.org/pep-0020/)
- [Type Hints (PEP 484)](https://peps.python.org/pep-0484/)

---

## 👨‍💻 Autor y Contacto

**Proyecto Educativo - Clase 7 y 8**  
*Python Senior AI - Modelo 5*  
*Dev Senior Code*

---

## 📄 Licencia

Este proyecto es para fines educativos.

---

## ✅ Checklist de Conceptos Aplicados

- ✅ Patrón MVC (Separación de responsabilidades)
- ✅ Patrón Repository (Abstracción de datos)
- ✅ Context Managers (Gestión de recursos)
- ✅ Type Hints (Tipado estático)
- ✅ Dataclasses (Modelos de dominio)
- ✅ Excepciones personalizadas (Manejo de errores)
- ✅ Validaciones robustas (Integridad de datos)
- ✅ SQL parametrizado (Seguridad)
- ✅ Variables de entorno (Configuración)
- ✅ Decoradores (DRY en manejo de errores)
- ✅ Transacciones automáticas (ACID)
- ✅ Constraints de BD (Integridad referencial)
- ✅ Consultas agregadas (AVG, COUNT)
- ✅ Menú interactivo (UX)
- ✅ Health checks (Monitoreo)

---

**¡Proyecto completo y listo para aprender! 🚀**
