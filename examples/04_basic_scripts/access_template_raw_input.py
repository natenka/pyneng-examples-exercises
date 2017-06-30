
interface = raw_input('Enter interface type and number: ')
vlan = int(raw_input('Enter VLAN number: '))

access_template = ['switchport mode access',
                   'switchport access vlan %d',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print '\n' + '-' * 30
print 'interface %s' % interface
print '\n'.join(access_template) % vlan
