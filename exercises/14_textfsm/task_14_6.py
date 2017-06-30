# -*- coding: utf-8 -*-
'''
Задание 14.6

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
'''

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
