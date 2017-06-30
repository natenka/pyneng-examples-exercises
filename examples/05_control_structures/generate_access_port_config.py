access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

fast_int = {'access':{'0/12':'10',
                      '0/14':'11',
                      '0/16':'17',
                      '0/17':'150'}}

for intf in fast_int['access']:
    print 'interface FastEthernet' + intf
    for command in access_template:
        if command.endswith('access vlan'):
            print ' %s %s' % (command, fast_int['access'][intf])
        else:
            print ' %s' % command

"""
Example:

python generate_access_port_config.py
interface FastEthernet0/12
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/14
 switchport mode access
 switchport access vlan 11
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/16
 switchport mode access
 switchport access vlan 17
 spanning-tree portfast
 spanning-tree bpduguard enable
"""
