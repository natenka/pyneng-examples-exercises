from concurrent.futures import ThreadPoolExecutor
from pprint import pprint

import yaml
from netmiko import ConnectHandler


def connect_ssh(device_dict, command='sh clock'):
    print('Connection to device: {}'.format(device_dict['ip']))
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return {device_dict['ip']: result}


def threads_conn(function, devices, limit=2):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        f_result = executor.map(function, devices)
    return list(f_result)


if __name__ == '__main__':
    devices = yaml.load(open('devices.yaml'))
    all_done = threads_conn(connect_ssh, devices['routers'])
    pprint(all_done)
