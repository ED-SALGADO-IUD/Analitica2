## Datos y fuentes

Para el desarrollo de esta actividad se utilizaron dos conjuntos de datos obtenidos de Hugging Face.

### Archivo CSV
- Dataset: Iris Tabular.
- Fuente: https://huggingface.co/datasets/a4n9i/iris-tabular
- Archivo original: `datos/iris_original.csv`
- Archivo modificado: `datos/iris_modificado.csv`

### Archivo JSON
- Dataset: Naukri Job Scraper Sample Data.
- Fuente: https://huggingface.co/datasets/logiover/naukri-job-scraper-sample-data
- Archivo original: `datos/empleos_original.json`
- Archivo modificado: `datos/empleos_modificado.json`

Ambos archivos fueron descargados manualmente de Hugging Face y conservados en su formato original.

Las modificaciones se realizaron mediante clases independientes de Python, coordinadas desde Jupyter Notebook, sin sobrescribir los archivos originales.

Finalmente, se generó `datos/resumen.txt` con las operaciones realizadas, las rutas de los archivos y la cantidad de registros procesados.