# Задания

{% include "../exercises_intro.md" %}

### Задание 14.1

Переделать пример, который использовался в разделе TextFSM, в функцию.

Функция должна называться parse_output. Параметры функции:
* template - шаблон TextFSM (это должно быть имя файла, в котором находится шаблон)
* output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов (в примере ниже, находится в переменной header)
* остальные элементы это списки, в которых находятся результаты обработки вывода (в примере ниже, находится в переменной result)

Проверить работу функции на каком-то из примеров раздела.

Пример из раздела:
```python
import sys
import textfsm
from tabulate import tabulate

template = sys.argv[1]
output_file = sys.argv[2]

f = open(template)
output = open(output_file).read()

re_table = textfsm.TextFSM(f)

header = re_table.header
result = re_table.ParseText(output)

print tabulate(result, headers=header)

```


### Задание 14.1a

Переделать функцию parse_output из задания 14.1 таким образом,
чтобы, вместо списка списков, она возвращала один список словарей:
* ключи - названия столбцов,
* значения, соответствующие значения в столбцах.

То есть, для каждой строки будет один словарь в списке.


### Задание 14.2

В этом задании нужно использовать функцию parse_output из задания 14.1.
Она используется для того, чтобы получить структурированный вывод
в результате обработки вывода команды.

Полученный вывод нужно записать в CSV формате.

Для записи вывода в CSV, нужно создать функцию list_to_csv, которая ожидает как аргументы:
* список:
 * первый элемент - это список с названиями заголовков
 * остальные элементы это списки, в котором находятся результаты обработки вывода
* имя файла, в который нужно записать данные в CSV формате

Проверить работу функции на примере обработки команды sh ip int br (шаблон и вывод есть в разделе).


### Задание 14.3

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding.
Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.

Шаблон должен обрабатывать и возвращать значения таких столбцов:
* MacAddress
* IpAddress
* VLAN
* Interface

Проверить работу шаблона с помощью функции из задания 14.1.

### Задание 14.4

На основе примера из раздела [clitable](https://natenka.gitbooks.io/pyneng/content/book/14_textfsm/3_textfsm_clitable.html) сделать функцию parse_command_dynamic.

Параметры функции:
* словарь атрибутов, в котором находятся такие пары ключ: значение:
 * 'Command': команда
 * 'Vendor': вендор (обратите внимание, что файл index отличается от примера, который использовался в разделе, поэтому вам нужно подставить тут правильное значение)
* имя файла, где хранится соответствие между командами и шаблонами (строка)
 * значение по умолчанию аргумента - index
* каталог, где хранятся шаблоны и файл с соответствиями (строка)
 * значение по умолчанию аргумента - templates
* вывод команды (строка)

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 14.1a):
* ключи - названия столбцов
* значения - соответствующие значения в столбцах

Проверить работу функции на примере вывода команды sh ip int br.

Пример из раздела:
```python
import textfsm.clitable as clitable

output_sh_ip_route_ospf = open('output/sh_ip_route_ospf.txt').read()
cli_table = clitable.CliTable('index', 'templates')
attributes = {'Command': 'show ip route ospf' , 'Vendor': 'Cisco'}
cli_table.ParseCmd(output_sh_ip_route_ospf, attributes)

print "CLI Table output:\n", cli_table
print "Formatted Table:\n", cli_table.FormattedTable()

data_rows = []

for row in cli_table:
    current_row = []
    for value in row:
        current_row.append(value)
    data_rows.append(current_row)

header = []
for name in cli_table.header:
    header.append(name)

print header
for row in data_rows:
    print row
```

### Задание 14.4a

Переделать функцию из задания 14.4:
* добавить аргумент show_output, который контролирует будет ли выводиться результат обработки команды на стандартный поток вывода
 * по умолчанию False, что значит результат не будет выводиться
* результат должен отображаться в виде, который возвращает метод FormattedTable (пример есть в разделе)


### Задание 14.5

В этом задании соединяется функциональность TextFSM и подключение к оборудованию.

Задача такая:
* подключиться к оборудованию
* выполнить команду show
* полученный вывод передавать на обработку TextFSM
* вернуть результат обработки

Для этого, воспользуемся функциями, которые были созданы ранее:
* функцией send_show_command из упражнения 12.1
* функцией parse_command_dynamic из упражнения 14.4

В этом упражнении нужно создать функцию send_and_parse_command:
* функция должна использовать внутри себя функции parse_command_dynamic и send_show_command.
* какие аргументы должны быть у функции send_and_parse_command, нужно решить самостоятельно
 * но, надо иметь в виду, какие аргументы ожидают две готовые функции, которые мы используем
* функция send_and_parse_command должна возвращать:
 * функция send_show_command возвращает словарь с результатами выполнения команды:
    * ключ - IP устройства
    * значение - результат выполнения команды
 * затем, нужно отправить полученный вывод на обработку функции parse_command_dynamic
 * в результате, должен получиться словарь, в котором:
    * ключ - IP устройства
    * значение - список словарей (то есть, тот вывод, который был получен из функции parse_command_dynamic)

Для функции send_show_command создан файл devices.yaml, в котором находятся параметры подключения к устройствам.

Проверить работу функции send_and_parse_command на команде sh ip int br.


### Задание 14.6

Это задание похоже на задание 14.5, но в этом задании подключения надо выполнять параллельно.

Для этого надо использовать функции connect_ssh и conn_processes (пример из раздела multiprocessing) и функцию parse_command_dynamic из упражнения 14.4.

В этом упражнении нужно создать функцию send_and_parse_command_parallel:
* она должна использовать внутри себя функции connect_ssh, conn_processes и parse_command_dynamic
* какие аргументы должны быть у функции send_and_parse_command_parallel, нужно решить самостоятельно
 * но надо иметь в виду, какие аргументы ожидают три готовые функции, которые используются
* функция send_and_parse_command_parallel должна возвращать словарь, в котором:
 * ключ - IP устройства
 * значение - список словарей (то есть, тот вывод, который был получен из функции parse_command_dynamic)

Для функции conn_processes создан файл devices.yaml, в котором находятся параметры подключения к устройствам.

Проверить работу функции send_and_parse_command_parallel на команде sh ip int br.

Пример из раздела multiprocessing:
```python
import multiprocessing
from netmiko import ConnectHandler
import sys
import yaml


COMMAND = sys.argv[1]
devices = yaml.load(open('devices.yaml'))

def connect_ssh(device_dict, command, queue):
    ssh = ConnectHandler(**device_dict)
    ssh.enable()
    result = ssh.send_command(command)

    print "Connection to device %s" % device_dict['ip']
    queue.put({device_dict['ip']: result})


def conn_processes(function, devices, command):
    processes = []
    queue = multiprocessing.Queue()

    for device in devices:
        p = multiprocessing.Process(target = function, args = (device, command, queue))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    results = []
    for p in processes:
        results.append(queue.get())

    return results

print( conn_processes(connect_ssh, devices['routers'], COMMAND) )
```
