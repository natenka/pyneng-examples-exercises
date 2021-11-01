from pprint import pprint

import yaml
from netmiko import (ConnectHandler, NetmikoAuthenticationException,
                     NetmikoTimeoutException)


def send_show_command(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        result = send_show_command(device, ["sh clock", "sh ip int br"])
        pprint(result, width=120)
