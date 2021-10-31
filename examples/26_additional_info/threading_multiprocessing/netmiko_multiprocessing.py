import multiprocessing
import sys
from pprint import pprint

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
        queue.put({device_dict['ip']: result})


def conn_processes(function, devices, command):
    processes = []
    queue = multiprocessing.Queue()

    for device in devices:
        p = multiprocessing.Process(
            target=function, args=(device, command, queue))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    results = []
    for p in processes:
        results.append(queue.get())

    return results


pprint(conn_processes(connect_ssh, devices['routers'], COMMAND))
