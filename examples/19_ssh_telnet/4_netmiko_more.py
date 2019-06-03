from netmiko import ConnectHandler, NetMikoTimeoutException


def send_command_netmiko(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        ssh.send_command('terminal length 40')
        ssh.write_channel(command+'\n')

        result = ''
        while True:
            try:
                page = ssh.read_until_pattern('More|end')
            except NetMikoTimeoutException:
                break
            result += page
            if 'More' in page:
                ssh.write_channel(' ')
    return result


device_dict = {'device_type':'cisco_ios',
               'username': 'cisco',
               'password': 'cisco',
               'secret': 'cisco',
               'ip': '192.168.100.1' }


if __name__ == "__main__":
    command = 'sh run'
    result = send_command_netmiko(device_dict, 'sh run')
    print(result)

