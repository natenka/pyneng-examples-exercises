# -*- coding: utf-8 -*-
from netmiko import ConnectHandler
import sys
import yaml
import threading

COMMAND = sys.argv[1]
devices = yaml.load(open('devices.yaml'))

def connect_ssh(device_dict, command, queue):
    ssh = ConnectHandler(**device_dict)
    ssh.enable()
    result = ssh.send_command(command)
    print "Connection to device %s" % device_dict['ip']

    #Добавляем словарь в список
    queue.append({ device_dict['ip']: result })


def conn_threads(function, devices, command):
    threads = []
    q = []

    for device in devices:
        # Передаем список как аргумент, функции
        th = threading.Thread(target = function, args = (device, command, q))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    # Эта часть нам не нужна, так как, при использовании списка,
    # мы просто можем вернуть его
    #results = []
    #for t in threads:
    #    results.append(q.get())

    return q

print conn_threads(connect_ssh, devices['routers'], COMMAND)
