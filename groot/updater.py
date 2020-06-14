import time
import sensors
from elasticsearch import Elasticsearch
import logging

logging.basicConfig(level=logging.INFO)
es = Elasticsearch(["192.168.2.1"])

if __name__ == "__main__":
    sensors.init()
    id = 1
    while True:
        try:
            data = sensors.collect_from_dht()
            res = es.index(index="weather", id=id,
                           body=data._asdict())
            id = id + 1
        except AttributeError:
            continue
        time.sleep(0.2)
