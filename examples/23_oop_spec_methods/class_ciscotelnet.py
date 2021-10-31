import telnetlib
import time


class CiscoTelnet:
    """Подключение к циско по телнет"""
    def __init__(self, ip, username, password, enable, disable_paging=True):
        """Инициализация экземпляра"""
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b'Username:')
        self.telnet.write(username.encode('utf-8') + b'\n')
        self.telnet.read_until(b'Password:')
        self.telnet.write(password.encode('utf-8') + b'\n')
        self.telnet.write(b'enable\n')
        self.telnet.read_until(b'Password:')
        self.telnet.write(enable.encode('utf-8') + b'\n')
        if disable_paging: self.telnet.write(b'terminal length 0\n')
        time.sleep(1)
        self.telnet.read_very_eager()

    def send_show_command(self, command):
        """Отправка команд show"""
        self.telnet.write(command.encode('utf-8') + b'\n')
        time.sleep(2)
        command_output = self.telnet.read_very_eager().decode('utf-8')
        return command_output


if __name__ == '__main__':
    r1 = CiscoTelnet('192.168.100.1', 'cisco', 'cisco', 'cisco')
    print(r1.send_show_command('sh ip int br'))
