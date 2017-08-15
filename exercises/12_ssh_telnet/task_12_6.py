# -*- coding: utf-8 -*-
'''
Задание 12.6

В задании используется пример из раздела про [модуль multiprocessing](book/chapter12/5b_multiprocessing.md).

Переделать пример таким образом, чтобы:
* вместо функции connect_ssh, использовалась функция send_commands из задания 12.3
 * переделать функцию send_commands, чтобы использовалась очередь и функция conn_processes по-прежнему возвращала словарь с результатами.
 * Проверить работу со списком команд, с командами из файла, с командой show

Подсказка: multiprocessing.Process может передавать функции не только позиционные аргументы, но и ключевые:
def conn_processes(function, arg1, arg2, **kwargs):

    for some in something:
        p = multiprocessing.Process(target=function,
                                    args=(arg1, arg2),
                                    kwargs=kwargs)
                                    
Пример из раздела:
'''

import multiprocessing
import sys
import yaml
from pprint import pprint

from netmiko import ConnectHandler


COMMAND = sys.argv[1]
devices = yaml.load(open('devices.yaml'))


def connect_ssh(device_dict, command, queue):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)

        print("Connection to device {}".format(device_dict['ip']))
        queue.put({device_dict['ip']: result})


def conn_processes(function, devices, command):
    processes = []
    queue = multiprocessing.Queue()

    for device in devices:
        p = multiprocessing.Process(target=function,
                                    args=(device, command, queue))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    results = []
    for p in processes:
        results.append(queue.get())

    return results


pprint((conn_processes(connect_ssh, devices['routers'], COMMAND)))

