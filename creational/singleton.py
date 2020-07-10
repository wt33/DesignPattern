"""

Desc:               单例模式(应用:1、资源复用，像数据库连接等关乎性能。 2、统一全局入口)
CreatedOn:          2020/6/17 10:34
Author:             wut
"""

import threading
import time


class Singleton1:
    _exist_instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._exist_instance:
            with cls._lock:
                if not cls._exist_instance:
                    cls._exist_instance = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        return cls._exist_instance


################################


def singleton(cls):
    _instance = {}
    lock = threading.Lock()

    def _singleton(*args, **kwargs):
        with lock:
            if cls not in _instance:
                _instance[cls] = cls(*args, **kwargs)
            return _instance[cls]

    return _singleton


@singleton
class Singleton2:
    def __init__(self):
        time.sleep(1)


###############################

class SingletonType(type):
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not hasattr(cls, "_instance"):
                cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Singleton3(metaclass=SingletonType):
    def __init__(self):
        time.sleep(1)


def test():
    print(id(Singleton1()))


if __name__ == "__main__":
    for i in range(10):
        threading.Thread(target=test).start()
