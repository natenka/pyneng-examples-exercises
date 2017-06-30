# -*- coding: utf-8 -*-

"""
Задание 4.3a

В этой задаче нельзя использовать условие if.

Дополнить скрипт из задания 4.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

"""

access_template = ['switchport mode access',
                   'switchport access vlan %s',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan %s']

