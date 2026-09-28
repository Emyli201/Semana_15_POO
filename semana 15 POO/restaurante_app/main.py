import os
import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurante App")
        self.geometry("980x620")
        self.minsize(860, 540)

        carpeta_datos = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos")
        self.restaurante_servicio = RestauranteServicio(carpeta_datos)

        self.vista_actual = None
        self.mostrar_login()

    def mostrar_login(self):
        if self.vista_actual is not None:
            self.vista_actual.destroy()

        self.vista_actual = LoginView(
            self,
            self.restaurante_servicio,
            self.mostrar_principal,
        )
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_principal(self, usuario_actual):
        if self.vista_actual is not None:
            self.vista_actual.destroy()

        self.vista_actual = MainView(
            self,
            self.restaurante_servicio,
            usuario_actual,
            self.mostrar_login,
        )
        self.vista_actual.pack(fill="both", expand=True)


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.mainloop()