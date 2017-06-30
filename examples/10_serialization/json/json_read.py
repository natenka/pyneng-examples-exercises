import json

templates = json.load(open('sw_templates.json'))

print templates

for section, commands in templates.items():
    print section
    print '\n'.join(commands)

"""
Example:
$ python json_read.py
{u'access': [u'switchport mode access', u'switchport access vlan', u'switchport nonegotiate', u'spanning-tree portfast', u'spanning-tree bpduguard enable'], u'trunk': [u'switchport trunk encapsulation dot1q', u'switchport mode trunk', u'switchport trunk native vlan 999', u'switchport trunk allowed vlan']}

access
switchport mode access
switchport access vlan
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
trunk
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk native vlan 999
switchport trunk allowed vlan
"""
