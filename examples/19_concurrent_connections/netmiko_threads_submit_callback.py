import csv
import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pprint import pprint

import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException

logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

start_msg = '===> {} Connection: {}'
received_msg = '<=== {} Received: {}'
parsed_msg = '#### {} Parsed: {}'

def send_show(device_dict, command):
    ip = device_dict['ip']
    logging.info(start_msg.format(datetime.now().time(), ip))
    if ip == '192.168.100.1': time.sleep(5)
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        logging.info(received_msg.format(datetime.now().time(), ip))
    return (ip, result)


def parse_sh_ip_int_br(future):
    regex = (r'(\S+) +([\d.]+) +\w+ +\w+ +'
             r'(up|down|administratively down) +(up|down)')
    ip, output = future.result()
    parsed = [match.groups() for match in re.finditer(regex, output)]
    logging.info(parsed_msg.format(datetime.now().time(), ip))
    with open(f'parsed_{ip}_sh_ip_int_br.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(parsed)


def send_command_to_devices(devices, command, callback=None):
    data = {}
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_ssh = []
        for device in devices:
            future = executor.submit(send_show, device, command)
            if callback:
                future.add_done_callback(callback)
            future_ssh.append(future)
        for f in as_completed(future_ssh):
            ip, result = f.result()
            data[ip] = result
    return data


if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    done = send_command_to_devices(devices, 'sh ip int br', callback=parse_sh_ip_int_br)
    pprint(done, width=120)

