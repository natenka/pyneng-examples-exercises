# -*- coding: utf-8 -*-

"""
Задание 11.1

* add_data.py
 * с помощью этого скрипта, мы будем добавлять данные в БД
  * теперь у нас есть не только данные из вывода sh ip dhcp snooping binding,
    но и информация о коммутаторах

Соответственно, в файле add_data.py у нас будет две части:
* запись информации о коммутаторах в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* запись информации на основании вывода sh ip dhcp snooping binding
 * теперь у нас есть вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch,
   нам нужно его заполнять. Имя коммутатора мы определяем по имени файла с данными

"""

import glob

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print dhcp_snoop_files

