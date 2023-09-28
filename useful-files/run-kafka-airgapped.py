#!/usr/bin/python3
# Run Kafka consumer and producer in airgapped env
# Prerequisite: pip3 install kafka-1.3.5.tar.gz
# https://pypi.org/project/kafka/

# create a consumer to listen to topic
from kafka import KafkaConsumer
consumer = KafkaConsumer('metrics', bootstrap_servers='[fd03:298c:8dfe:805:3000::1102]:9092')
for msg in consumer:
  print (msg)


# create a producer to write, but could not create new topic
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='[fd03:298c:8dfe:805:3000::1102]:9092')
producer.send('metrics', b'first message')


# doesn't work - kafka.admin is missing
#from kafka.admin import kafkaAdminClient, NewTopic
#admin_client = KafkaAdminClient(
#    bootstrap_servers="[fd03:298c:8dfe:805:3000::1102]:9092", 
#    client_id='test'
#)
#topic_list = []
#topic_list.append(NewTopic(name="OBF_METRICS", num_partitions=1, replication_factor=1))
#admin_client.create_topics(new_topics=topic_list, validate_only=False)


