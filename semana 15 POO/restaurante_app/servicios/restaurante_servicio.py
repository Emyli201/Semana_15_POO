import os
from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self, carpeta_datos):
        self.carpeta_datos = carpeta_datos
        self.archivo_servicio = ArchivoServicio(carpeta_datos)
        self.usuarios = []
        self.productos = []
        self.ventas = []
        self.cargar_datos()

    def cargar_datos(self):
        usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
        productos_json = self.archivo_servicio.leer_json("productos.json")
        ventas_json = self.archivo_servicio.leer_json("ventas.json")

        self.usuarios = [
            Usuario(
                identificador=u.get("identificador", ""),
                nombre=u.get("nombre", ""),
                usuario=u.get("usuario", ""),
                contrasena=u.get("contrasena", ""),
            )
            for u in usuarios_json
        ]

        self.productos = [
            Producto(
                codigo=p.get("codigo", ""),
                nombre=p.get("nombre", ""),
                precio=p.get("precio", 0),
                categoria=p.get("categoria", ""),
            )
            for p in productos_json
        ]

        self.ventas = [
            Venta(
                identificador=v.get("identificador", ""),
                identificador_usuario=v.get("identificador_usuario", ""),
                codigo_producto=v.get("codigo_producto", ""),
                fecha=v.get("fecha", ""),
            )
            for v in ventas_json
        ]

    # ------------------------- USUARIOS -------------------------

    def listar_usuarios(self):
        return self.usuarios

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def buscar_usuario_por_identificador(self, identificador):
        for usuario in self.usuarios:
            if usuario.identificador == identificador:
                return usuario
        return None

    def buscar_usuario_por_credenciales(self, usuario, contrasena):
        for u in self.usuarios:
            if u.usuario == usuario and u.contrasena == contrasena:
                return u
        return None

    def validar_acceso(self, usuario, contrasena):
        return self.buscar_usuario_por_credenciales(usuario, contrasena)

    # ------------------------- PRODUCTOS -------------------------

    def listar_productos(self):
        return self.productos

    def cantidad_productos(self):
        return len(self.productos)

    def buscar_producto_por_codigo(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar_producto(self, codigo, nombre, precio, categoria):
        if not codigo or not nombre or not precio or not categoria:
            raise ValueError("Todos los campos del producto son obligatorios.")

        if self.buscar_producto_por_codigo(codigo) is not None:
            raise ValueError("Ya existe un producto con ese codigo.")

        try:
            precio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser un numero valido.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        self.productos.append(
            Producto(codigo=codigo, nombre=nombre, precio=precio, categoria=categoria)
        )
        self.guardar_productos()

    def actualizar_producto(self, codigo, nombre, precio, categoria):
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            raise ValueError("No existe un producto con ese codigo.")

        if not nombre or not precio or not categoria:
            raise ValueError("Todos los campos del producto son obligatorios.")

        try:
            precio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser un numero valido.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        producto.nombre = nombre
        producto.precio = precio
        producto.categoria = categoria
        self.guardar_productos()

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            raise ValueError("No existe un producto con ese codigo.")

        self.productos.remove(producto)
        self.guardar_productos()

    def guardar_productos(self):
        datos = [
            {
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "categoria": producto.categoria,
            }
            for producto in self.productos
        ]
        self.archivo_servicio.guardar_json("productos.json", datos)

    # ------------------------- VENTAS -------------------------

    def listar_ventas(self):
        return self.ventas

    def cantidad_ventas(self):
        return len(self.ventas)

    def registrar_venta(self, identificador_usuario, codigo_producto):
        usuario = self.buscar_usuario_por_identificador(identificador_usuario)
        if usuario is None:
            raise ValueError("El usuario seleccionado no existe.")

        producto = self.buscar_producto_por_codigo(codigo_producto)
        if producto is None:
            raise ValueError("El producto seleccionado no existe.")

        numero = len(self.ventas) + 1
        identificador = f"V{numero:03d}"
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.ventas.append(
            Venta(
                identificador=identificador,
                identificador_usuario=identificador_usuario,
                codigo_producto=codigo_producto,
                fecha=fecha,
            )
        )
        self.guardar_ventas()

    def guardar_ventas(self):
        datos = [
            {
                "identificador": venta.identificador,
                "identificador_usuario": venta.identificador_usuario,
                "codigo_producto": venta.codigo_producto,
                "fecha": venta.fecha,
            }
            for venta in self.ventas
        ]
        self.archivo_servicio.guardar_json("ventas.json", datos)
