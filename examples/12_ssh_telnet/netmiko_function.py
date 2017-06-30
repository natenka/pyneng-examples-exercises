from netmiko import ConnectHandler
import sys
import yaml

COMMAND = sys.argv[1]
devices = yaml.load(open('devices.yaml'))

def connect_ssh(device_dict, command):

    print "Connection to device %s" % device_dict['ip']

    ssh = ConnectHandler(**device_dict)
    ssh.enable()

    result = ssh.send_command(command)
    print result

for router in devices['routers']:
    connect_ssh(router, COMMAND)
