#!/usr/bin/env python3

import logging
from elasticsearch import Elasticsearch
from groot import lib
import pytz


class Streamer(metaclass=lib.SingletonMeta):
    def __init__(self, timezone=None):
        self._handlers = []
        self._timezone = pytz.timezone(timezone) if timezone else timezone

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        self._timezone = pytz.timezone(timezone)

    def index(self, **kwargs):
        try:
            for handler in self._handlers:
                handler.index(**kwargs)
        except Exception as e:
            logging.error(e)

    def addHandler(self, handler: Elasticsearch):
        if not handler in self._handlers:
            self._handlers.append(handler)


root = Streamer()


def basicConfig(**kwargs):
    try:
        timezone = kwargs.pop('timezone')
        root.timezone = timezone
    except KeyError:
        logging.warning(
            'Cannot parse timezone. Default timezone will be used.')
        pass

    try:
        hosts = kwargs.pop('hosts')
        for host in hosts:
            root.addHandler(Elasticsearch(**hosts.get(host)))
    except KeyError:
        logging.error('Cannot find Elasticsearch hosts info')
        pass
