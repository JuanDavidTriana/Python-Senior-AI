from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.proyecto import Proyecto
from models.desarrollador import Desarrollador
from models.habilidad import Habilidad
from models.desarrollador_proyecto import DesarrolladorProyecto
from models.desarrollador_habilidad import DesarrolladorHabilidad
from models.spring import Sprint
from models.user_story import UserStory
from models.tarea import Tarea
from models.tarea_asignacion import TareaAsignacion
from datetime import datetime


# Configurar la conexión a la base de datos PostgreSQL
# Formato: postgresql://usuario:contraseña@host:puerto/nombre_base_datos
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/scrum_db"
engine = create_engine(DATABASE_URL, echo=True)

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()


def crear_datos_prueba():
    """Crear datos de prueba para verificar que los modelos funcionan correctamente"""
    
    print("\n=== Creando datos de prueba ===\n")
    
    # Crear Proyecto
    proyecto1 = Proyecto(
        id=1,
        nombre="Sistema de Gestión",
        descripcion="Sistema para gestionar proyectos Scrum",
        fecha_inicio=datetime(2025, 1, 1),
        fecha_fin=datetime(2025, 6, 30),
        product_owner_id=1,
        scrum_master_id=2
    )
    session.add(proyecto1)
    
    # Crear Desarrolladores
    dev1 = Desarrollador(
        id=1,
        nombre="Juan",
        apellido="Pérez",
        correo="juan.perez@example.com",
        telefono="555-0001",
        rol_scrum="Product Owner",
        seniority="Senior",
        estado="Activo"
    )
    
    dev2 = Desarrollador(
        id=2,
        nombre="María",
        apellido="González",
        correo="maria.gonzalez@example.com",
        telefono="555-0002",
        rol_scrum="Scrum Master",
        seniority="Senior",
        estado="Activo"
    )
    
    dev3 = Desarrollador(
        id=3,
        nombre="Carlos",
        apellido="López",
        correo="carlos.lopez@example.com",
        telefono="555-0003",
        rol_scrum="Developer",
        seniority="Mid",
        estado="Activo"
    )
    
    session.add_all([dev1, dev2, dev3])
    
    # Crear Habilidades
    habilidad1 = Habilidad(
        id=1,
        nombre="Python",
        categoria="Lenguaje de Programación"
    )
    
    habilidad2 = Habilidad(
        id=2,
        nombre="SQLAlchemy",
        categoria="Framework"
    )
    
    habilidad3 = Habilidad(
        id=3,
        nombre="Scrum",
        categoria="Metodología"
    )
    
    session.add_all([habilidad1, habilidad2, habilidad3])
    
    # Crear Desarrollador-Proyecto
    dev_proyecto1 = DesarrolladorProyecto(
        id=1,
        desarrollador_id=3,
        proyecto_id=1,
        rol_en_proyecto="Backend Developer"
    )
    session.add(dev_proyecto1)
    
    # Crear Desarrollador-Habilidad
    dev_habilidad1 = DesarrolladorHabilidad(
        id=1,
        desarrollador_id=3,
        habilidad_id=1,
        nivel=4
    )
    
    dev_habilidad2 = DesarrolladorHabilidad(
        id=2,
        desarrollador_id=3,
        habilidad_id=2,
        nivel=3
    )
    
    session.add_all([dev_habilidad1, dev_habilidad2])
    
    # Crear Sprint
    sprint1 = Sprint(
        id=1,
        proyecto_id=1,
        nombre="Sprint 1",
        objetivo="Implementar modelos de base de datos",
        fecha_inicio=datetime(2025, 1, 1),
        fecha_fin=datetime(2025, 1, 14),
        estado="En Progreso"
    )
    session.add(sprint1)
    
    # Crear User Story
    user_story1 = UserStory(
        id=1,
        proyecto_id=1,
        sprint_id=1,
        titulo="Crear modelos SQLAlchemy",
        descripcion="Como desarrollador, necesito crear los modelos de la base de datos",
        prioridad="Alta",
        puntos=8,
        estado="En Progreso"
    )
    session.add(user_story1)
    
    # Crear Tarea
    tarea1 = Tarea(
        id=1,
        user_story_id=1,
        titulo="Definir modelo Proyecto",
        descripcion="Crear el modelo SQLAlchemy para la tabla proyectos",
        horas_estimadas=datetime(2025, 1, 1, 4, 0),  # 4 horas
        horas_restantes=datetime(2025, 1, 1, 2, 0),  # 2 horas
        estado="En Progreso"
    )
    session.add(tarea1)
    
    # Crear Tarea Asignación
    tarea_asignacion1 = TareaAsignacion(
        id=1,
        tarea_id=1,
        desarrollador_id=3,
        fecha_asignacion=datetime(2025, 1, 1, 9, 0)
    )
    session.add(tarea_asignacion1)
    
    # Commit de todos los cambios
    session.commit()
    print("✓ Datos de prueba creados exitosamente\n")


def consultar_datos():
    """Consultar y mostrar los datos creados"""
    
    print("\n=== Consultando datos ===\n")
    
    # Consultar proyectos
    proyectos = session.query(Proyecto).all()
    print(f"Proyectos: {len(proyectos)}")
    for p in proyectos:
        print(f"  - {p.nombre}: {p.descripcion}")
    
    # Consultar desarrolladores
    desarrolladores = session.query(Desarrollador).all()
    print(f"\nDesarrolladores: {len(desarrolladores)}")
    for d in desarrolladores:
        print(f"  - {d.nombre} {d.apellido} ({d.rol_scrum}) - {d.seniority}")
    
    # Consultar habilidades
    habilidades = session.query(Habilidad).all()
    print(f"\nHabilidades: {len(habilidades)}")
    for h in habilidades:
        print(f"  - {h.nombre} ({h.categoria})")
    
    # Consultar sprints
    sprints = session.query(Sprint).all()
    print(f"\nSprints: {len(sprints)}")
    for s in sprints:
        print(f"  - {s.nombre}: {s.objetivo} - Estado: {s.estado}")
    
    # Consultar user stories
    user_stories = session.query(UserStory).all()
    print(f"\nUser Stories: {len(user_stories)}")
    for us in user_stories:
        print(f"  - {us.titulo} (Prioridad: {us.prioridad}, Puntos: {us.puntos})")
    
    # Consultar tareas
    tareas = session.query(Tarea).all()
    print(f"\nTareas: {len(tareas)}")
    for t in tareas:
        print(f"  - {t.titulo}: {t.descripcion}")
    
    # Consultar relaciones
    print(f"\nDesarrolladores en proyectos: {session.query(DesarrolladorProyecto).count()}")
    print(f"Habilidades de desarrolladores: {session.query(DesarrolladorHabilidad).count()}")
    print(f"Asignaciones de tareas: {session.query(TareaAsignacion).count()}")


def verificar_relaciones():
    """Verificar que las relaciones entre modelos funcionan correctamente"""
    
    print("\n=== Verificando relaciones ===\n")
    
    # Obtener un desarrollador y sus habilidades
    dev = session.query(Desarrollador).filter_by(id=3).first()
    if dev:
        print(f"Desarrollador: {dev.nombre} {dev.apellido}")
        print(f"Habilidades:")
        for dh in dev.desarrollador_habilidades:
            print(f"  - {dh.habilidad.nombre}: Nivel {dh.nivel}")
    
    # Obtener un proyecto y sus sprints
    proyecto = session.query(Proyecto).filter_by(id=1).first()
    if proyecto:
        print(f"\nProyecto: {proyecto.nombre}")
        print(f"Sprints:")
        for sprint in proyecto.sprints:
            print(f"  - {sprint.nombre}: {sprint.estado}")
    
    # Obtener un sprint y sus user stories
    sprint = session.query(Sprint).filter_by(id=1).first()
    if sprint:
        print(f"\nSprint: {sprint.nombre}")
        print(f"User Stories:")
        for us in sprint.user_stories:
            print(f"  - {us.titulo} ({us.estado})")
    
    # Obtener una user story y sus tareas
    us = session.query(UserStory).filter_by(id=1).first()
    if us:
        print(f"\nUser Story: {us.titulo}")
        print(f"Tareas:")
        for tarea in us.tareas:
            print(f"  - {tarea.titulo} ({tarea.estado})")
    
    # Obtener una tarea y sus asignaciones
    tarea = session.query(Tarea).filter_by(id=1).first()
    if tarea:
        print(f"\nTarea: {tarea.titulo}")
        print(f"Asignada a:")
        for asignacion in tarea.tarea_asignaciones:
            dev = asignacion.desarrollador
            print(f"  - {dev.nombre} {dev.apellido} (Fecha: {asignacion.fecha_asignacion})")


if __name__ == "__main__":
    try:
        print("=" * 60)
        print("PRUEBA DE MODELOS SCRUM")
        print("=" * 60)
        
        # Crear datos de prueba
        crear_datos_prueba()
        
        # Consultar datos
        consultar_datos()
        
        # Verificar relaciones
        verificar_relaciones()
        
        print("\n" + "=" * 60)
        print("✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        session.rollback()
    finally:
        session.close()
