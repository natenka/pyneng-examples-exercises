# -*- coding: utf-8 -*-
'''
Задание 12.4

В задании используется пример из раздела про [модуль threading](book/chapter12/5a_threading.md).

Переделать пример таким образом, чтобы:
* вместо функции connect_ssh, использовалась функция send_commands из задания 12.3
 * переделать функцию send_commands, чтобы использовалась очередь и функция conn_threads по-прежнему возвращала словарь с результатами.
 * Проверить работу со списком команд, с командами из файла, с командой show

Подсказка: threading.Thread может передавать функции не только позиционные аргументы, но и ключевые:
def conn_threads(function, arg1, arg2, **kwargs):

    for some in something:
        th = threading.Thread(target=function,
                              args=(arg1, arg2),
                              kwargs=kwargs)

'''

import threading
from queue import Queue
from pprint import pprint
from netmiko import ConnectHandler


COMMAND = sys.argv[1]
devices = yaml.load(open('devices.yaml'))


def connect_ssh(device_dict, command, queue):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        print("Connection to device {}".format(device_dict['ip']))

        #Добавляем словарь в очередь
        queue.put({device_dict['ip']: result})


def conn_threads(function, devices, command):
    threads = []
    q = Queue()

    for device in devices:
        # Передаем очередь как аргумент, функции
        th = threading.Thread(target=function, args=(device, command, q))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    results = []
    # Берем результаты из очереди и добавляем их в список results
    for t in threads:
        results.append(q.get())

    return results

pprint(conn_threads(connect_ssh, devices['routers'], COMMAND))

