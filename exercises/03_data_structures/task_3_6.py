# -*- coding: utf-8 -*-
'''
Задание 3.6

Обработать строку NAT таким образом, чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.
'''

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
