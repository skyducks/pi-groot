#!/usr/bin/env python3

from collections import namedtuple
from groot import hardware, streaming
import logging


def init(**kwargs):
    pass


def observe():
    data = dict()
    for key, value in hardware.nature.items():
        try:
            v = value()
            logging.info('{}: {} {}'.format(key, *v))
            if v.value:
                data[key] = v.value
        except RuntimeError as e:
            logging.error('Cannot parse %s. %s', key, e)

    streaming.index(data)