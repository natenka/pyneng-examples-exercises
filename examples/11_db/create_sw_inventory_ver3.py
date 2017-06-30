# -*- coding: utf-8 -*-
import sqlite3

data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]

con = sqlite3.connect('sw_inventory3.db')
con.execute("create table switch (mac text primary key, hostname text, model text, location text)")

try:
    with con:
        query = "INSERT into switch values (?, ?, ?, ?)"
        con.executemany(query, data)
except sqlite3.IntegrityError as e:
    print "Error occured: ", e

for row in con.execute("select * from switch"):
    print row

print '-'*30

#MAC-адрес sw7 совпадает с MAC-адресом существующего коммутатора - sw3
data2 = [('0055.AAAA.CCCC', 'sw5', 'Cisco 3750', 'London, Green Str'),
         ('0066.BBBB.CCCC', 'sw6', 'Cisco 3780', 'London, Green Str'),
         ('0000.AAAA.DDDD', 'sw7', 'Cisco 2960', 'London, Green Str'),
         ('0088.AAAA.CCCC', 'sw8', 'Cisco 3750', 'London, Green Str')]

try:
    with con:
        query = "INSERT into switch values (?, ?, ?, ?)"
        con.executemany(query, data2)
except sqlite3.IntegrityError as e:
    print "Error occured: ", e

for row in con.execute("select * from switch"):
    print row
