from sqlalchemy.orm import Session
from model.cliente import Cliente # Modelo 
from schema.schema import ClienteCreate # Esquema de Pydantic
import repository.repositoryCliente as repo_cliente
from database.database import SessionLocal, Base, engine
from fastapi import APIRouter, Depends, status

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ClienteController:

    def __init__(self):
        #Router del controlador
        self.router = APIRouter(prefix="/clientes", tags=["Clientes"])

        self.router.post("/", status_code=status.HTTP_201_CREATED)(self.crear)
        self.router.post("/2", status_code=status.HTTP_201_CREATED)(self.crear2)
        self.router.get("/")(self.leer)
        self.router.get("/{cliente_id}")(self.leer_por_id)
        self.router.get("/buscar/{letra}")(self.leer_cliente_letra)
        self.router.put("/{cliente_id}")(self.actualizar)
        self.router.delete("/{cliente_id}")(self.eliminar)
        
    def crear(self, nombre, edad, img_url, db: Session = Depends(get_db)):
        nuevoCliente = ClienteCreate(
            nombre= nombre,
            edad= edad,
            img_url = img_url
        )
        return repo_cliente.crear(db,nuevoCliente)
    
    def crear2(self, cliente: ClienteCreate, db: Session = Depends(get_db)):
        return repo_cliente.crear(db, cliente)

    def leer(self, db:Session = Depends(get_db)):
        return repo_cliente.leer(db)
    
    def leer_por_id(self, cliente_id: int, db:Session = Depends(get_db) ):
        return repo_cliente.leer_por_id(db, cliente_id)

    def leer_cliente_letra(self, letra:str, db:Session = Depends(get_db)):
        return repo_cliente.leer_cliente_letra(db, letra)
    
    def actualizar(self, cliente_id: int, cliente: ClienteCreate, db:Session = Depends(get_db)):
        return repo_cliente.actualizar(db, cliente_id, cliente)
    
    def eliminar(self, cliente_id: int, db:Session = Depends(get_db)):
        return repo_cliente.eliminar(db, cliente_id)