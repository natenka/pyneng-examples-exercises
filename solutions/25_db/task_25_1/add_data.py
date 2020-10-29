import glob
import os
import re
import sqlite3
from pprint import pprint

import yaml


def parse_dhcp_snoop(filename):
    regex = re.compile("(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)")
    sw = re.search("(\w+)_dhcp_snooping.txt", filename).group(1)
    with open(filename) as f:
        result = [match.groups() + (sw,) for match in regex.finditer(f.read())]
    return result


def add_data(db, query, data):
    connection = sqlite3.connect(db)
    for row in data:
        try:
            with connection:
                connection.execute(query, row)
        except sqlite3.IntegrityError as err:
            print("При добавлении данных:", row, "Возникла ошибка:", err)
    connection.close()


def add_sw_data(db_name, sw_data_file):
    db_exists = os.path.exists(db_name)
    if not db_exists:
        print("База данных не существует. Перед добавлением данных, ее надо создать")
        return
    print("Добавляю данные в таблицу switches...")
    query_switches = "insert into switches values (?,?)"
    with open(sw_data_file) as f:
        switches = yaml.safe_load(f)
    sw_data = list(switches["switches"].items())
    add_data(db_name, query_switches, sw_data)


def add_dhcp_data(db_name, data_files):
    db_exists = os.path.exists(db_name)
    if not db_exists:
        print("База данных не существует. Перед добавлением данных, ее надо создать")
        return
    print("Добавляю данные в таблицу dhcp...")
    query = "insert into dhcp values (?, ?, ?, ?, ?)"
    result = []
    for filename in data_files:
        result.extend(parse_dhcp_snoop(filename))
    add_data(db_name, query, result)


if __name__ == "__main__":
    db_filename = "dhcp_snooping.db"
    dhcp_snoop_files = glob.glob("sw*_dhcp_snooping.txt")
    add_sw_data(db_filename, "switches.yml")
    add_dhcp_data(db_filename, dhcp_snoop_files)
