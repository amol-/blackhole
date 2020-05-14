from multiprocessing.managers import SyncManager

class DBManager(SyncManager):
    pass
DBManager.register("db")

manager = DBManager(("127.0.0.1", 5000), authkey="password")
manager.connect()

current_value = manager.db().get_key("key") or 0
manager.db().set_key("key", current_value + 1)
print("Value", current_value)