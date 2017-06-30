import sqlite3
import re

regex = re.compile('(.+?) +(.*?) +\d+ +[\w-]+ +(\d+) +(.*$)')
result = []

with open('dhcp_snooping.txt') as data:
    for line in data:
        if line[0].isdigit():
            result.append(regex.search(line).groups())

with sqlite3.connect('dhcp_snooping.db') as conn:
    print 'Creating schema...'
    with open('dhcp_snooping_schema.sql', 'r') as f:
        schema = f.read()
        conn.executescript(schema)
    print "Done"

    print 'Inserting DHCP Snooping data'

    for row in result:
        query = """insert into dhcp (mac, ip, vlan, interface)
        values (?, ?, ?, ?)"""
        conn.execute(query, row)
