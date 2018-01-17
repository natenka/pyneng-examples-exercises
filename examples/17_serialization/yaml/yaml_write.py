import yaml

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_yaml = {'trunk': trunk_template, 'access': access_template}

with open('sw_templates.yaml', 'w') as f:
    yaml.dump(to_yaml, f)

with open('sw_templates.yaml') as f:
    print(f.read())
'''
Example:

$ python yaml_write.py
access: [switchport mode access, switchport access vlan, switchport nonegotiate, spanning-tree
    portfast, spanning-tree bpduguard enable]
trunk: [switchport trunk encapsulation dot1q, switchport mode trunk, switchport trunk
    native vlan 999, switchport trunk allowed vlan]
'''
