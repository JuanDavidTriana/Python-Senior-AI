from interfaces.iPago import InterfacePago
from database.database import get_connection

class PagoRepository(InterfacePago):
    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()
    
    def obtener_pagos(self):
        query = '''
        SELECT * FROM pagos;
        '''
        self.cur.execute(query)
        return self.cur.fetchall()