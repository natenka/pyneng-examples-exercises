# -*- coding: utf-8 -*-
'''
Задание 18.6

В этом задании выложен файл parse_dhcp_snooping.py.

В файле созданы несколько функций и описаны аргументы командной строки,
которые принимает файл.

> В файле parse_dhcp_snooping.py нельзя ничего менять.

Есть поддержка аргументов для выполнения всех действий, которые,
в предыдущих заданиях, выполнялись в файлах create_db.py, add_data.py и get_data.py.

В файле parse_dhcp_snooping.py есть такая строка:
import parse_dhcp_snooping_functions as pds

И задача этого задания в том, чтобы создать все необходимые функции,
в файле parse_dhcp_snooping_functions.py на основе информации в файле parse_dhcp_snooping.py.

Из файла parse_dhcp_snooping.py, необходимо определить:
* какие функции должны быть в файле parse_dhcp_snooping_functions.py
* какие параметры создать в этих функциях

Необходимо создать соответствующие функции и перенести в них функционал,
который описан в предыдущих заданиях.

Вся необходимая информация, присутствует в функциях create, add, get,
в файле parse_dhcp_snooping.py.

В принципе, для выполнения задания, не обязательно разбираться с модулем argparse.
Но, вы можете почитать о нем в разделе 08_modules/useful_modules/argparse.html.

Для того, чтобы было проще начать, попробуйте создать необходимые функции в файле
parse_dhcp_snooping_functions.py и просто выведите аргументы функций, используя print.

Потом, можно создать функции, которые запрашивают информацию из БД
(базу данных можно скопировать из предыдущих заданий).

Можно создавать любые вспомогательные функции в файле parse_dhcp_snooping_functions.py,
а не только те, которые вызываются из файла parse_dhcp_snooping.py.


Проверьте все операции:
* создание БД
* добавление информации о коммутаторах
* добавление информации на основании вывода sh ip dhcp snooping binding из файлов
* выборку информации из БД (по параметру и всю информацию)


Чтобы было проще понять, как будет выглядеть вызов скрипта,
ниже несколько примеров.

$ python parse_dhcp_snooping.py -h
usage: parse_dhcp_snooping.py [-h] {create_db,add,get} ...

optional arguments:
  -h, --help           show this help message and exit

subcommands:
  valid subcommands

  {create_db,add,get}  additional info
    create_db          create new db
    add                add data to db
    get                get data from db

$ python parse_dhcp_snooping.py get -h
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]

optional arguments:
  -h, --help            show this help message and exit
  --db DB_FILE          db name
  -k {mac,ip,vlan,interface,switch}
                        host key (parameter) to search
  -v VALUE              value of key
  -a                    show db content

$ python parse_dhcp_snooping.py add -h
usage: parse_dhcp_snooping.py add [-h] [--db DB_FILE] [-s]
                                  filename [filename ...]

positional arguments:
  filename      file(s) to add to db

optional arguments:
  -h, --help    show this help message and exit
  --db DB_FILE  db name
  -s            add switch data if set, else add normal data

$ python parse_dhcp_snooping.py create_db -h
usage: parse_dhcp_snooping.py create_db [-h] [-n NAME] [-s SCHEMA]

optional arguments:
  -h, --help  show this help message and exit
  -n NAME     db filename
  -s SCHEMA   db schema filename


$ python parse_dhcp_snooping.py create_db
Creating DB dhcp_snooping.db with DB schema dhcp_snooping_schema.sql
Creating schema...
Done

$ python parse_dhcp_snooping.py add sw1_dhcp_snooping.txt sw2_dhcp_snooping.txt sw3_dhcp_snooping.txt
Reading info from file(s)
sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt

Adding data to db dhcp_snooping.db


$ python parse_dhcp_snooping.py add -s switches.yml
Adding switch data to database


$ python parse_dhcp_snooping.py get
Showing dhcp_snooping.db content...
----------------------------------------------------------------------
00:09:BB:3D:D6:58  10.1.10.2         10    FastEthernet0/1      sw1
00:04:A3:3E:5B:69  10.1.5.2          5     FastEthernet0/10     sw1
00:05:B3:7E:9B:60  10.1.5.4          5     FastEthernet0/9      sw1
00:07:BC:3F:A6:50  10.1.10.6         10    FastEthernet0/3      sw1
00:09:BC:3F:A6:50  192.168.1.100     100   FastEthernet0/5      sw1
00:A9:BB:3D:D6:58  10.1.10.20        10    FastEthernet0/7      sw2
00:B4:A3:3E:5B:69  10.1.5.20         5     FastEthernet0/5      sw2
00:C5:B3:7E:9B:60  10.1.5.40         5     FastEthernet0/9      sw2
00:A9:BC:3F:A6:50  100.1.1.6         3     FastEthernet0/20     sw3

$ python parse_dhcp_snooping.py get -k vlan -v 10
Geting data from DB: dhcp_snooping.db
Request data for host(s) with vlan 10

Detailed information for host(s) with vlan 10
----------------------------------------
mac         : 00:09:BB:3D:D6:58
ip          : 10.1.10.2
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------
mac         : 00:07:BC:3F:A6:50
ip          : 10.1.10.6
interface   : FastEthernet0/3
switch      : sw1
----------------------------------------
mac         : 00:A9:BB:3D:D6:58
ip          : 10.1.10.20
interface   : FastEthernet0/7
switch      : sw2
----------------------------------------


$ python parse_dhcp_snooping.py get -k vln -v 10
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]
parse_dhcp_snooping.py get: error: argument -k: invalid choice: 'vln' (choose from 'mac', 'ip', 'vlan', 'interface', 'switch')

'''
