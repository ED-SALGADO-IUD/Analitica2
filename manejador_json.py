import json
from pathlib import Path


class ManejadorJSON:
    def __init__(self):
        self.registros = []
        self.cambios = []

    def importar(self, ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
        if not isinstance(contenido, list) or not all(isinstance(fila, dict) for fila in contenido):
            raise ValueError("Se requiere un JSON con una lista de objetos")
        self.registros = contenido
        self.cambios = []
        return len(self.registros)

    def modificar(self, indice, campo, nuevo_valor):
        if not 0 <= indice < len(self.registros):
            raise IndexError("Índice fuera del rango de registros")
        if campo not in self.registros[indice]:
            raise KeyError(f"Campo no encontrado: {campo}")
        anterior = self.registros[indice][campo]
        self.registros[indice][campo] = nuevo_valor
        cambio = f"Registro {indice + 1}: {campo}, {anterior!r} -> {nuevo_valor!r}"
        self.cambios.append(cambio)
        return cambio

    def guardar(self, ruta):
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(self.registros, archivo, ensure_ascii=False, indent=2)
        return str(ruta)
