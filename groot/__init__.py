#!/usr/bin/env python3

from groot import streaming, hardware, farmer
import logging


def setup(es_config=None, hw_config=None):
    try:
        streaming.basicConfig(**es_config)
    except Exception:
        logging.error('Cannot setup streaming for: %s', es_config)

    try:
        hardware.basicConfig(**hw_config)
    except Exception as e:
        logging.error('Cannot load hardware: %s', e)
        raise Exception


def run():
    import time
    # TODO
    while True:
        farmer.observe()
        time.sleep(10)
