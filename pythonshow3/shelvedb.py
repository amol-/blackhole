import shelve
import atexit
import threading
from multiprocessing.managers import SyncManager


class KeyManager:
    def __init__(self):  
        self._lock = threading.Lock()      
        self._shelve = shelve.open("./shelve.db", writeback=True)

    def get_key(self, key):
        with self._lock:
            return self._shelve.get(key)

    def set_key(self, key, value):
        with self._lock:
            self._shelve[key] = value

    def close(self):
        self._shelve.close()

keymanager = KeyManager()
atexit.register(keymanager.close)

class DBManager(SyncManager):
    pass
DBManager.register("db", lambda: keymanager)

manager = DBManager(("127.0.0.1", 5000), authkey="password")
print("Listening on port 5000")
manager.get_server().serve_forever()
print("bye")
