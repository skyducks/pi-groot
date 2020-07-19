#!/usr/bin/env python3
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


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
