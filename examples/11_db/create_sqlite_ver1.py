import sqlite3

with sqlite3.connect('dhcp_snooping.db') as conn:
    print 'Creating schema...'
    with open('dhcp_snooping_schema.sql', 'r') as f:
        schema = f.read()
        conn.executescript(schema)
    print "Done"
