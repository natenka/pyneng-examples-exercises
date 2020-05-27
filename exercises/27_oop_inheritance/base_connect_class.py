import netmiko


class BaseSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)

    def send_show_command(self, command):
        return self.ssh.send_command(command)

    def send_cfg_commands(self, commands):
        return self.ssh.send_config_set(commands)
