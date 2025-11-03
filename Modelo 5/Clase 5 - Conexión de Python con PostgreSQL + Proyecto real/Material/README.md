# Conexión de Python con PostgreSQL (psycopg2)

Este ejemplo muestra cómo conectar a PostgreSQL desde Python usando `psycopg2`, crear una tabla, insertar registros de forma segura y listarlos.

## Archivos
- `connection_postgres.py`: Script principal con funciones educativas y un flujo `main` de demostración.
- `requirements.txt`: Dependencia recomendada para entorno local (Windows): `psycopg2-binary`.

## Requisitos
- Python 3.8+
- PostgreSQL accesible (local o remoto) y una base de datos llamada `biblioteca`.

## Configuración rápida (Windows PowerShell)

```powershell
# 1) Crear y activar un entorno virtual (opcional pero recomendado)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Configurar credenciales en connection_postgres.py (usuario/contraseña/host/puerto)
#    Asegúrate de que la base de datos 'biblioteca' exista.

# 4) Ejecutar el script
python .\connection_postgres.py
```

Si la conexión es exitosa, el script:
1. Verifica/crea la tabla `libros`.
2. Inserta un libro de prueba.
3. Muestra el listado de libros.

## Notas
- `psycopg2-binary` es ideal para desarrollo local ya que evita compilar librerías nativas. Para producción, considera usar `psycopg2` estándar y gestionar las libs del sistema (libpq).
- El código usa `commit()` y `rollback()` para asegurar consistencia, y parámetros `%s` para prevenir inyección SQL.
