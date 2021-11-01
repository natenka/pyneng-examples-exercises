import yaml
from netmiko import ConnectHandler

# COMMAND = sys.argv[1]
with open('devices.yaml') as f:
    devices = yaml.safe_load(f)


def connect_ssh(device_dict, commands):

    print('Connection to device {}'.format(device_dict['ip']))

    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()

        result = ssh.send_config_set(commands)
        print(result)


commands_to_send = [
    'logg 10.1.12.3', 'ip access-li ext TESST2', 'permit ip any any'
]

for router in devices['routers']:
    connect_ssh(router, commands_to_send)
