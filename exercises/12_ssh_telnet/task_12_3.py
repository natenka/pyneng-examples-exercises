# -*- coding: utf-8 -*-
'''
Задание 12.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри.

Далее комбинация из аргумента и соответствующей функции:
* show -- функция send_show_command из задания 12.1
* config -- функция send_config_commands из задания 12.2, 12.2a или 12.2b
* filename -- функция send_commands_from_file (ее также надо написать по аналогии с предыдущими)

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Проверить работу функции на примере:
* устройств из файла devices.yaml (для этого надо считать информацию из файла)
* и различных комбинация аргумента с командами:
    * списка команд commands
    * команды command
    * файла config.txt
'''

from netmiko import ConnectHandler

commands = [ 'logging 10.255.255.1',
             'logging buffered 20010',
             'no logging console' ]
command = "sh ip int br"

def send_show_command(device_list, show_command):
    pass

def send_config_commands(device_list, config_commands, output=True):
    pass

def send_commands_from_file(device_list, filename):
    pass

def send_commands(device_list, config=[], show='', filename=''):
    pass

