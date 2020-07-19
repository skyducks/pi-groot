#!/usr/bin/env python3

from abc import ABC, abstractmethod
from datetime import datetime
from groot import hardware
import RPi.GPIO as GPIO
import adafruit_dht
from collections import namedtuple
import logging
import psutil


class Sensor(object):
    def __init__(self, pins=[]):
        self._pins = pins

    @property
    def pins(self):
        return self._pins

    @abstractmethod
    def snapshot(self, key):
        pass


Nature = namedtuple('Nature', ['value', 'unit'])


def factory(sensor_type, pins=[]):
    class DhtSensor(Sensor):
        def __init__(self, pins=[]):
            super(DhtSensor, self).__init__(pins)
            for proc in psutil.process_iter():
                if proc.name() == 'libgpiod_pulsein':
                    proc.kill()
                    logging.debug(
                        'libgpiod_pulsei process PID %d was killed.' % proc.pid)
                    break
            self._hw = adafruit_dht.DHT22(pins[0])
            hardware.nature['temperature'] = self.temperature
            hardware.nature['humidity'] = self.humidity

        def snapshot(self, key):
            data = self._hw.__getattribute__(key)
            logging.debug('Getting %s: %s', key, data)
            return data

        def temperature(self):
            data = self.snapshot('temperature')
            return Nature(data, 'C')

        def humidity(self):
            data = self.snapshot('humidity')
            return Nature(data, '%')

    class LightSensor(Sensor):
        def __init__(self, pins=[]):
            super(LightSensor, self).__init__(pins)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pins[0], GPIO.IN)
            hardware.nature['light'] = self.light

        def snapshot(self, key=None):
            return GPIO.input(self.pins[0])

        def light(self):
            data = self.snapshot()
            return Nature(data, '')

    if str.lower(sensor_type) == 'dht':
        return DhtSensor(pins)
    elif str.lower(sensor_type) == 'light':
        return LightSensor(pins)
    else:
        return Sensor(pins)
