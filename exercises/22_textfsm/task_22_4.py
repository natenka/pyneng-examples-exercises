# -*- coding: utf-8 -*-
'''
Задание 22.4

На основе примера textfsm_clitable.py из раздела TextFSM
сделать функцию parse_command_dynamic.

Параметры функции:
* словарь атрибутов, в котором находятся такие пары ключ: значение:
 * 'Command': команда
 * 'Vendor': вендор (обратите внимание, что файл index отличается от примера, который использовался в разделе, поэтому вам нужно подставить тут правильное значение)
* имя файла, где хранится соответствие между командами и шаблонами (строка)
 * значение по умолчанию аргумента - index
* каталог, где хранятся шаблоны и файл с соответствиями (строка)
 * значение по умолчанию аргумента - templates
* вывод команды (строка)

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - названия столбцов
* значения - соответствующие значения в столбцах

Проверить работу функции на примере вывода команды sh ip int br.

Пример из раздела:
'''

import clitable

output_sh_ip_route_ospf = open('output/sh_ip_route_ospf.txt').read()

cli_table = clitable.CliTable('index', 'templates')
attributes = {'Command': 'show ip route ospf', 'Vendor': 'Cisco'}

cli_table.ParseCmd(output_sh_ip_route_ospf, attributes)

print('CLI Table output:\n', cli_table)
print('Formatted Table:\n', cli_table.FormattedTable())

data_rows = [list(row) for row in cli_table]
header = list(cli_table.header)

print(header)
for row in data_rows:
    print(row)
