# -*- coding: utf-8 -*-

"""
Задание 11.1a

Добавить в файл add_data.py, из задания 11.1, проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

"""

import glob

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print dhcp_snoop_files

