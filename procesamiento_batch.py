
# Instalación de Spark (versión que sí descarga)
!apt-get install openjdk-11-jdk-headless -qq > /dev/null
!wget -q https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz
!tar xf spark-3.3.2-bin-hadoop3.tgz
!pip install -q findspark

# Configurar las variables de entorno
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.3.2-bin-hadoop3"

# Inicializar Spark
import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("Tarea3_BigData").getOrCreate()

# Montar Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Leer tu archivo CSV desde tu ubicación personalizada
df = spark.read.csv('/content/drive/MyDrive/Personal/Mis materias/Diplomado + Servicio Social/BIG DATA/3/AB_NYC_2019.csv', header=True, inferSchema=True)

# Mostrar las primeras 5 filas
df.show(5)

# Mostrar las columnas del DataFrame
df.printSchema()

# Eliminar alojamientos donde el precio es 0 o negativo
df_clean = df.filter(df.price > 0)

# Verificar la cantidad de registros después de limpiar
print(f"Número de registros luego de limpiar: {df_clean.count()}")

# Convertir 'price' a número
from pyspark.sql.functions import col
from pyspark.sql.types import DoubleType

df_clean = df_clean.withColumn("price", col("price").cast(DoubleType()))

# Agrupar por neighbourhood_group y calcular promedio
df_avg_price = df_clean.groupBy('neighbourhood_group').avg('price')

# Mostrar resultados
df_avg_price.show()

# Guardar el resultado en una carpeta llamada 'resultados_batch' en tu Drive
output_path = '/content/drive/MyDrive/Personal/Mis materias/Diplomado + Servicio Social/BIG DATA/3/resultados_batch'

# Escribir el archivo CSV
df_avg_price.write.csv(output_path, header=True, mode='overwrite')
