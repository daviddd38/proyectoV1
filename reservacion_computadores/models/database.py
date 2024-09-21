import mysql.connector
from reservacion_computadores.config import DB_CONFIG

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor(buffered=True)
            print("Conexión a la base de datos establecida")
        except mysql.connector.Error as err:
            print(f"Error de conexión a la base de datos: {err}")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Conexión a la base de datos cerrada")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return self.cursor
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            self.connection.rollback()
            return None

    def fetch_one(self):
        return self.cursor.fetchone()

    def fetch_all(self):
        return self.cursor.fetchall()