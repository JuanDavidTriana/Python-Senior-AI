from database.database import get_connection
from interfaces.iVehiculo import InterfaceVehiculo

class VehiculoRepository(InterfaceVehiculo):
    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def listar(self):
        query = '''
        SELECT * FROM vehiculos;
        '''
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def crear(self, tipoVehiculo:int,placa:str,documento:str,nombre:str):
        query = '''
                INSERT INTO vehiculos (id_tipovehiculo, placa, documento, nombre) 
                VALUES (%s, %s, %s, %s) 
                RETURNING id;
            '''
        self.cur.execute(query,(tipoVehiculo,placa,documento,nombre))
        return self.cur.fetchone()["id"]
    
    def cambiar_estado(self,vehiculo_id: str):
        query = '''
                UPDATE vehiculos 
                SET estado = NOT estado 
                WHERE id = %s 
                RETURNING estado;
            '''
        self.cur.execute(query, (vehiculo_id,))
        return self.cur.fetchone()
    
    def actualizar(self, id_vehiculo: int, id_tipovehiculo: int, placa: str, documento: str, nombre: str, estado: bool):
        query = '''
                UPDATE vehiculos 
                SET id_tipovehiculo = %s, placa = %s, documento = %s, nombre = %s, estado = %s 
                WHERE id = %s
                RETURNING *;
            '''
        self.cur.execute(query, (id_tipovehiculo, placa, documento, nombre, estado, id_vehiculo))
        return self.cur.fetchone()
    
    def eliminar(self, vehiculo_id: int):
        query = '''
            DELETE FROM vehiculos 
            WHERE id = %s
        '''
        self.cur.execute(query, (vehiculo_id,))
        return self.cur.fetchone()