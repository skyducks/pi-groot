from datetime import datetime
import board
import adafruit_dht
from collections import namedtuple
import logging

DhtData = namedtuple('DHT', ('temperature', 'humidity', 'timestamp'))

# TODO class Nature


def init():
    global dht_device
    dht_device = adafruit_dht.DHT22(board.D7)


def collect_from_dht():
    # REF https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        data = DhtData(temperature_c, humidity, datetime.now())
        logging.info(data)
        return data
    except RuntimeError as e:
        logging.error(e.args[0])
