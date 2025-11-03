from db.connection import conectar, cerrar_conexion
from psycopg2 import Error
from models.tipoVehiculos import TipoVehiculo
from models.vehiculos import Vehiculo
from models.pagos import Pago
from datetime import datetime

class Queries:
    # Tipo Vehiculo
    @staticmethod
    def crear_tipo_vehiculo(nombre,tarifa,limite):
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            query = '''
            insert into tipo_vehiculo(nombre,tarifa,limite)
            values (%s,%s,%s)
            returning id
            '''
            cursor.execute(query,(nombre,tarifa,limite))
            tipo_id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()

            print(f"Tipo de vehiculo {nombre} creado con el ID: {tipo_id}")
            return tipo_id
        except Error as e:
            if conn:
                conn.rollback()
            print(f"[Error] Problema al crear un tipo de vehiculo: {e}")
            return None
        finally:
            if conn:
                cerrar_conexion(conn)

    @staticmethod
    def listar_tipos_vehiculos():
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            query = '''
            select * from tipo_vehiculo order by id
            '''
            cursor.execute(query)
            
            tipos = []

            for row in cursor.fetchall():
                tipo = TipoVehiculo(row[0],row[1],row[2],row[3],row[4])
                tipos.append(tipo)

            cursor.close()
            return tipos
        
        except Error as e:
            if conn:
                conn.rollback()
            print(f"[Error] Problema al crear un tipo de vehiculo: {e}")
            return None
        finally:
            if conn:
                cerrar_conexion(conn)


    # Vehiculo
    @staticmethod
    def registrar_entrada(id_tipo_vehiculo,placa, documento, nombre):
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            query = '''
            select t.limite, count(v.id) as cantiad
            from tipo_vehiculo t
            join vehiculos v on v.id_tipovehiculo = t.id and v.estado = true
            where t.id = %s
            GROUP by t.limite
            '''
            cursor.execute(query,(id_tipo_vehiculo,))
            result = cursor.fetchone()
            
            if result:
                limite, cantidad = result
                if cantidad >= limite: print(f"[ERROR] No hay espacio disponible para este tipo de vehiculo."); 
                cursor.close()
                return None
            
            query = '''
            insert into vehiculos(id_tipovehiculo,placa,documento,nombre)
            values (%s,%s,%s,%s)
            returning id
            '''

            cursor.execute(query,(id_tipo_vehiculo,placa,documento,nombre))
            vehiculo_id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()

            print(f"Vehiculo {nombre} registrado con el ID: {vehiculo_id}")
            return vehiculo_id
        except Error as e:
            if conn:
                conn.rollback()
            print(f"[Error] Problema al registrar el vehiculo: {e}")
            return None
        finally:
            if conn:
                cerrar_conexion(conn)

    def listar_vehiculos_activos():
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            query = '''
            select v.id, v.placa, v.nombre, v.documento, v.hora_llegada, t.nombre as tipo
            from vehiculos v
            join  tipo_vehiculo t on v.id_tipovehiculo = t.id and v.estado = true
            order by v.hora_llegada
            '''
            cursor.execute(query)
            vehiculos = cursor.fetchall()
            cursor.close()
            return vehiculos
        
        except Error as e:
            if conn:
                conn.rollback()
            print(f"[Error] Problema al listar vehiculos: {e}")
            return None
        finally:
            if conn:
                cerrar_conexion(conn)

    @staticmethod
    def registrar_salida(vehiculo_id):
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            query = '''
            select *
            from vehiculos v 
            where v.id = %s and v.estado = true
            '''
            cursor.execute(query,(vehiculo_id,))
            result = cursor.fetchone()
            
            if not result:
                print(f"[ERROR] No se encontró el vehiculo con ID: {vehiculo_id}")
                cursor.close()
                return None
            
            hora_salida = datetime.now()
            tiempo_estadia = hora_salida - result[5]
            horas = tiempo_estadia.total_seconds() / 3600
            
            if horas < 1:
                horas = 1  
            
            


        except Error as e:
            if conn:
                conn.rollback()
            print(f"[Error] Problema al registrar el vehiculo: {e}")
            return None
        finally:
            if conn:
                cerrar_conexion(conn)

