# -*- coding: utf-8 -*-
import sys
import threading
from pprint import pprint
from queue import Queue

import yaml
from netmiko import ConnectHandler

COMMAND = sys.argv[1]
with open('devices.yaml') as f:
    devices = yaml.safe_load(f)


def connect_ssh(device_dict, command, queue):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        print('Connection to device {}'.format(device_dict['ip']))

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
