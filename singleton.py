import threading

class Database:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, host, port):
        if not hasattr(self, '_is_init'):
            with self.__lock:
                if not hasattr(self, '_is_init'):
                    self.host = host
                    self.port = port
                    self._is_init = True

    def connection(self):
        print(f'connection in {self.host}, {self.port}')


d1 = Database('126.0.0.1', 5000)
d2 = Database('126.0.0.3', 1000)
d1.connection()
d2.connection()