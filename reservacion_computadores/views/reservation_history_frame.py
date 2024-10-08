import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ReservationHistoryFrame(ttk.Frame):
    def __init__(self, master, user_controller, user_id, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.user_controller = user_controller
        self.user_id = user_id
        self.create_widgets()

    def create_widgets(self):
        # Lista de reservaciones del usuario
        self.reservation_list = tk.Listbox(self, width=70, height=10)
        self.reservation_list.pack(pady=10)

        # Botón para cancelar reservación
        self.cancel_reservation_button = tk.Button(self, text="Cancelar Reservación", command=self.cancel_reservation)
        self.cancel_reservation_button.pack(pady=10)

        self.load_reservations()

    def load_reservations(self):
        reservations = self.user_controller.get_user_reservations(self.user_id)
        self.reservation_list.delete(0, tk.END)
        for reservation in reservations:
            self.reservation_list.insert(tk.END, f"ID: {reservation.id_reservacion} - Computador: {reservation.id_computador} - Inicio: {reservation.fecha_inicio.strftime('%I:%M %p')} - Fin: {reservation.fecha_fin.strftime('%I:%M %p')} - Estado: {reservation.estado}")

    def cancel_reservation(self):
        selected = self.reservation_list.curselection()
        if selected:
            reservation_info = self.reservation_list.get(selected[0])
            reservation_id = int(reservation_info.split(':')[1].split('-')[0].strip())
            success = self.user_controller.cancel_reservation(reservation_id)
            if success:
                messagebox.showinfo("Éxito", "Reservación cancelada correctamente")
                self.load_reservations()
            else:
                messagebox.showerror("Error", "No se pudo cancelar la reservación")
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una reservación para cancelar")