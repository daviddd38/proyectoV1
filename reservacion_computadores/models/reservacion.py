from .database import Database
from datetime import datetime

class Reservacion:
    def __init__(self, id_reservacion=None, id_usuario=None, id_computador=None, fecha_inicio=None, fecha_fin=None, estado=None):
        self.id_reservacion = id_reservacion
        self.id_usuario = id_usuario
        self.id_computador = id_computador
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    @staticmethod
    def create(id_usuario, id_computador, fecha_inicio, fecha_fin):
        db = Database()
        db.connect()
        query = "INSERT INTO Reservaciones (id_usuario, id_computador, fecha_inicio, fecha_fin, estado) VALUES (%s, %s, %s, %s, 'activa')"
        cursor = db.execute_query(query, (id_usuario, id_computador, fecha_inicio, fecha_fin))
        new_id = cursor.lastrowid
        db.disconnect()
        return Reservacion(new_id, id_usuario, id_computador, fecha_inicio, fecha_fin, 'activa')

    @staticmethod
    def get_active_by_user(id_usuario):
        db = Database()
        db.connect()
        query = "SELECT * FROM Reservaciones WHERE id_usuario = %s AND estado IN ('activa', 'pendiente')"
        cursor = db.execute_query(query, (id_usuario,))
        reservaciones = [Reservacion(*row) for row in cursor.fetchall()]
        db.disconnect()
        return reservaciones

    @staticmethod
    def get_all_active():
        db = Database()
        db.connect()
        query = "SELECT * FROM Reservaciones WHERE estado IN ('activa', 'pendiente')"
        cursor = db.execute_query(query)
        reservaciones = [Reservacion(*row) for row in cursor.fetchall()]
        db.disconnect()
        return reservaciones

    def update_status(self, new_status):
        db = Database()
        db.connect()
        query = "UPDATE Reservaciones SET estado = %s WHERE id_reservacion = %s"
        db.execute_query(query, (new_status, self.id_reservacion))
        db.disconnect()
        self.estado = new_status

    @staticmethod
    def get_by_id(id_reservacion):
        db = Database()
        db.connect()
        query = "SELECT * FROM Reservaciones WHERE id_reservacion = %s"
        cursor = db.execute_query(query, (id_reservacion,))
        result = cursor.fetchone()
        db.disconnect()
        if result:
            return Reservacion(*result)
        return None

    @staticmethod
    def get_active_by_computer(id_computador):
        db = Database()
        db.connect()
        query = "SELECT * FROM Reservaciones WHERE id_computador = %s AND estado = 'activa' ORDER BY fecha_fin DESC LIMIT 1"
        cursor = db.execute_query(query, (id_computador,))
        result = cursor.fetchone()
        db.disconnect()
        if result:
            return Reservacion(*result)
        return None