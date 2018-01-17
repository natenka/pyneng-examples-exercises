# -*- coding: utf-8 -*-
'''
Задание 22.6

Это задание похоже на задание 22.5, но в этом задании подключения надо выполнять параллельно с помощью потоков.
Для параллельного подключения использовать модуль concurrent.futures.

В этом упражнении нужно создать функцию send_and_parse_command_parallel:
* она должна использовать внутри себя функцию send_and_parse_command
* какие аргументы должны быть у функции send_and_parse_command_parallel, нужно решить самостоятельно
* функция send_and_parse_command_parallel должна возвращать словарь, в котором:
 * ключ - IP устройства
 * значение - список словарей

Проверить работу функции send_and_parse_command_parallel на команде sh ip int br.

'''

import yaml

test_command = "sh ip int br"
devices = yaml.load(open('devices.yaml'))
