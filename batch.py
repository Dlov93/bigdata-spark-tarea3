from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BatchBogota").getOrCreate()

#cargamos el archivo csv
df = spark.read.csv("datos.csv", header=True, inferSchema=True)
#Mostramos la estructura del  dataset
df.printSchema()
#Mostramos las primera 5 filas
df.show(5)
#Limpieza de datos , eliminamos filas ocn valores nulos
df = df.dropna()
#hacemos un pequeño analisis, cantidad de registros por entidad
df.groupBy("Nombre de la Entidad").count().show()
#contar registros por tipo de activos
df.groupBy("Tipo de Activo").count().show()
#Mostrar estadisticas generales
df.describe().show()
#finalizamos la sesion de spark
spark.stop()
