import csv
from pathlib import Path


class ManejadorCSV:
    def __init__(self):
        self.encabezados = []
        self.registros = []
        self.cambios = []

    def importar(self, ruta):
        with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.reader(archivo)
            self.encabezados = next(lector)
            self.registros = [dict(zip(self.encabezados, fila)) for fila in lector]
        self.cambios = []
        return len(self.registros)

    def modificar(self, indice, campo, nuevo_valor):
        if campo not in self.encabezados:
            raise KeyError(f"Columna no encontrada: {campo}")
        if not 0 <= indice < len(self.registros):
            raise IndexError("Índice fuera del rango de registros")
        anterior = self.registros[indice][campo]
        self.registros[indice][campo] = str(nuevo_valor)
        cambio = f"Registro {indice + 1}: {campo}, '{anterior}' -> '{nuevo_valor}'"
        self.cambios.append(cambio)
        return cambio

    def guardar(self, ruta):
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            for registro in self.registros:
                escritor.writerow([registro[campo] for campo in self.encabezados])
        return str(ruta)
