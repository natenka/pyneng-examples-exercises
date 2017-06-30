# Задания

{% include "../exercises_intro.md" %}

### Задание 12.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к устройствам из списка, и выполняет  команду
на основании переданных аргументов.

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* command - команда, которую надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - результат выполнения команды

Проверить работу функции на примере:
* устройств из файла devices.yaml (для этого надо считать информацию из файла)
* и команды command

```python
import netmiko

command = "sh ip int br"

def send_show_command(device_list, command):
    """
    Функция подключается по SSH к устройствам из списка, и выполняет команду
    на основании переданных аргументов.

    Параметры функции:
    - devices_list - список словарей с параметрами подключения к устройствам,
      которым надо передать команды
    - command - команда, которую надо выполнить
    
    Функция возвращает словарь с результатами выполнения команды:
        - ключ - IP устройства
        - значение - результат выполнения команды
    """
```

### Задание 12.2

Создать функцию send_config_commands

Функция подключается по SSH (с помощью netmiko) к устройствам из списка, и выполняет перечень команд в конфигурационном режиме на основании переданных аргументов.

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* config_commands - список команд, которые надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Проверить работу функции на примере:
* устройств из файла devices.yaml (для этого надо считать информацию из файла)
* и списка команд commands

```python

import netmiko

commands = [ 'logging 10.255.255.1',
             'logging buffered 20010',
             'no logging console' ]

def send_config_commands(device_list, config_commands):
    """
    Функция подключается по SSH к устройствам из списка,
    и выполняет команды в конфигурационном режиме.

    Параметры функции:
        - devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
        - config_commands - список команд, которые надо выполнить
    
    Функция возвращает словарь с результатами выполнения команды:
        - ключ - IP устройства
        - значение - вывод с выполнением команд
    """


```

### Задание 12.2a

Дополнить функцию send_config_commands из задания 12.2

Добавить аргумент output, который контролирует будет ли результат выполнения команд выводиться на стандартный поток вывода.
По умолчанию, результат должен выводиться.


### Задание 12.2b

Дополнить функцию send_config_commands из задания 12.2a или 12.2

Добавить проверку на ошибки:
* При выполнении команд, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

Проверить функцию на команде с ошибкой.



### Задание 12.3

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

```python
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
```


### Задание 12.3a

Изменить функцию send_commands таким образом, чтобы в списке словарей device_list
не надо было указывать имя пользователя, пароль, и пароль на enable.

Функция должна запрашивать имя пользователя, пароль и пароль на enable при старте.
Пароль не должен отображаться при наборе.

В файле devices2.yaml эти параметры уже удалены.



### Задание 12.3b
Дополнить функцию send_commands таким образом, чтобы перед подключением к устройствам по SSH,
выполнялась проверка доступности устройства pingом (можно вызвать команду ping в ОС).

> Как выполнять команды ОС, описано в разделе [subprocess](https://natenka.gitbooks.io/pyneng/content/book/16_additional_info/useful_modules/subprocess.html). Там же есть пример функции с отправкой ping.

Если устройство доступно, можно выполнять подключение.
Если не доступно, вывести сообщение о том, что устройство с определенным IP-адресом недоступно
и не выполнять подключение.

Для удобства можно сделать отдельную функцию для проверки доступности 
и затем использовать ее в функции send_commands.



### Задание 12.4

В задании используется пример из раздела про [модуль threading](../../book/12_ssh_telnet/5a_threading.md).

Переделать пример таким образом, чтобы:
* вместо функции connect_ssh, использовалась функция send_commands из задания 12.3
 * переделать функцию send_commands, чтобы использовалась очередь и функция conn_threads по-прежнему возвращала словарь с результатами.
 * Проверить работу со списком команд, с командами из файла, с командой show 


Пример из раздела:
```python
from netmiko import ConnectHandler
import sys
import yaml
import threading
from Queue import Queue

COMMAND = sys.argv[1]
devices = yaml.load(open('devices.yaml'))

def connect_ssh(device_dict, command, queue):

    ssh = ConnectHandler(**device_dict)
    ssh.enable()
    result = ssh.send_command(command)
    print "Connection to device %s" % device_dict['ip']

    queue.put({ device_dict['ip']: result })


def conn_threads(function, devices, command):
    threads = []
    q = Queue()

    for device in devices:
        th = threading.Thread(target = function, args = (device, command, q))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    results = []
    for t in threads:
        results.append(q.get())

    return results

print conn_threads(connect_ssh, devices['routers'], COMMAND)
```


### Задание 12.5

Использовать функции полученные в результате выполнения задания 12.4.

Переделать функцию conn_threads таким образом, чтобы с помощью аргумента limit,
можно было указывать сколько подключений будут выполняться параллельно.
По умолчанию, значение аргумента должно быть 2.

Изменить функцию соответственно, так, чтобы параллельных подключений выполнялось столько,
сколько указано в аргументе limit.


### Задание 12.6

В задании используется пример из раздела про [модуль multiprocessing](book/chapter12/5b_multiprocessing.md).

Переделать пример таким образом, чтобы:
* вместо функции connect_ssh, использовалась функция send_commands из задания 12.3
 * переделать функцию send_commands, чтобы использовалась очередь и функция conn_processes по-прежнему возвращала словарь с результатами.
 * Проверить работу со списком команд, с командами из файла, с командой show


Пример из раздела:
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

### Задание 12.7

Использовать функции полученные в результате выполнения задания 12.6.

Переделать функцию conn_processes таким образом, чтобы с помощью аргумента limit,
можно было указывать сколько подключений будут выполняться параллельно.
По умолчанию, значение аргумента должно быть 2.

Изменить функцию соответственно, так, чтобы параллельных подключений выполнялось столько,
сколько указано в аргументе limit.

