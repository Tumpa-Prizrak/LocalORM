import sys
import database

sys.dont_write_bytecode = True

db_users = database.Database("configs/users.json")
print(db_users.get_config())
