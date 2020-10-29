import os
import sqlite3


def create_db(db_name, schema):
    db_exists = os.path.exists(db_name)
    if db_exists:
        print("База данных существует")
        return
    print("Создаю базу данных...")
    with open(schema, "r") as f:
        schema_f = f.read()
        connection = sqlite3.connect(db_name)
        connection.executescript(schema_f)
        connection.close()


if __name__ == "__main__":
    db_filename = "dhcp_snooping.db"
    schema_filename = "dhcp_snooping_schema.sql"
    create_db(db_filename, schema_filename)
