#!/usr/bin/env python3

from collections import namedtuple

Humidity = namedtuple('Humidity', ['value', 'unit'], defaults=('%'))
Temperature = namedtuple('Temperature', ['value', 'unit'], defaults=('C'))
Light = namedtuple('Light', ['value'])
