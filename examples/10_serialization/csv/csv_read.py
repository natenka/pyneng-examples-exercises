import csv

with open('sw_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

"""
Example:
$ python csv_read.py
['hostname', 'vendor', 'model', 'location']
['sw1', 'Cisco', '3750', 'London']
['sw2', 'Cisco', '3850', 'Liverpool']
['sw3', 'Cisco', '3650', 'Liverpool']
['sw4', 'Cisco', '3650', 'London']
"""
