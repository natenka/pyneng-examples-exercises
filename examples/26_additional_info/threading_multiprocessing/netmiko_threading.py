import sys
import yaml
import threading

from netmiko import ConnectHandler

COMMAND = sys.argv[1]
with open('devices.yaml') as f:
    devices = yaml.safe_load(f)


def connect_ssh(device_dict, command):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)

        print('Connection to device {}'.format(device_dict['ip']))
        print(result)


def conn_threads(function, devices, command):
    threads = []
    for device in devices:
        th = threading.Thread(target=function, args=(device, command))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


conn_threads(connect_ssh, devices['routers'], COMMAND)
