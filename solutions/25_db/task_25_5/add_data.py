import glob
import sqlite3
import re
import os
import yaml
from pprint import pprint


def parse_dhcp_snoop(filename):
    regex = re.compile("(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)")
    hostname = re.search("(\w+)_dhcp_snooping.txt", filename).group(1)
    with open(filename) as f:
        result = [match.groups() + (hostname,) for match in regex.finditer(f.read())]
    return result


def add_data(connection, query, data):
    for row in data:
        try:
            with connection:
                connection.execute(query, row)
        except sqlite3.IntegrityError as err:
            print("При добавлении данных:", row, "Возникла ошибка:", err)


def add_sw_data(db_name, sw_data_file):
    connection = sqlite3.connect(db_name)
    query_switches = "insert into switches values (?,?)"
    with open(sw_data_file) as f:
        switches = yaml.safe_load(f)
        sw_data = list(switches["switches"].items())
        add_data(connection, query_switches, sw_data)
    connection.close()


def add_dhcp_data(db_name, data_files):
    connection = sqlite3.connect(db_name)
    connection.execute("update dhcp set active = 0")
    query = "replace into dhcp values (?, ?, ?, ?, ?, ?, datetime('now'))"
    for filename in data_files:
        result = parse_dhcp_snoop(filename)
        updated_result = [row + (1,) for row in result]
        add_data(connection, query, updated_result)
    connection.close()


if __name__ == "__main__":
    db_filename = "dhcp_snooping.db"
    # dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
    dhcp_snoop_files = glob.glob("new_data/sw*_dhcp_snooping.txt")

    db_exists = os.path.exists(db_filename)
    if db_exists:
        add_sw_data(db_filename, "switches.yml")
        add_dhcp_data(db_filename, dhcp_snoop_files)
    else:
        print("База данных не существует. Для добавления данных, ее надо создать")
