import csv

with open('sw_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print row


"""
Example:
$ python csv_read_dict.py
{'model': '3750', 'hostname': 'sw1', 'vendor': 'Cisco', 'location': 'London'}
{'model': '3850', 'hostname': 'sw2', 'vendor': 'Cisco', 'location': 'Liverpool'}
{'model': '3650', 'hostname': 'sw3', 'vendor': 'Cisco', 'location': 'Liverpool'}
{'model': '3650', 'hostname': 'sw4', 'vendor': 'Cisco', 'location': 'London'}
"""
