from confluent_kafka import Consumer, KafkaError
import json 
from config import *

def consume_data(bootstrap_servers, topic):
    conf = {'bootstrap.servers': bootstrap_servers, 'group.id': 'ashraf-supply-chain', 'auto.offset.reset': 'earliest'}
    consumer = Consumer(conf)
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition
                    continue
                else:
                    print(msg.error())
                    # break
            else:
                # Message value and key are raw bytes -- decode if necessary!
                # e.g., convert to utf-8
                print('Received message: {}'.format(msg.value().decode('utf-8')))
 

            break
    except KeyboardInterrupt:
        pass

    finally:
        consumer.close()

if __name__ == "__main__":
    conf ={'bootstrap.servers':BOOTSTRAP_SERVERS,
       'group.id': 'cycle_data',
       'auto.offset.reset': 'earliest'
       }
    print(TOPIC)
    consume_data(BOOTSTRAP_SERVERS, TOPIC)