class Venta:
    def __init__(self, identificador, identificador_usuario, codigo_producto, fecha):
        self.identificador = identificador
        self.identificador_usuario = identificador_usuario
        self.codigo_producto = codigo_producto
        self.fecha = fecha

    @staticmethod
    def validar_texto(valor, campo):
        if not valor or not valor.strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")
        return valor.strip()

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, valor):
        self._identificador = self.validar_texto(valor, "identificador")

    @property
    def identificador_usuario(self):
        return self._identificador_usuario

    @identificador_usuario.setter
    def identificador_usuario(self, valor):
        self._identificador_usuario = self.validar_texto(valor, "identificador_usuario")

    @property
    def codigo_producto(self):
        return self._codigo_producto

    @codigo_producto.setter
    def codigo_producto(self, valor):
        self._codigo_producto = self.validar_texto(valor, "codigo_producto")

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = self.validar_texto(valor, "fecha")
