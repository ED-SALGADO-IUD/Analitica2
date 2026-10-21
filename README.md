# AE2 - Manejo de archivos CSV, JSON y TXT

Proyecto de Python coordinado desde Jupyter Notebook. Se cargan registros locales, se modifica un valor en cada formato, se guardan archivos nuevos y se genera `resumen.txt` con los resultados efectivos.

## Estructura

- `manejador_csv.py`: lectura con `csv.reader`, actualización de valores y escritura con `csv.writer`.
- `manejador_json.py`: lectura con `json.load`, actualización y escritura con `json.dump`.
- `generador_resumen_txt.py`: generación del resumen con los resultados de las clases.
- `actividad_ae2.ipynb`: ejecución y verificación de cada paso.
- `datos/`: originales, versiones modificadas y resumen.

## Datos y fuentes

**CSV:** [a4n9i/iris-tabular - iris.csv](https://huggingface.co/datasets/a4n9i/iris-tabular/blob/main/iris.csv)  
Archivo: https://huggingface.co/datasets/a4n9i/iris-tabular/resolve/main/iris.csv

**JSON:** [logiover/naukri-job-scraper-sample-data - sample.json](https://huggingface.co/datasets/logiover/naukri-job-scraper-sample-data/blob/main/sample.json)  
Archivo: https://huggingface.co/datasets/logiover/naukri-job-scraper-sample-data/resolve/main/sample.json

**Datos locales de demostración:** el CSV incluido contiene las cinco filas visibles de la fuente. El JSON incluido contiene dos registros ilustrativos, no el archivo completo de Hugging Face. Para realizar la entrega conforme a la instrucción de descarga manual, descarga ambos archivos desde las URL anteriores y reemplaza `datos/iris_original.csv` y `datos/empleos_original.json` antes de volver a ejecutar el notebook. Conserva ambos originales sin editar. El notebook se ha preparado para funcionar con ambos conjuntos.

## Ejecución

1. Instala Python 3.9+ y Jupyter Notebook: `python -m pip install notebook nbclient ipykernel`.
2. Entra en la carpeta `AE2`.
3. Ejecuta `jupyter notebook` y abre `actividad_ae2.ipynb`.
4. Selecciona **Kernel > Restart & Run All**.
5. Verifica las salidas en `datos/iris_modificado.csv`, `datos/empleos_modificado.json` y `datos/resumen.txt`.

Los archivos originales nunca se sobrescriben. La única dependencia adicional es Jupyter; las clases utilizan la biblioteca estándar de Python.
