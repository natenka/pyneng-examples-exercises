# -*- coding: utf-8 -*-

"""
Задание 24.1a

Дополнить класс CiscoSSH из задания 24.1.

Перед подключением по SSH необходимо проверить если ли в словаре
с параметрами подключения такие параметры: username, password, secret.
Если нет, запросить их у пользователя, а затем выполнять подключение.
Если параметры есть, сразу выполнить подключение.

In [1]: from task_24_1a import CiscoSSH

In [2]: device_params = {
   ...:         'device_type': 'cisco_ios',
   ...:         'host': '192.168.100.1',
   ...: }

In [3]: r1 = CiscoSSH(**device_params)
Введите имя пользователя: cisco
Введите пароль: cisco
Введите пароль для режима enable: cisco

In [4]: r1.send_show_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

"""
from base_connect_class import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, **device_params):
        params = {
            "username": "Введите имя пользователя: ",
            "password": "Введите пароль: ",
            "secret": "Введите пароль для режима enable: ",
        }
        for param in params:
            if not param in device_params:
                device_params[param] = input(params[param])
        super().__init__(**device_params)
        self.ssh.enable()

