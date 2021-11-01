from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint

import yaml
from netmiko import ConnectHandler

start_msg = '===> {} Connection to device: {}'
received_msg = '<=== {} Received result from device: {}'


class CiscoSSH:
    def __init__(self, delay_connect=False, **device_dict):
        self.device_dict = device_dict
        if not delay_connect:
            self.ssh = ConnectHandler(**device_dict)
            self.ssh.enable()

    def send_show_command(self, command):
        return self.ssh.send_command(command)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        self.ssh.disconnect()

    def __call__(self, command):
        if not hasattr(self, 'ssh'):
            self.ssh = ConnectHandler(**self.device_dict)
            self.ssh.enable()
        return {self.ssh.ip: self.send_show_command(command)}

    def __repr__(self):
        return 'CiscoSSH({})'.format(self.device_dict['ip'])


def threads_conn(sessions, command, limit=2):
    all_results = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ssh = [
            executor.submit(session, command) for session in sessions
        ]
        for f in as_completed(future_ssh):
            all_results.append(f.result())
    return all_results


if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    instances = [CiscoSSH(delay_connect=True, **device) for device in devices]
    print(instances)
    all_done = threads_conn(instances, command='sh clock')
    pprint(all_done)
