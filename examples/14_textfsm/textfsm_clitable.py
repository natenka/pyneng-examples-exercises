import textfsm.clitable as clitable

output_sh_ip_route_ospf = open('output/sh_ip_route_ospf.txt').read()

cli_table = clitable.CliTable('index', 'templates')

attributes = {'Command': 'show ip route ospf' , 'Vendor': 'Cisco'}

cli_table.ParseCmd(output_sh_ip_route_ospf, attributes)
print "CLI Table output:\n", cli_table

print "Formatted Table:\n", cli_table.FormattedTable()

data_rows = []

for row in cli_table:
    current_row = []
    for value in row:
        current_row.append(value)
    data_rows.append(current_row)

header = []
for name in cli_table.header:
    header.append(name)

print header
for row in data_rows:
    print row

"""
Example:

$ python textfsm_clitable.py
CLI Table output:
Network, Mask, Distance, Metric, NextHop
10.0.24.0, /24, 110, 20, ['10.0.12.2']
10.0.34.0, /24, 110, 20, ['10.0.13.3']
10.2.2.2, /32, 110, 11, ['10.0.12.2']
10.3.3.3, /32, 110, 11, ['10.0.13.3']
10.4.4.4, /32, 110, 21, ['10.0.13.3', '10.0.12.2', '10.0.14.4']
10.5.35.0, /24, 110, 20, ['10.0.13.3']

Formatted Table:
 Network    Mask  Distance  Metric  NextHop
====================================================================
 10.0.24.0  /24   110       20      10.0.12.2
 10.0.34.0  /24   110       20      10.0.13.3
 10.2.2.2   /32   110       11      10.0.12.2
 10.3.3.3   /32   110       11      10.0.13.3
 10.4.4.4   /32   110       21      10.0.13.3, 10.0.12.2, 10.0.14.4
 10.5.35.0  /24   110       20      10.0.13.3

['Network', 'Mask', 'Distance', 'Metric', 'NextHop']
['10.0.24.0', '/24', '110', '20', ['10.0.12.2']]
['10.0.34.0', '/24', '110', '20', ['10.0.13.3']]
['10.2.2.2', '/32', '110', '11', ['10.0.12.2']]
['10.3.3.3', '/32', '110', '11', ['10.0.13.3']]
['10.4.4.4', '/32', '110', '21', ['10.0.13.3', '10.0.12.2', '10.0.14.4']]
['10.5.35.0', '/24', '110', '20', ['10.0.13.3']]

"""
