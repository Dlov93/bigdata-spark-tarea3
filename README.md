# bigdata-spark-tarea3

# Procesamiento de Datos con Apache Spark y Kafka

## Descripción

Este proyecto implementa un sistema de procesamiento de datos utilizando Apache Spark y Apache Kafka, combinando procesamiento batch y en tiempo real (streaming).

Se utiliza un conjunto de datos de activos de información de datos abiertos de Bogotá.

---

## Tecnologías utilizadas

- Apache Spark
- Apache Kafka
- Python

---

## Archivos del proyecto

- batch.py → Procesamiento de datos históricos (batch)
- streaming.py → Procesamiento en tiempo real
- producer.py → Simulación de datos en tiempo real

---

## Funcionamiento del sistema

1. El archivo CSV contiene los datos originales
2. producer.py envía los datos a Kafka
3. Kafka actúa como intermediario
4. streaming.py consume y procesa los datos en tiempo real
5. batch.py analiza los datos históricos

---

## Requisitos

- Python 3
- Apache Spark
- Apache Kafka

---

## Ejecución paso a paso

### 1. Iniciar Zookeeper
/opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties
### 2. Inicia KAFKA
/opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties
### tiene que estar creado el Topic: 
/opt/Kafka/bin/kafka-topics.sh --create \
--bootstrap-server localhost:9092 \
--replication-factor 1 \
--partitions 1 \
--topic topic_tarea3
### 3.Ejecutar Spark Streaming
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 streaming.py
### 4. Ejecutamos el producto
python3 producer.py
### 5. Ejecutar procesamiento batch
spark-submit batch.py

Autor: Diana L. Ocampo Vargas
Estudiante Ing. Sistemas
