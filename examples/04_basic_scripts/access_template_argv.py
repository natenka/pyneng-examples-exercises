from sys import argv

interface, vlan = argv[1:]

access_template = ['switchport mode access',
                   'switchport access vlan %d',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print 'interface %s' % interface
print '\n'.join(access_template) % int(vlan)
