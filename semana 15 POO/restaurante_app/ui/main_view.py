import os
import tkinter as tk
from tkinter import messagebox, ttk

CARPETA_ICONOS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "assets",
    "iconos",
)


class MainView(tk.Frame):
    def __init__(self, master, restaurante_servicio, usuario_actual, al_cerrar_sesion):
        super().__init__(master, bg="#f7fafc")
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion

        self.contenido = None
        self.etiqueta_estado = None
        self.botones_menu = {}
        self.iconos = []

        self.producto_codigo_entry = None
        self.producto_nombre_entry = None
        self.producto_precio_entry = None
        self.producto_categoria_entry = None
        self.tabla_productos = None
        self.tabla_usuarios = None

        self.venta_usuario_combobox = None
        self.venta_producto_combobox = None
        self.tabla_ventas = None

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        self.color_fondo = "#f7fafc"
        self.color_panel = "#ffffff"
        self.color_encabezado = "#1f2a44"
        self.color_texto = "#243447"
        self.color_secundario = "#dbeafe"
        self.color_resaltado = "#2563eb"

        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "MenuActivo.TButton",
            background=self.color_resaltado,
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(12, 10),
            borderwidth=0,
            anchor="w",
        )
        estilo.map("MenuActivo.TButton", background=[("active", "#1d4ed8")])
        estilo.configure(
            "Secundario.TButton",
            background="#1f2a44",
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(10, 7),
            borderwidth=0,
        )
        estilo.map("Secundario.TButton", background=[("active", "#334155")])
        estilo.configure(
            "Accion.TButton",
            background=self.color_resaltado,
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(10, 7),
            borderwidth=0,
        )
        estilo.map("Accion.TButton", background=[("active", "#1d4ed8")])
        estilo.configure(
            "Eliminar.TButton",
            background="#e11d48",
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(10, 7),
            borderwidth=0,
        )
        estilo.map("Eliminar.TButton", background=[("active", "#be123c")])
        estilo.configure(
            "Treeview.Heading",
            background=self.color_secundario,
            foreground=self.color_encabezado,
            font=("Arial", 10, "bold"),
        )

    def cargar_icono(self, nombre):
        try:
            ruta = os.path.join(CARPETA_ICONOS, f"{nombre}.png")
            icono = tk.PhotoImage(file=ruta)
            self.iconos.append(icono)
            return icono
        except Exception:
            return None

    def construir_interfaz(self):
        frame_sidebar = tk.Frame(self, bg=self.color_encabezado, width=200, padx=16, pady=18)
        frame_sidebar.pack(side="left", fill="both", expand=True)
        frame_sidebar.pack_propagate(False)

        tk.Label(
            frame_sidebar,
            text="RESTAURANTE",
            bg=self.color_encabezado,
            fg="#ffffff",
            font=("Arial", 17, "bold"),
        ).pack(anchor="w", pady=(0, 8))

        tk.Label(
            frame_sidebar,
            text=self.usuario_actual.nombre,
            bg=self.color_encabezado,
            fg="#dbeafe",
            font=("Arial", 10),
            wraplength=150,
            justify="left",
        ).pack(anchor="w", pady=(0, 24))

        self.crear_boton_menu(frame_sidebar, "Inicio", self.mostrar_inicio, "inicio")
        self.crear_boton_menu(frame_sidebar, "Usuarios", self.mostrar_usuarios, "usuarios")
        self.crear_boton_menu(frame_sidebar, "Productos", self.mostrar_productos, "productos")
        self.crear_boton_menu(frame_sidebar, "Ventas", self.mostrar_ventas, "ventas")

        tk.Frame(frame_sidebar, bg=self.color_encabezado).pack(fill="both", expand=True)

        self.crear_boton_cerrar(frame_sidebar)

        frame_principal = tk.Frame(self, bg=self.color_fondo)
        frame_principal.pack(side="left", fill="both", expand=True)

        self.contenido = tk.Frame(frame_principal, bg=self.color_fondo, padx=28, pady=24)
        self.contenido.pack(fill="both", expand=True)

        barra_estado = tk.Frame(frame_principal, bg=self.color_secundario, padx=18, pady=8)
        barra_estado.pack(fill="x", side="bottom")

        self.etiqueta_estado = tk.Label(
            barra_estado,
            bg=self.color_secundario,
            fg=self.color_texto,
            font=("Arial", 10),
        )
        self.etiqueta_estado.pack(side="left")

        self.mostrar_inicio()

    def crear_boton_menu(self, contenedor, texto, comando, icono_nombre):
        icono = self.cargar_icono(icono_nombre)
        boton = tk.Button(
            contenedor,
            text=f"  {texto}",
            command=comando,
            bg=self.color_encabezado,
            fg="#ffffff",
            activebackground="#334155",
            activeforeground="#ffffff",
            relief="flat",
            anchor="w",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=9,
            cursor="hand2",
            image=icono,
            compound="left",
        )
        boton.pack(fill="x", pady=(0, 8))
        self.botones_menu[texto] = boton

    def crear_boton_cerrar(self, contenedor):
        icono = self.cargar_icono("cerrar")
        tk.Button(
            contenedor,
            text="  Cerrar sesion",
            command=self.cerrar_sesion,
            bg="#e11d48",
            fg="#ffffff",
            activebackground="#be123c",
            activeforeground="#ffffff",
            relief="flat",
            anchor="w",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=9,
            cursor="hand2",
            image=icono,
            compound="left",
        ).pack(fill="x", pady=(16, 0))

    def marcar_seccion(self, seccion):
        for texto, boton in self.botones_menu.items():
            if texto == seccion:
                boton.configure(bg=self.color_resaltado, activebackground="#1d4ed8")
            else:
                boton.configure(bg=self.color_encabezado, activebackground="#334155")

    def limpiar_contenido(self):
        assert self.contenido is not None
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def actualizar_barra_estado(self):
        assert self.etiqueta_estado is not None
        self.etiqueta_estado.config(
            text=(
                f"Productos: {self.restaurante_servicio.cantidad_productos()} | "
                f"Usuarios: {self.restaurante_servicio.cantidad_usuarios()} | "
                f"Ventas: {self.restaurante_servicio.cantidad_ventas()} | "
                "Datos JSON locales"
            )
        )

    def mostrar_inicio(self):
        self.marcar_seccion("Inicio")
        self.limpiar_contenido()
        self.actualizar_barra_estado()

        assert self.contenido is not None

        tk.Label(
            self.contenido,
            text="Panel principal",
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 20, "bold"),
        ).pack(anchor="w", pady=(0, 8))

        tk.Label(
            self.contenido,
            text="Consulte usuarios, gestione productos y registre ventas desde el menu lateral.",
            bg=self.color_fondo,
            fg=self.color_texto,
            font=("Arial", 12),
        ).pack(anchor="w", pady=(0, 22))

        resumen = tk.Frame(self.contenido, bg=self.color_fondo)
        resumen.pack(fill="x")
        self.crear_tarjeta_resumen(resumen, "Usuarios registrados", self.restaurante_servicio.cantidad_usuarios())
        self.crear_tarjeta_resumen(resumen, "Productos registrados", self.restaurante_servicio.cantidad_productos())
        self.crear_tarjeta_resumen(resumen, "Ventas registradas", self.restaurante_servicio.cantidad_ventas())

    def crear_tarjeta_resumen(self, contenedor, titulo, valor):
        tarjeta = tk.Frame(contenedor, bg=self.color_panel, padx=18, pady=16)
        tarjeta.pack(side="left", fill="x", expand=True, padx=(0, 14))

        tk.Label(
            tarjeta,
            text=titulo,
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")
        tk.Label(
            tarjeta,
            text=str(valor),
            bg=self.color_panel,
            fg=self.color_resaltado,
            font=("Arial", 24, "bold"),
        ).pack(anchor="w", pady=(8, 0))

    def mostrar_usuarios(self):
        self.marcar_seccion("Usuarios")
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_titulo_seccion("Usuarios registrados")
        listado = self.crear_listado(self.contenido, "Consulta de usuarios")
        self.tabla_usuarios = self.crear_tabla(
            listado,
            ("identificador", "nombre", "usuario"),
            ("Identificador", "Nombre", "Usuario"),
        )
        self.refrescar_usuarios()

    def refrescar_usuarios(self):
        assert self.tabla_usuarios is not None
        self.limpiar_tabla(self.tabla_usuarios)
        for usuario in self.restaurante_servicio.listar_usuarios():
            self.tabla_usuarios.insert(
                "",
                tk.END,
                values=(usuario.identificador, usuario.nombre, usuario.usuario),
            )
        self.actualizar_barra_estado()

    def mostrar_productos(self):
        self.marcar_seccion("Productos")
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_titulo_seccion("Gestion de productos")

        cuerpo = tk.Frame(self.contenido, bg=self.color_fondo)
        cuerpo.pack(fill="both", expand=True)
        cuerpo.grid_columnconfigure(1, weight=1)
        cuerpo.grid_rowconfigure(0, weight=1)

        formulario = tk.LabelFrame(
            cuerpo,
            text="Datos del producto",
            bg=self.color_panel,
            fg=self.color_encabezado,
            font=("Arial", 10, "bold"),
            padx=14,
            pady=14,
        )
        formulario.grid(row=0, column=0, sticky="n", padx=(0, 18))

        self.producto_codigo_entry = self.crear_campo(formulario, "Codigo", 0)
        self.producto_nombre_entry = self.crear_campo(formulario, "Nombre", 1)
        self.producto_precio_entry = self.crear_campo(formulario, "Precio", 2)
        self.producto_categoria_entry = self.crear_campo(formulario, "Categoria", 3)

        acciones = tk.Frame(formulario, bg=self.color_panel)
        acciones.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(12, 0))

        botones = (
            ("Registrar", self.registrar_producto, "Accion.TButton"),
            ("Cargar por codigo", self.cargar_producto_en_formulario, "Secundario.TButton"),
            ("Actualizar", self.actualizar_producto, "Accion.TButton"),
            ("Eliminar", self.eliminar_producto, "Eliminar.TButton"),
            ("Limpiar", self.limpiar_formulario_producto, "Secundario.TButton"),
        )

        for texto, comando, estilo in botones:
            ttk.Button(
                acciones,
                text=texto,
                command=comando,
                style=estilo,
            ).pack(fill="x", pady=(0, 7))

        listado = self.crear_listado(cuerpo, "Productos registrados", usar_grid=True)
        self.tabla_productos = self.crear_tabla(
            listado,
            ("codigo", "nombre", "precio", "categoria"),
            ("Codigo", "Nombre", "Precio", "Categoria"),
        )
        self.refrescar_productos()

    def obtener_datos_producto(self):
        assert self.producto_codigo_entry is not None
        assert self.producto_nombre_entry is not None
        assert self.producto_precio_entry is not None
        assert self.producto_categoria_entry is not None

        return (
            self.producto_codigo_entry.get(),
            self.producto_nombre_entry.get(),
            self.producto_precio_entry.get(),
            self.producto_categoria_entry.get(),
        )

    def registrar_producto(self):
        try:
            self.restaurante_servicio.registrar_producto(*self.obtener_datos_producto())
            self.limpiar_formulario_producto()
            self.refrescar_productos()
            messagebox.showinfo("Productos", "Producto registrado correctamente.")
        except ValueError as error:
            messagebox.showerror("Productos", str(error))

    def cargar_producto_en_formulario(self):
        assert self.producto_codigo_entry is not None
        assert self.producto_nombre_entry is not None
        assert self.producto_precio_entry is not None
        assert self.producto_categoria_entry is not None

        producto = self.restaurante_servicio.buscar_producto_por_codigo(self.producto_codigo_entry.get())
        if producto is None:
            messagebox.showerror("Productos", "No existe un producto con ese codigo.")
            return

        self.limpiar_formulario_producto()
        self.producto_codigo_entry.insert(0, producto.codigo)
        self.producto_nombre_entry.insert(0, producto.nombre)
        self.producto_precio_entry.insert(0, str(producto.precio))
        self.producto_categoria_entry.insert(0, producto.categoria)

    def actualizar_producto(self):
        try:
            self.restaurante_servicio.actualizar_producto(*self.obtener_datos_producto())
            self.refrescar_productos()
            messagebox.showinfo("Productos", "Producto actualizado correctamente.")
        except ValueError as error:
            messagebox.showerror("Productos", str(error))

    def eliminar_producto(self):
        assert self.producto_codigo_entry is not None

        try:
            self.restaurante_servicio.eliminar_producto(self.producto_codigo_entry.get())
            self.limpiar_formulario_producto()
            self.refrescar_productos()
            messagebox.showinfo("Productos", "Producto eliminado correctamente.")
        except ValueError as error:
            messagebox.showerror("Productos", str(error))

    def limpiar_formulario_producto(self):
        for entrada in (
            self.producto_codigo_entry,
            self.producto_nombre_entry,
            self.producto_precio_entry,
            self.producto_categoria_entry,
        ):
            assert entrada is not None
            entrada.delete(0, tk.END)

    def refrescar_productos(self):
        assert self.tabla_productos is not None

        self.limpiar_tabla(self.tabla_productos)
        for producto in self.restaurante_servicio.listar_productos():
            self.tabla_productos.insert(
                "",
                tk.END,
                values=(producto.codigo, producto.nombre, producto.precio, producto.categoria),
            )

        self.actualizar_barra_estado()

    def mostrar_ventas(self):
        self.marcar_seccion("Ventas")
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_titulo_seccion("Registro de ventas")

        cuerpo = tk.Frame(self.contenido, bg=self.color_fondo)
        cuerpo.pack(fill="both", expand=True)
        cuerpo.grid_columnconfigure(1, weight=1)
        cuerpo.grid_rowconfigure(0, weight=1)

        formulario = tk.LabelFrame(
            cuerpo,
            text="Nueva venta",
            bg=self.color_panel,
            fg=self.color_encabezado,
            font=("Arial", 10, "bold"),
            padx=14,
            pady=14,
        )
        formulario.grid(row=0, column=0, sticky="n", padx=(0, 18))

        tk.Label(
            formulario,
            text="Usuario",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 10, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8), padx=(0, 10))
        self.venta_usuario_combobox = ttk.Combobox(
            formulario,
            width=26,
            state="readonly",
            font=("Arial", 10),
        )
        self.venta_usuario_combobox.grid(row=0, column=1, sticky="ew", pady=(0, 8))

        tk.Label(
            formulario,
            text="Producto",
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 10, "bold"),
        ).grid(row=1, column=0, sticky="w", pady=(0, 8), padx=(0, 10))
        self.venta_producto_combobox = ttk.Combobox(
            formulario,
            width=26,
            state="readonly",
            font=("Arial", 10),
        )
        self.venta_producto_combobox.grid(row=1, column=1, sticky="ew", pady=(0, 8))

        ttk.Button(
            formulario,
            text="Registrar venta",
            command=self.registrar_venta,
            style="Accion.TButton",
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(16, 0))

        listado = self.crear_listado(cuerpo, "Ventas registradas", usar_grid=True)
        self.tabla_ventas = self.crear_tabla(
            listado,
            ("identificador", "identificador_usuario", "codigo_producto", "fecha"),
            ("ID", "Usuario", "Producto", "Fecha"),
        )

        self.refrescar_combos_venta()
        self.refrescar_ventas()

    def refrescar_combos_venta(self):
        assert self.venta_usuario_combobox is not None
        assert self.venta_producto_combobox is not None

        self.venta_usuario_combobox["values"] = [
            f"{usuario.identificador} - {usuario.nombre}"
            for usuario in self.restaurante_servicio.listar_usuarios()
        ]
        self.venta_producto_combobox["values"] = [
            f"{producto.codigo} - {producto.nombre}"
            for producto in self.restaurante_servicio.listar_productos()
        ]

        if self.venta_usuario_combobox["values"]:
            self.venta_usuario_combobox.current(0)
        if self.venta_producto_combobox["values"]:
            self.venta_producto_combobox.current(0)

    def registrar_venta(self):
        assert self.venta_usuario_combobox is not None
        assert self.venta_producto_combobox is not None

        seleccion_usuario = self.venta_usuario_combobox.get()
        seleccion_producto = self.venta_producto_combobox.get()

        if not seleccion_usuario or not seleccion_producto:
            messagebox.showerror("Ventas", "Seleccione un usuario y un producto.")
            return

        identificador_usuario = seleccion_usuario.split(" - ")[0].strip()
        codigo_producto = seleccion_producto.split(" - ")[0].strip()

        try:
            self.restaurante_servicio.registrar_venta(identificador_usuario, codigo_producto)
            self.refrescar_ventas()
            messagebox.showinfo("Ventas", "Venta registrada correctamente.")
        except ValueError as error:
            messagebox.showerror("Ventas", str(error))

    def refrescar_ventas(self):
        assert self.tabla_ventas is not None

        self.limpiar_tabla(self.tabla_ventas)
        for venta in self.restaurante_servicio.listar_ventas():
            self.tabla_ventas.insert(
                "",
                tk.END,
                values=(venta.identificador, venta.identificador_usuario, venta.codigo_producto, venta.fecha),
            )

        self.actualizar_barra_estado()

    def crear_titulo_seccion(self, texto):
        assert self.contenido is not None
        tk.Label(
            self.contenido,
            text=texto,
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 20, "bold"),
        ).pack(anchor="w", pady=(0, 16))

    def crear_campo(self, contenedor, etiqueta, fila):
        tk.Label(
            contenedor,
            text=etiqueta,
            bg=self.color_panel,
            fg=self.color_texto,
            font=("Arial", 10, "bold"),
        ).grid(row=fila, column=0, sticky="w", pady=(0, 8), padx=(0, 10))

        entrada = tk.Entry(contenedor, width=28, font=("Arial", 10))
        entrada.grid(row=fila, column=1, sticky="ew", pady=(0, 8))
        return entrada

    def crear_listado(self, contenedor, titulo, usar_grid=False):
        listado = tk.LabelFrame(
            contenedor,
            text=titulo,
            bg=self.color_panel,
            fg=self.color_encabezado,
            font=("Arial", 10, "bold"),
            padx=12,
            pady=12,
        )

        if usar_grid:
            listado.grid(row=0, column=1, sticky="nsew")
        else:
            listado.pack(fill="both", expand=True)

        return listado

    def crear_tabla(self, contenedor, columnas, encabezados):
        frame_tabla = tk.Frame(contenedor, bg=self.color_panel)
        frame_tabla.pack(fill="both", expand=True)

        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=12)
        barra = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=barra.set)

        for columna, encabezado in zip(columnas, encabezados):
            tabla.heading(columna, text=encabezado)
            tabla.column(columna, width=150, anchor="w")

        tabla.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")
        return tabla

    def limpiar_tabla(self, tabla):
        for item in tabla.get_children():
            tabla.delete(item)

    def cerrar_sesion(self):
        self.al_cerrar_sesion()
