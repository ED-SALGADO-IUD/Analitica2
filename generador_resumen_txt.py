from pathlib import Path


class GeneradorResumenTXT:
    def generar(self, ruta, datos_csv, datos_json):
        lineas = ["AE2 - MANEJO DE ARCHIVOS CSV Y JSON", "", "ORIGEN CSV", datos_csv["url"],
                  f"Archivo importado: {datos_csv['origen']}",
                  f"Archivo guardado: {datos_csv['salida']}",
                  f"Registros procesados: {datos_csv['cantidad']}",
                  "Clase: ManejadorCSV", "Métodos: importar, modificar, guardar",
                  "Modificaciones: *" ]
        lineas += [f"  - {c}" for c in datos_csv["cambios"]]
        lineas += ["", "ORIGEN JSON", datos_json["url"],
                   f"Archivo importado: {datos_json['origen']}",
                   f"Archivo guardado: {datos_json['salida']}",
                   f"Registros procesados: {datos_json['cantidad']}",
                   "Clase: ManejadorJSON", "Métodos: importar, modificar, guardar", "Modificaciones: *"]
        lineas += [f"  - {c}" for c in datos_json["cambios"]]
        lineas += ["", "GENERACIÓN TXT", "Clase: GeneradorResumenTXT", "Método: generar", f"Salida: {ruta}"]
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write("\n".join(lineas).replace("Modificaciones: *", "Modificaciones:") + "\n")
        return str(ruta)
