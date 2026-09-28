import os
import tkinter as tk
from tkinter import messagebox, ttk


class LoginView(tk.Frame):
    def __init__(self, master, restaurante_servicio, al_iniciar_sesion):
        super().__init__(master, bg="#f7fafc")
        self.restaurante_servicio = restaurante_servicio
        self.al_iniciar_sesion = al_iniciar_sesion

        self.usuario_entry = None
        self.contrasena_entry = None

        self.construir_interfaz()

    def construir_interfaz(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Login.TButton",
            background="#9B5278",
            foreground="#000000",
            bordercolor="#9B5278",
            lightcolor="#9B5278",
            darkcolor="#9B5278",
            font=("Arial", 11, "bold"),
            padding=(12, 8),
        )
        estilo.map(
            "Login.TButton",
            background=[("active", "#7d3f60")],
            foreground=[("active", "#000000")],
        )

        contenedor = tk.Frame(self, bg="#f7fafc")
        contenedor.pack(expand=True)

        ruta_logo = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "assets",
            "iconos",
            "logo.png",
        )
        try:
            logo = tk.PhotoImage(file=ruta_logo)
            etiqueta_logo = tk.Label(contenedor, image=logo, bg="#f7fafc")
            etiqueta_logo.image = logo
            etiqueta_logo.pack(pady=(0, 12))
        except Exception:
            pass

        tk.Label(
            contenedor,
            text="RESTAURANTE APP",
            bg="#f7fafc",
            fg="#9B5278",
            font=("Arial", 24, "bold"),
        ).pack(pady=(0, 8))

        tk.Label(
            contenedor,
            text="Inicie sesion para continuar",
            bg="#f7fafc",
            fg="#243447",
            font=("Arial", 12),
        ).pack(pady=(0, 24))

        tarjeta = tk.Frame(contenedor, bg="#ffffff", padx=28, pady=24)
        tarjeta.pack()

        tk.Label(
            tarjeta,
            text="Usuario",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w", pady=(0, 6))
        self.usuario_entry = tk.Entry(tarjeta, width=30, font=("Arial", 11))
        self.usuario_entry.pack(pady=(0, 14))

        tk.Label(
            tarjeta,
            text="Contrasena",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w", pady=(0, 6))
        self.contrasena_entry = tk.Entry(tarjeta, width=30, font=("Arial", 11), show="*")
        self.contrasena_entry.pack(pady=(0, 18))

        ttk.Button(
            tarjeta,
            text="Iniciar sesion",
            command=self.iniciar_sesion,
            style="Login.TButton",
        ).pack(fill="x")

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        if not usuario or not contrasena:
            messagebox.showerror("Acceso", "Ingrese usuario y contrasena.")
            return

        usuario_encontrado = self.restaurante_servicio.validar_acceso(usuario, contrasena)
        if usuario_encontrado is None:
            messagebox.showerror("Acceso", "Credenciales incorrectas.")
            return

        self.al_iniciar_sesion(usuario_encontrado)