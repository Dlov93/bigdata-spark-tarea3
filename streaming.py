# Este proceso simula la ingestión de datos en tiempo real para su análisis
#continuo
from pyspark.sql import SparkSession

#iniicamos la aplicacion

spark = SparkSession.builder.appName("StreamingBogota").getOrCreate()
spark.sparkContext.setLogLevel("WARN")
#configuramos la lectura en tiempo real desde Kafka
df = (spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "topic_tarea3")
    .load())
#convertimos el valor recibido  que esta en binario a texto
data = df.selectExpr("CAST(value AS STRING)")

#mostramos los datos en consola en tiempo real
query = (data.writeStream
    .outputMode("append")
    .format("console")
    .start())
#mantenemos la aplicacion corriendo
query.awaitTermination()
