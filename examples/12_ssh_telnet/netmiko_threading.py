from netmiko import ConnectHandler
import sys
import yaml
import threading

COMMAND = sys.argv[1]
devices = yaml.load(open('devices.yaml'))

def connect_ssh(device_dict, command):
    ssh = ConnectHandler(**device_dict)
    ssh.enable()
    result = ssh.send_command(command)

    print "Connection to device %s" % device_dict['ip']
    print result


def conn_threads(function, devices, command):
    threads = []
    for device in devices:
        th = threading.Thread(target = function, args = (device, command))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

conn_threads(connect_ssh, devices['routers'], COMMAND)
