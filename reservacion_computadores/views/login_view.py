import tkinter as tk
from tkinter import messagebox
from reservacion_computadores.controllers.auth_controller import AuthController

class LoginView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.auth_controller = AuthController()

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.password_label = tk.Label(self, text="Contraseña:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Iniciar Sesión", command=self.login)
        self.login_button.pack()

        print("LoginView inicializada")

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        try:
            user = self.auth_controller.login(email, password)
            if user:
                messagebox.showinfo("Éxito", f"Bienvenido, {user.nombre}!")
                print(f"Usuario {user.nombre} ha iniciado sesión")
                if user.rol == 'administrador':
                    self.master.show_admin_view(user)
                else:
                    self.master.show_user_view(user)
            else:
                messagebox.showerror("Error", "Credenciales inválidas")
                print("Intento de inicio de sesión fallido")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
            print(f"Error durante el inicio de sesión: {e}")