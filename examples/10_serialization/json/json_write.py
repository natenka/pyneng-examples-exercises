import json


trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan']


access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

to_json = {'trunk':trunk_template, 'access':access_template}

with open('sw_templates.json', 'w') as f:
    f.write(json.dumps(to_json))

with open('sw_templates.json') as f:
    print f.read()

"""
Example:
$ python json_write.py
{"access": ["switchport mode access", "switchport access vlan", "switchport nonegotiate", "spanning-tree portfast", "spanning-tree bpduguard enable"], "trunk": ["switchport trunk encapsulation dot1q", "switchport mode trunk", "switchport trunk native vlan 999", "switchport trunk allowed vlan"]}

"""
