# -*- coding: utf-8 -*-
import sqlite3
import sys

db_filename = 'dhcp_snooping.db'

query_dict = {'vlan': "select * from dhcp where vlan = ?",
              'mac': "select * from dhcp where mac = ?",
              'ip': "select * from dhcp where ip = ?",
              'interface': "select * from dhcp where interface = ?"}


key, value = sys.argv[1:]
keys = query_dict.keys()

if not key in keys:
    print "Enter key from {}".format(','.join(keys))
else:

    with sqlite3.connect(db_filename) as conn:
        conn.row_factory = sqlite3.Row

        print "\nDetailed information for host(s) with", key, value
        print '-' * 40

        query = query_dict[key]
        result = conn.execute(query, (value,))
        # метод description позволяет получить заголовки полученных столбцов.
        # В нем будут находиться только те столбцы, который соответствуют запросу.
        all_rows = [r[0] for r in result.description]

        for row in result:
            for row_name in all_rows:
                print "{:12}: {}".format(row_name, row[row_name])
            print '-' * 40
