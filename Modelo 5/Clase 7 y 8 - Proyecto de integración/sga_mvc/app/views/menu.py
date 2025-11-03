from __future__ import annotations

from app.controllers.docente_controller import DocenteController
from app.controllers.programa_controller import ProgramaController
from app.controllers.alumno_controller import AlumnoController
from app.controllers.nota_controller import NotaController
from app.utils.exceptions import DomainError, IntegrityError, NotFoundError
from app.db.init_db import init_schema
from app.db.connection import health_check


def prompt_int(msg: str) -> int:
    return int(input(msg).strip())


def prompt_float(msg: str) -> float:
    return float(input(msg).strip())


def pause() -> None:
    input("\nPresiona Enter para continuar...")


def menu_principal() -> None:
    while True:
        print("\n=== Sistema de Gestión Académica (SGA) ===")
        print("1. Docentes")
        print("2. Programas")
        print("3. Alumnos")
        print("4. Notas")
        print("5. Inicializar BD (crear tablas)")
        print("6. Health Check BD")
        print("0. Salir")
        op = input("Selecciona una opción: ").strip()
        if op == "1":
            menu_docentes()
        elif op == "2":
            menu_programas()
        elif op == "3":
            menu_alumnos()
        elif op == "4":
            menu_notas()
        elif op == "5":
            try:
                init_schema()
                print("Esquema creado/actualizado correctamente.")
            except Exception as e:
                print(f"Error al inicializar BD: {e}")
            pause()
        elif op == "6":
            ok = health_check()
            print("BD OK" if ok else "BD NO DISPONIBLE")
            pause()
        elif op == "0":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida.")
            pause()


def handle_action(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except (DomainError, IntegrityError, NotFoundError) as e:
            print(f"Error: {e}")
        except ValueError:
            print("Entrada inválida (tipo de dato).")
        except Exception as e:
            print(f"Error inesperado: {e}")
        finally:
            pause()
    return wrapper


# --------- DOCENTES ---------
@handle_action
def docentes_crear():
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    d = DocenteController.crear(nombre, correo)
    print(f"Docente creado: {d}")


def docentes_listar():
    docs = DocenteController.listar()
    if not docs:
        print("No hay docentes.")
    else:
        for d in docs:
            print(f"[{d.id}] {d.nombre} - {d.correo}")
    pause()


@handle_action
def docentes_actualizar():
    docente_id = prompt_int("ID a actualizar: ")
    nombre = input("Nuevo nombre: ")
    correo = input("Nuevo correo: ")
    DocenteController.actualizar(docente_id, nombre, correo)
    print("Actualizado correctamente.")


@handle_action
def docentes_eliminar():
    docente_id = prompt_int("ID a eliminar: ")
    DocenteController.eliminar(docente_id)
    print("Eliminado correctamente.")


def menu_docentes():
    while True:
        print("\n--- Docentes ---")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("0. Volver")
        op = input("Opción: ").strip()
        if op == "1":
            docentes_crear()
        elif op == "2":
            docentes_listar()
        elif op == "3":
            docentes_actualizar()
        elif op == "4":
            docentes_eliminar()
        elif op == "0":
            break
        else:
            print("Opción inválida.")
            pause()


# --------- PROGRAMAS ---------
@handle_action
def programas_crear():
    nombre = input("Nombre: ")
    duracion = prompt_int("Duración (int): ")
    docente_id_str = input("Docente ID (opcional, Enter para ninguno): ").strip()
    docente_id = int(docente_id_str) if docente_id_str else None
    p = ProgramaController.crear(nombre, duracion, docente_id)
    print(f"Programa creado: {p}")


def programas_listar():
    progs = ProgramaController.listar()
    if not progs:
        print("No hay programas.")
    else:
        for p in progs:
            print(f"[{p.id}] {p.nombre} - {p.duracion} - docente_id={p.docente_id}")
    pause()


@handle_action
def programas_actualizar():
    programa_id = prompt_int("ID a actualizar: ")
    nombre = input("Nuevo nombre: ")
    duracion = prompt_int("Nueva duración (int): ")
    docente_id_str = input("Nuevo docente ID (opcional, Enter para ninguno): ").strip()
    docente_id = int(docente_id_str) if docente_id_str else None
    ProgramaController.actualizar(programa_id, nombre, duracion, docente_id)
    print("Actualizado correctamente.")


@handle_action
def programas_eliminar():
    programa_id = prompt_int("ID a eliminar: ")
    ProgramaController.eliminar(programa_id)
    print("Eliminado correctamente.")


def menu_programas():
    while True:
        print("\n--- Programas ---")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("0. Volver")
        op = input("Opción: ").strip()
        if op == "1":
            programas_crear()
        elif op == "2":
            programas_listar()
        elif op == "3":
            programas_actualizar()
        elif op == "4":
            programas_eliminar()
        elif op == "0":
            break
        else:
            print("Opción inválida.")
            pause()


# --------- ALUMNOS ---------
@handle_action
def alumnos_crear():
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    programa_id = prompt_int("Programa ID: ")
    a = AlumnoController.crear(nombre, correo, programa_id)
    print(f"Alumno creado: {a}")


def alumnos_listar():
    alums = AlumnoController.listar()
    if not alums:
        print("No hay alumnos.")
    else:
        for a in alums:
            print(f"[{a.id}] {a.nombre} - {a.correo} - programa_id={a.programa_id}")
    pause()


@handle_action
def alumnos_actualizar():
    alumno_id = prompt_int("ID a actualizar: ")
    nombre = input("Nuevo nombre: ")
    correo = input("Nuevo correo: ")
    programa_id = prompt_int("Nuevo programa ID: ")
    AlumnoController.actualizar(alumno_id, nombre, correo, programa_id)
    print("Actualizado correctamente.")


@handle_action
def alumnos_eliminar():
    alumno_id = prompt_int("ID a eliminar: ")
    AlumnoController.eliminar(alumno_id)
    print("Eliminado correctamente.")


@handle_action
def alumnos_promedio():
    alumno_id = prompt_int("Alumno ID: ")
    prom = AlumnoController.promedio(alumno_id)
    if prom is None:
        print("El alumno no tiene notas registradas.")
    else:
        print(f"Promedio: {prom:.2f}")


def menu_alumnos():
    while True:
        print("\n--- Alumnos ---")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Ver promedio")
        print("0. Volver")
        op = input("Opción: ").strip()
        if op == "1":
            alumnos_crear()
        elif op == "2":
            alumnos_listar()
        elif op == "3":
            alumnos_actualizar()
        elif op == "4":
            alumnos_eliminar()
        elif op == "5":
            alumnos_promedio()
        elif op == "0":
            break
        else:
            print("Opción inválida.")
            pause()


# --------- NOTAS ---------
@handle_action
def notas_crear():
    alumno_id = prompt_int("Alumno ID: ")
    asignatura = input("Asignatura: ")
    calificacion = prompt_float("Calificación (0..5): ")
    n = NotaController.crear(alumno_id, asignatura, calificacion)
    print(f"Nota creada: {n}")


@handle_action
def notas_actualizar():
    nota_id = prompt_int("ID de nota a actualizar: ")
    asignatura = input("Nueva asignatura: ")
    calificacion = prompt_float("Nueva calificación (0..5): ")
    NotaController.actualizar(nota_id, asignatura, calificacion)
    print("Actualizado correctamente.")


@handle_action
def notas_eliminar():
    nota_id = prompt_int("ID de nota a eliminar: ")
    NotaController.eliminar(nota_id)
    print("Eliminado correctamente.")


@handle_action
def notas_listar_por_alumno():
    alumno_id = prompt_int("Alumno ID: ")
    notas = NotaController.listar_por_alumno(alumno_id)
    if not notas:
        print("El alumno no tiene notas.")
    else:
        for n in notas:
            print(f"[{n.id}] {n.asignatura} - {n.calificacion:.1f}")


def menu_notas():
    while True:
        print("\n--- Notas ---")
        print("1. Crear")
        print("2. Actualizar")
        print("3. Eliminar")
        print("4. Listar por alumno")
        print("0. Volver")
        op = input("Opción: ").strip()
        if op == "1":
            notas_crear()
        elif op == "2":
            notas_actualizar()
        elif op == "3":
            notas_eliminar()
        elif op == "4":
            notas_listar_por_alumno()
        elif op == "0":
            break
        else:
            print("Opción inválida.")
            pause()
