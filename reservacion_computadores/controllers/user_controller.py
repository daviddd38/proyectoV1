from reservacion_computadores.models.computador import Computador
from reservacion_computadores.models.reservacion import Reservacion
from datetime import datetime

class UserController:
    def get_user_reservations(self, id_usuario):
        return Reservacion.get_active_by_user(id_usuario)

    def get_all_computers(self):
        return Computador.get_all()

    def get_available_computers(self):
        return Computador.get_available()

    def make_reservation(self, id_usuario, id_computador, fecha_inicio, fecha_fin):
        try:
            Reservacion.create(id_usuario, id_computador, fecha_inicio, fecha_fin)
            Computador.update_status(id_computador, "reservado")
            return True
        except Exception as e:
            print(f"Error al crear la reservación: {e}")
            return False

    def cancel_reservation(self, id_reservacion):
        try:
            reservacion = Reservacion.get_by_id(id_reservacion)
            if reservacion:
                reservacion.update_status('cancelada')
                Computador.update_status(reservacion.id_computador, "disponible")
                return True
            return False
        except Exception as e:
            print(f"Error al cancelar la reservación: {e}")
            return False

    def check_and_update_reservations(self):
        now = datetime.now()
        reservations = Reservacion.get_all_active()
        for reservation in reservations:
            if reservation.fecha_fin <= now:
                reservation.update_status('completada')
                Computador.update_status(reservation.id_computador, "disponible")

    def get_computer_status(self, id_computador):
        computer = Computador.get_by_id(id_computador)
        if computer:
            active_reservation = Reservacion.get_active_by_computer(computer.id_computador)
            if active_reservation:
                return "reservado", active_reservation.fecha_fin
            return computer.estado, None
        return None, None