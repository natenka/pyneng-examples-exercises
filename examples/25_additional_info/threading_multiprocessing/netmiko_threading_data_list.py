# -*- coding: utf-8 -*-
import sys
import yaml
import threading
from pprint import pprint

from netmiko import ConnectHandler

COMMAND = sys.argv[1]
with open('devices.yaml') as f:
    devices = yaml.safe_load(f)


def connect_ssh(device_dict, command, queue):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        print('Connection to device {}'.format(device_dict['ip']))

        #Добавляем словарь в список
        queue.append({device_dict['ip']: result})


def conn_threads(function, devices, command):
    threads = []
    q = []

    for device in devices:
        # Передаем список как аргумент, функции
        th = threading.Thread(target=function, args=(device, command, q))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    return q


result = conn_threads(connect_ssh, devices['routers'], COMMAND)
pprint(result)
