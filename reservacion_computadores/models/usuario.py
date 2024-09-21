from .database import Database

class Usuario:
    def __init__(self, id_usuario=None, nombre=None, apellido=None, email=None, contrasena=None, rol=None, fecha_creacion=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena
        self.rol = rol
        self.fecha_creacion = fecha_creacion

    @staticmethod
    def get_by_email(email):
        print(f"Buscando usuario con email: {email}")
        db = Database()
        db.connect()
        query = "SELECT * FROM Usuarios WHERE email = %s"
        cursor = db.execute_query(query, (email,))
        if cursor:
            user_data = db.fetch_one()
            db.disconnect()
            if user_data:
                print(f"Usuario encontrado: {user_data[1]} {user_data[2]}")
                return Usuario(*user_data)
        db.disconnect()
        print("Usuario no encontrado")
        return None

    def __str__(self):
        return f"Usuario(id={self.id_usuario}, nombre={self.nombre}, apellido={self.apellido}, email={self.email}, rol={self.rol})"