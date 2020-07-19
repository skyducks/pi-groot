#!/usr/bin/env python3

import logging
from elasticsearch import Elasticsearch
from groot import lib
import pytz
from datetime import datetime


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

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        self._prefix = prefix

    def index(self, **kwargs):
        body = kwargs
        body['timestamp'] = datetime.now(self._timezone)
        index_name = '-'.join([self._prefix, datetime.now().strftime(r'%Y.%m.%d')])
        try:
            for handler in self._handlers:
                handler.index(index=index_name, body=body)
        except ConnectionError as e:
            logging.error(e)
            pass

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
        prefix = kwargs.pop('prefix')
        root.prefix = prefix
    except KeyError:
        pass

    try:
        hosts = kwargs.pop('hosts')
        for host in hosts:
            root.addHandler(Elasticsearch(**hosts.get(host)))
    except KeyError:
        logging.error('Cannot find Elasticsearch hosts info')
        pass


def index(**kwargs):
    root.index(**kwargs)
