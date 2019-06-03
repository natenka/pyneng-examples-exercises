from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat

import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException, SSHException

start_msg = '===> {} Connection to device: {}'
received_msg = '<=== {} Received result from device: {}'


def connect_ssh(device_dict, command):
    print(start_msg.format(datetime.now().time(), device_dict['ip']))
    try:
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            print(received_msg.format(datetime.now().time(), device_dict['ip']))
        return device_dict['ip'], result
    except SSHException as exc:
        return device_dict['ip'], exc


def threads_conn(function, devices, limit=2, command=''):
    all_results = {}
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ssh = [
            executor.submit(function, device, command) for device in devices
        ]
        for f in as_completed(future_ssh):
            print(f)
            ip, result = f.result()
            all_results.update({ip: result})
            if isinstance(result, Exception):
                break
        print('-'*40)
        for f in reversed(future_ssh):
            if not f.cancel():
                ip, result = f.result()
                all_results.update({ip: result})
            print(f)
    return all_results


if __name__ == '__main__':
    devices = yaml.load(open('devices.yaml'))
    all_done = threads_conn(
        connect_ssh, devices, command='sh clock')
    pprint(all_done)
