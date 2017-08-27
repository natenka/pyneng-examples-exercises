from concurrent.futures import ProcessPoolExecutor, as_completed
from pprint import pprint

import yaml
from netmiko import ConnectHandler


def connect_ssh(device_dict, command):
    print('Connection to device {}'.format(device_dict['ip']))
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)

    return {device_dict['ip']: result}


def processes_conn(function, devices, limit=2, **kwargs):
    all_results = {}
    with ProcessPoolExecutor(max_workers=limit) as executor:
        future_ssh = [executor.submit(function, device, **kwargs)
                      for device in devices]
        for f in as_completed(future_ssh):
            all_results.update(f.result())
    return all_results


if __name__ == '__main__':
    devices = yaml.load(open('devices.yaml'))
    all_done = processes_conn(connect_ssh,
                              devices['routers'],
                              limit=3,
                              command='sh ip int br')
    pprint(all_done)

