import os
import sqlite3
import re

data_filename = 'dhcp_snooping.txt'
db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'

regex = re.compile('(.+?) +(.*?) +\d+ +[\w-]+ +(\d+) +(.*$)')

with open(data_filename) as data:
    result = [regex.search(line).groups() for line in data if line[0].isdigit()]

db_exists = os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if not db_exists:
        print 'Creating schema...'
        with open(schema_filename, 'r') as f:
            schema = f.read()
        conn.executescript(schema)
        print 'Done'

        print 'Inserting DHCP Snooping data'
        for val in result:
            query = """insert into dhcp (mac, ip, vlan, interface)
            values (?, ?, ?, ?)"""
            conn.execute(query, val)
    else:
        print 'Database exists, assume dhcp table does, too.'
