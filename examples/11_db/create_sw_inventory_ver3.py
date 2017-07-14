# -*- coding: utf-8 -*-
from pprint import pprint
import sqlite3

data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]

#MAC-адрес sw7 совпадает с MAC-адресом существующего коммутатора - sw3
data2 = [('0000.AAAA.DDDD', 'sw7', 'Cisco 2960', 'London, Green Str')]

def crete_connection(db_name):
    con = sqlite3.connect(db_name)
    return con


def create_table(connection, sql_command):
    con.execute("""create table switch
                   (mac text primary key,
                    hostname text,
                    model text,
                    location text)""")


def write_data_to_db(connection, query, data):
    try:
        with connection:
            connection.executemany(query, data)
    except sqlite3.IntegrityError as e:
        print("Error occured: ", e)
        return False
    else:
        return True


def get_all(connection, query):
    result = []
    for row in connection.execute(query):
        result.append(row)
    return result


query = "INSERT into switch values (?, ?, ?, ?)"

write_data_to_db(query, data)
pprint(get_all("select * from switch"))

print('-'*30)

write_data_to_db(query, data2)
pprint(get_all("select * from switch"))


