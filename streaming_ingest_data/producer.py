from confluent_kafka import Producer
from config import *
import csv                      
import time   
import json 


def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row 


def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to topic: {msg.topic()}, partition: {msg.partition()}, offset: {msg.offset()}')


def produce_data(bootstrap_servers, topic, file_path):
    producer = Producer({'bootstrap.servers':bootstrap_servers})
    try:
        for row in read_csv(file_path):
            json_row = json.dumps(row)
            producer.produce(topic, value=json_row, callback=delivery_report)
            producer.flush()
            
    except KeyboardInterrupt:
        pass 
    finally:
        producer.flush()
    


if __name__ == "__main__":
    bootstrap_servers = BOOTSTRAP_SERVERS  # Change this to your Kafka broker's address
    topic = TOPIC
    # print(conf)
    file_path = "../data/202201-divvy-tripdata.csv"
    producer = produce_data(bootstrap_servers, topic, file_path)
