
# Cargar los datos completos de Airbnb NYC
df_stream = spark.read.csv('/content/drive/MyDrive/Personal/Mis materias/Diplomado + Servicio Social/BIG DATA/3/AB_NYC_2019.csv', header=True, inferSchema=True)

# Filtrar datos pequeños como si fueran nuevos datos
df_simulado = df_stream.select("id", "neighbourhood_group", "price").limit(5)

# Mostrar los registros
df_simulado.show(truncate=False)
