#!/usr/bin/env python3

from abc import ABC, abstractmethod

from datetime import datetime
import board
import adafruit_dht
from collections import namedtuple
import logging


class Sensor(object):
    def __init__(self, pins=[]):
        pass

    @property
    @abstractmethod
    def hw(self):
        pass

    @hw.deleter
    @abstractmethod
    def hw(self):
        pass

    @abstractmethod
    def snapshot(self, key):
        pass


def factory(sensor_type, pins=[]):
    class DhtSensor(Sensor):
        def __init__(self, pins=[]):
            self._dht = adafruit_dht.DHT22(pins.pop())

        @property
        def hw(self):
            return self._dht

        @hw.deleter
        def hw(self):
            # TODO test process kill
            del self._dht

        def snapshot(self, key):
            data = self._dht.__getattribute__(key)
            logging.info('Getting %s: %s', key, data)
            return data

        def temperature(self):
            return self.snapshot('temperature')

        def humidity(self):
            return self.snapshot('humidity')

    if str.lower(sensor_type) == 'dht':
        return DhtSensor(pins)
    # TODO

    else:
        return Sensor(pins)
