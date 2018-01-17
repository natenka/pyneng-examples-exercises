import getpass
import sys
import time

from netmiko import ConnectHandler

COMMAND = sys.argv[1]
USER = input('Username: ')
PASSWORD = getpass.getpass()
ENABLE_PASS = getpass.getpass(prompt='Enter enable password: ')

DEVICES_IP = ['192.168.100.1', '192.168.100.2', '192.168.100.3']

for IP in DEVICES_IP:
    print('Connection to device {}'.format(IP))
    DEVICE_PARAMS = {
        'device_type': 'cisco_ios_telnet',
        'ip': IP,
        'username': USER,
        'password': PASSWORD,
        'secret': ENABLE_PASS,
        'verbose': True
    }
    with ConnectHandler(**DEVICE_PARAMS) as telnet:
        telnet.enable()

        result = telnet.send_command(COMMAND)
        print(result)
