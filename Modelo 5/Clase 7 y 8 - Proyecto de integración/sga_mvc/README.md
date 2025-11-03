# Sistema de Gestión Académica (SGA)

Sistema de gestión académica desarrollado con Python y PostgreSQL siguiendo el patrón MVC (Modelo-Vista-Controlador).

## 📋 Requisitos Previos

- Python 3.10 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

### 1. Clonar el repositorio o descargar el proyecto

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## 🗄️ Configuración de la Base de Datos

### 1. Crear la base de datos en PostgreSQL

Abre psql o pgAdmin y ejecuta:

```sql
CREATE DATABASE sga_mvc;
```

### 2. Configurar las credenciales

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sga_mvc
DB_USER=postgres
DB_PASSWORD=tu_contraseña_aqui
```

### 3. Inicializar el esquema de la base de datos

Ejecuta la aplicación y selecciona la opción `5. Inicializar BD (crear tablas)`:

```bash
python run.py
```

### 4. (Opcional) Cargar datos de prueba

Puedes insertar datos de prueba ejecutando el archivo SQL:

```bash
psql -U postgres -d sga_mvc -f datos_prueba.sql
```

O copiando el contenido de `datos_prueba.sql` y ejecutándolo en tu cliente SQL favorito.

## ▶️ Ejecución

Para iniciar la aplicación, ejecuta:

```bash
python run.py
```

## 📂 Estructura del Proyecto

```
sga_mvc/
│
├── app/
│   ├── controllers/         # Controladores (lógica de negocio)
│   │   ├── alumno_controller.py
│   │   ├── docente_controller.py
│   │   ├── nota_controller.py
│   │   └── programa_controller.py
│   │
│   ├── db/                  # Configuración de base de datos
│   │   ├── connection.py    # Conexión a PostgreSQL
│   │   ├── init_db.py       # Inicialización del esquema
│   │   └── schema.sql       # Esquema de tablas
│   │
│   ├── models/              # Modelos de datos
│   │   ├── alumno.py
│   │   ├── docente.py
│   │   ├── nota.py
│   │   └── programa.py
│   │
│   ├── repositories/        # Acceso a datos (CRUD)
│   │   ├── alumno_repo.py
│   │   ├── docente_repo.py
│   │   ├── nota_repo.py
│   │   └── programa_repo.py
│   │
│   ├── utils/               # Utilidades
│   │   ├── exceptions.py    # Excepciones personalizadas
│   │   └── validators.py    # Validaciones
│   │
│   ├── views/               # Interfaz de usuario
│   │   └── menu.py          # Menú interactivo
│   │
│   └── main.py              # Punto de entrada de la app
│
├── run.py                   # Script de ejecución
├── datos_prueba.sql         # Datos de prueba
├── requirements.txt         # Dependencias
└── README.md               # Este archivo
```

## 🎯 Funcionalidades

### Gestión de Docentes
- ✅ Crear docente
- ✅ Listar docentes
- ✅ Actualizar docente
- ✅ Eliminar docente

### Gestión de Programas
- ✅ Crear programa
- ✅ Listar programas
- ✅ Actualizar programa
- ✅ Eliminar programa
- ✅ Asignar docente a programa

### Gestión de Alumnos
- ✅ Crear alumno
- ✅ Listar alumnos
- ✅ Actualizar alumno
- ✅ Eliminar alumno
- ✅ Ver promedio de notas

### Gestión de Notas
- ✅ Crear nota
- ✅ Actualizar nota
- ✅ Eliminar nota
- ✅ Listar notas por alumno

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+**
- **PostgreSQL** - Base de datos relacional
- **psycopg2-binary** - Adaptador de PostgreSQL para Python
- **python-dotenv** - Gestión de variables de entorno
- **rich** - Formato mejorado de texto en consola

## 📝 Validaciones Implementadas

- Validación de correos electrónicos únicos
- Validación de calificaciones (0.0 - 5.0)
- Validación de integridad referencial
- Validación de duraciones positivas
- Prevención de eliminación de registros con dependencias

