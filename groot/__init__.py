#!/usr/bin/env python3

from groot import streaming, farmer
import logging


def setup(es_config=None, hw_config=None):
    try:
        streaming.basicConfig(**es_config)
    except Exception as e:
        logging.error('Cannot setup streaming for: %s', es_config)

    try:
        farmer.init(**hw_config)
    except Exception as e:
        logging.error('Cannot load hardware: %s', hw_config)
        raise Exception


def run():
    while True:
        values = farmer.get_around()
