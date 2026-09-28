import json
import os


class ArchivoServicio:
    def __init__(self, carpeta_datos):
        self.carpeta_datos = carpeta_datos
        os.makedirs(self.carpeta_datos, exist_ok=True)

    def ruta_archivo(self, nombre_archivo):
        return os.path.join(self.carpeta_datos, nombre_archivo)

    def leer_json(self, nombre_archivo):
        ruta = self.ruta_archivo(nombre_archivo)
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, OSError):
            return []

    def guardar_json(self, nombre_archivo, datos):
        ruta = self.ruta_archivo(nombre_archivo)
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
