#!/usr/bin/env python3

from elasticsearch import Elasticsearch
import threading

# ------------------------------------------------------------
# REF Thread-related stuff
# https://github.com/python/cpython/blob/master/Lib/logging/__init__.py

_lock = threading.RLock()


def _acquireLock():
    """
    Acquire the module-level lock for serializing access to shared data.

    This should be released with _releaseLock().
    """
    if _lock:
        _lock.acquire()


def _releaseLock():
    """
    Release the module-level lock acquired by calling _acquireLock().
    """
    if _lock:
        _lock.release()
# ------------------------------------------------------------


class Streamer():
    def __init__(self, host=None, index_prefix=None):
        self._es = Elasticsearch([host])
        self._index_prefix = index_prefix()

    @property
    def host(self):
        return self._es

    @host.setter
    def host(self, host):
        self._es = Elasticsearch([host])

    @property
    def index_prefix(self):
        return self._index_prefix

    @index_prefix.setter
    def index_prefix(self, index_prefix):
        self._index_prefix = index_prefix


root = Streamer()


def basicConfig(**kwargs):
    try:
        host = kwargs.pop('host', '127.0.0.1')
        index_prefix = kwargs.pop('index-prefix', '')
        root.host = host
        root.index_prefix = index_prefix
    except UnboundLocalError:
        root = Streamer(host, index_prefix)
    finally:
        _releaseLock()
