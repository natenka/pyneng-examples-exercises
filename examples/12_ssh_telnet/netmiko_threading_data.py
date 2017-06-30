# -*- coding: utf-8 -*-
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

    #Добавляем словарь в очередь
    queue.put({ device_dict['ip']: result })


def conn_threads(function, devices, command):
    threads = []
    q = Queue()

    for device in devices:
        # Передаем очередь как аргумент, функции
        th = threading.Thread(target = function, args = (device, command, q))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    results = []
    # Берем результаты из очереди и добавляем их в список results
    for t in threads:
        results.append(q.get())

    return results

print conn_threads(connect_ssh, devices['routers'], COMMAND)
