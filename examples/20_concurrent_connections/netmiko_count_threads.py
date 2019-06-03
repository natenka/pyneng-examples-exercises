from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat

import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException


def send_show(device_dict, command):
    ip = device_dict['ip']
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return {ip: result}


def send_command_to_devices(devices, command, max_threads=2):
    data = {}
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_ssh = [
            executor.submit(send_show, device, command) for device in devices
        ]
        for f in as_completed(future_ssh):
            result = f.result()
            data.update(result)
    return data


if __name__ == '__main__':
    filename = 'devices_all.yaml'
    min_th, max_th = 3, 9

    with open(filename) as f:
        devices = yaml.load(f, Loader=yaml.FullLoader)
    print('Количество устройств:', len(devices))

    for num_threads in range(min_th, max_th+1):
        print(' {} потоков '.format(num_threads).center(50, '#'))
        start_time = datetime.now()
        all_done = send_command_to_devices(devices, command='sh ip int br', max_threads=num_threads)
        print(datetime.now() - start_time)

