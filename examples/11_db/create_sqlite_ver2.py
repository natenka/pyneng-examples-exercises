import sqlite3
import re

regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

result = []

with open('dhcp_snooping.txt') as data:
    for line in data:
        match = regex.search(line)
        if match:
            result.append(match.groups())

with sqlite3.connect('dhcp_snooping.db') as conn:
    print('Creating schema...')
    with open('dhcp_snooping_schema.sql', 'r') as f:
        schema = f.read()
        conn.executescript(schema)
    print("Done")

    print('Inserting DHCP Snooping data')

    for row in result:
        query = """insert into dhcp (mac, ip, vlan, interface)
                   values (?, ?, ?, ?)"""
        conn.execute(query, row)
