# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

vlan_option = {'trunk': 'Enter trunk allowed vlans: ', 'access': 'Enter access vlan: '}

intf_mode = input('Enter interface mode (access/trunk): ')
intf = input('Enter interface type and number (Fa0/6, Gi0/1, Fa0/1): ')
vlan = input(vlan_option.get(intf_mode))
switch = {'access': access_template, 'trunk': trunk_template}

print(f'\ninterface {intf}')
print('\n'.join(switch.get(intf_mode)).format(vlan))

