import getpass
import sys
import re

from netmiko import ConnectHandler


def cfg_comand(session, section, command):
    cfg = session.send_command('sh run')
    regex = '{}\n( .*\n)* {}'.format(section, command)
    match = re.search(regex, cfg)
    if match:
        print('Команды уже настроены')
        return

    result=session.send_config_set([section, command])
    return result


device_params = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': user,
    'password': password,
    'secret': enable_pass
}

if __name__ == "__main__":
    with ConnectHandler(**device_params) as ssh:
        ssh.enable()
        cfg_comand(ssh, 'interface Loopback55', 'ip address 5.5.5.5 255.255.255.255')
