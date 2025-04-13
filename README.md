Tarea 3 - Procesamiento de Big Data con Apache Spark

Este proyecto contiene el desarrollo de la Tarea 3 del curso Big Data de la UNAD.

📁 Contenido del repositorio
- procesamiento_batch.py: Código de procesamiento batch de datos del dataset Airbnb NYC.
- simulacion_streaming.py: Código de simulación de llegada de datos en tiempo real (streaming).
- AB_NYC_2019.csv: Dataset original utilizado.
- README.md: Instrucciones y explicación del proyecto.

⚙️ Tecnologías usadas
- Apache Spark 3.3.2
- PySpark
- Google Colab
- Google Drive (para manejo de archivos)
- Python 3.x

🚀 Instrucciones para replicar el proyecto

1. Configurar Google Colab
- Abre Google Colab (https://colab.research.google.com/).
- Crea un nuevo notebook.
- En la primera celda, instala y configura Spark:

Instalación de Spark en Colab:
!apt-get install openjdk-11-jdk-headless -qq > /dev/null
!wget -q https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz
!tar xf spark-3.3.2-bin-hadoop3.tgz
!pip install -q findspark

Configuración de Spark:
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.3.2-bin-hadoop3"

import findspark
findspark.init()

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("Tarea3_BigData").getOrCreate()

2. Subir los archivos a Colab
- Sube los siguientes archivos:
  - procesamiento_batch.py
  - simulacion_streaming.py
  - AB_NYC_2019.csv

Puedes usar:
from google.colab import files
uploaded = files.upload()

3. Ejecutar procesamiento batch
Corre el contenido del archivo procesamiento_batch.py:

%run procesamiento_batch.py

Este script:
- Carga el dataset AB_NYC_2019.csv.
- Limpia datos inválidos (precios <= 0).
- Calcula precio promedio por barrio.
- Guarda los resultados en archivos CSV.

4. Ejecutar simulación de streaming
Corre el contenido del archivo simulacion_streaming.py:

%run simulacion_streaming.py

Este script:
- Simula la llegada de datos de alojamientos en tiempo real.
- Muestra registros uno por uno simulando flujo de datos.
- Procesa y visualiza información en consola.

📊 Resultados obtenidos
- Procesamiento batch exitoso de datos de alojamientos de NYC.
- Cálculo de precios promedios por barrio.
- Simulación de procesamiento de datos en tiempo real.
- Documentación y carga completa en GitHub.

👨‍💻 Autor
Miguel David Saavera Hamburger

📚 Referencias
- Dataset tomado de: New York City Airbnb Open Data (https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)
- Documentación oficial de Apache Spark (https://spark.apache.org/docs/latest/)
- Plataforma educativa UNAD - Curso Big Data
