#!/usr/bin/env python3

from groot import lib
from groot.hardware import sensors


class SensorManager(metaclass=lib.SingletonMeta):
    def __init__(self):
        self._sensors = []

    @property
    def sensors(self):
        return self._sensors


root = SensorManager()


def basicConfig(**kwargs):
    sensors_config = kwargs.pop('sensors')
    for sensor_type, sensor_details in sensors_config.items():
        root.sensors.append(sensors.factory(
            sensor_type, sensor_details.pop('pins')))
    # TODO motors, analog sensors
