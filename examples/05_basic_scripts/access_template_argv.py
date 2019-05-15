from sys import argv

interface = argv[1]
vlan = argv[2]
# второй вариант:
# interface, vlan = argv[1:3]

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))
