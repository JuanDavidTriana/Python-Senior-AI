from database.database import get_connection
from interfaces.iTipoVehiculo import InterfaceTipoVehiculo

class TipoVehiculoRepository(InterfaceTipoVehiculo):
    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def listarTodos(self):
        query = '''
        SELECT * FROM tipo_vehiculo;
        '''
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def listarActivos(self):
        query = '''
        SELECT * FROM tipo_vehiculo WHERE estado = TRUE;
        '''
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def obtenerPorId(self, id_tipovehiculo: int):
        query = '''
        SELECT * FROM tipo_vehiculo WHERE id = %s;
        '''
        self.cur.execute(query, (id_tipovehiculo,))
        return self.cur.fetchone()
    
    def crear(self, nombre: str, tarifa: float, limite: int):
        query = '''
                INSERT INTO tipo_vehiculo (nombre, tarifa, limite) 
                VALUES (%s, %s, %s) 
                RETURNING id;
            '''
        self.cur.execute(query, (nombre, tarifa, limite))
        return self.cur.fetchone()["id"]
    
    def actualizar(self, id_tipovehiculo: int, nombre: str, tarifa: float, limite: int, estado: bool):
        query = '''
                UPDATE tipo_vehiculo 
                SET nombre = %s, tarifa = %s, limite = %s, estado = %s 
                WHERE id = %s
                RETURNING *;
            '''
        self.cur.execute(query, (nombre, tarifa, limite, estado, id_tipovehiculo))
        return self.cur.fetchone()
    
    def cambiarEstado(self, tipo_vehiculo_id: int):
        query = '''
                UPDATE tipo_vehiculo 
                SET estado = NOT estado 
                WHERE id = %s 
                RETURNING estado;
            '''
        self.cur.execute(query, (tipo_vehiculo_id,))
        return self.cur.fetchone()