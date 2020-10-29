# -*- coding: utf-8 -*-

import sqlite3
import os
import re
from datetime import timedelta, datetime

import yaml
from tabulate import tabulate


def print_data_in_rows(data, active=True):
    data = list(data)
    if data:
        print(
            "\n{active} записи:\n".format(active="Активные" if active else "Неактивные")
        )
        print(tabulate(data))


def parse_dhcp_snoop(filename):
    regex = re.compile("(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)")
    hostname = re.search("(\w+)_dhcp_snooping.txt", filename).group(1)
    with open(filename) as f:
        result = [match.groups() + (hostname,) for match in regex.finditer(f.read())]
    return result


def add_data_to_db(connection, query, data):
    for row in data:
        try:
            with connection:
                connection.execute(query, row)
        except sqlite3.IntegrityError as err:
            print("При добавлении данных:", row, "Возникла ошибка:", err)


def get_db_column_names(db_filename):
    conn = sqlite3.connect(db_filename)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    keys = cursor.execute("select * from dhcp").fetchone().keys()
    keys.remove("active")
    conn.close()
    return keys


def create_db(db_filename, schema_file):
    if os.path.exists(db_filename):
        print("База данных существует")
        return
    conn = sqlite3.connect(db_filename)
    print("Создаю базу данных...")
    with open(schema_file) as f:
        schema = f.read()
    conn.executescript(schema)


def add_data_switches(db_filename, sw_info_files):
    if not os.path.exists(db_filename):
        print("База данных не существует. Перед добавлением данных, ее надо создать")
        return

    conn = sqlite3.connect(db_filename)
    query_switches = "insert into switches values (?,?)"
    for sw_file in sw_info_files:
        with open(sw_file) as f:
            switches = yaml.load(f)
        sw_data = list(switches["switches"].items())
        add_data_to_db(conn, query_switches, sw_data)
    conn.close()


def remove_old_records(conn):
    now = datetime.today().replace(microsecond=0)
    week_ago = str(now - timedelta(days=7))
    query = "delete from dhcp where last_active < ?"
    conn.execute(query, (week_ago,))
    conn.commit()


def add_data(db_filename, data_files):
    if not os.path.exists(db_filename):
        print("База данных не существует. Перед добавлением данных, ее надо создать")
        return
    conn = sqlite3.connect(db_filename)
    remove_old_records(conn)
    conn.execute("update dhcp set active = 0")
    conn.commit()

    query = "replace into dhcp values (?, ?, ?, ?, ?, ?, ?)"
    for filename in data_files:
        result = parse_dhcp_snoop(filename)
        now = str(datetime.today().replace(microsecond=0))
        updated_result = (row + (1, now) for row in result)
        add_data_to_db(conn, query, updated_result)
    conn.close()


def get_data(db_filename, key, value):
    keys = "mac ip vlan interface switch".split()
    if key not in keys:
        print("Данный параметр не поддерживается.")
        print("Допустимые значения параметров: {}".format(", ".join(keys)))
        return
    conn = sqlite3.connect(db_filename)
    query = "select * from dhcp where {} = ? and active = ?".format(key)

    for active in (1, 0):
        result = conn.execute(query, (value, active))
        print_data_in_rows(result, active)
    conn.close()


def get_all_data(db_filename):
    query = "select * from dhcp where active = ?"
    conn = sqlite3.connect(db_filename)
    for active in (1, 0):
        result = conn.execute(query, (active,))
        print_data_in_rows(result, active)
    conn.close()
