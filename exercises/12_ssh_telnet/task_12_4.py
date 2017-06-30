# -*- coding: utf-8 -*-
'''
Задание 12.4

В задании используется пример из раздела про [модуль threading](book/chapter12/5a_threading.md).

Переделать пример таким образом, чтобы:
* вместо функции connect_ssh, использовалась функция send_commands из задания 12.3
 * переделать функцию send_commands, чтобы использовалась очередь и функция conn_threads по-прежнему возвращала словарь с результатами.
 * Проверить работу со списком команд, с командами из файла, с командой show

'''

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
