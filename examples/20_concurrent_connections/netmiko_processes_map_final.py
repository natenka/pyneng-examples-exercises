from concurrent.futures import ProcessPoolExecutor
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat

import yaml
from netmiko import ConnectHandler

start_msg = '===> {} Connection to device: {}'
received_msg = '<=== {} Received result from device: {}'


def connect_ssh(device_dict, command):
    print(start_msg.format(datetime.now().time(), device_dict['ip']))
    if device_dict['ip'] == '192.168.100.1':
        time.sleep(10)
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        print(received_msg.format(datetime.now().time(), device_dict['ip']))
    return {device_dict['ip']: result}


def threads_conn(function, devices, limit=2, command=''):
    with ProcessPoolExecutor(max_workers=limit) as executor:
        f_result = executor.map(function, devices, repeat(command))
    return list(f_result)


if __name__ == '__main__':
    devices = yaml.load(open('devices.yaml'))
    all_done = threads_conn(
        connect_ssh, devices['routers'], command='sh clock')
    pprint(all_done)
