# -*- coding: utf-8 -*-
'''
Задание 25.6

Для заданий 25 раздела нет тестов!

В этом задании выложен файл parse_dhcp_snooping.py.
В файле parse_dhcp_snooping.py нельзя ничего менять.

В файле созданы несколько функций и описаны аргументы командной строки,
которые принимает файл.

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
Но, вы можете почитать о нем в разделе https://natenka.gitbook.io/pyneng/part_ii/12_useful_modules/argparse.

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
В примерах показывается вариант, когда в базе данных есть поля active и last_active,
но можно также использовать вариант без этих полей.

$ python parse_dhcp_snooping.py get -h
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]

optional arguments:
  -h, --help            show this help message and exit
  --db DB_FILE          имя БД
  -k {mac,ip,vlan,interface,switch}
                        параметр для поиска записей
  -v VALUE              значение параметра
  -a                    показать все содержимое БД


$ python parse_dhcp_snooping.py add -h
usage: parse_dhcp_snooping.py add [-h] [--db DB_FILE] [-s]
                                  filename [filename ...]

positional arguments:
  filename      файл(ы), которые надо добавить

optional arguments:
  -h, --help    show this help message and exit
  --db DB_FILE  имя БД
  -s            если флаг установлен, добавлять данные коммутаторов, иначе -
                DHCP записи


$ python parse_dhcp_snooping.py add -h
usage: parse_dhcp_snooping.py add [-h] [--db DB_FILE] [-s]
                                  filename [filename ...]

positional arguments:
  filename      файл(ы), которые надо добавить

optional arguments:
  -h, --help    show this help message and exit
  --db DB_FILE  имя БД
  -s            если флаг установлен, добавлять данные коммутаторов, иначе
                добавлять DHCP записи


$ python parse_dhcp_snooping.py get -h
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]

optional arguments:
  -h, --help            show this help message and exit
  --db DB_FILE          имя БД
  -k {mac,ip,vlan,interface,switch}
                        параметр для поиска записей
  -v VALUE              значение параметра
  -a                    показать все содержимое БД


$ python parse_dhcp_snooping.py create_db
Создаю БД dhcp_snooping.db со схемой dhcp_snooping_schema.sql
Создаю базу данных...


$ python parse_dhcp_snooping.py add sw[1-3]_dhcp_snooping.txt
Читаю информацию из файлов
sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt

Добавляю данные по DHCP записях в dhcp_snooping.db


$ python parse_dhcp_snooping.py add -s switches.yml
Добавляю данные о коммутаторах

$ python parse_dhcp_snooping.py get
В таблице dhcp такие записи:

Активные записи:

-----------------  ---------------  --  ----------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1  2019-03-08 16:47:52
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1  1  2019-03-08 16:47:52
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1  2019-03-08 16:47:52
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1  1  2019-03-08 16:47:52
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  1  2019-03-08 16:47:52
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1  2019-03-08 16:47:52
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1  2019-03-08 16:47:52
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  1  2019-03-08 16:47:52
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2  1  2019-03-08 16:47:52
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1  2019-03-08 16:47:52
-----------------  ---------------  --  ----------------  ---  -  -------------------


$ python parse_dhcp_snooping.py get -k vlan -v 10
Данные из БД: dhcp_snooping.db
Информация об устройствах с такими параметрами: vlan 10

Активные записи:

-----------------  ----------  --  ---------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1  1  2019-03-08 16:47:52
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/3  sw1  1  2019-03-08 16:47:52
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2  1  2019-03-08 16:47:52
-----------------  ----------  --  ---------------  ---  -  -------------------


$ python parse_dhcp_snooping.py get -k vln -v 10
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]
parse_dhcp_snooping.py get: error: argument -k: invalid choice: 'vln' (choose from 'mac', 'ip', 'vlan', 'interface', 'switch')

'''
