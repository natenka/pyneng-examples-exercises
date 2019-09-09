from netmiko.cisco.cisco_ios import CiscoIosBase

device_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}

### Базовый пример наследования

class MyNetmiko(CiscoIosBase):
    pass


r1 = MyNetmiko(**device_params)
print(r1.send_command('sh ip int br'))

### Добавление метода

class MyNetmiko(CiscoIosBase):
    def say_hello(self):
        print('Hello from', self.ip)


r1 = MyNetmiko(**device_params)
print(r1.send_command('sh ip int br'))
r1.say_hello()

### Переопределение родительского метода

class MyNetmiko(CiscoIosBase):
    def send_command(self, command, *args, **kwargs):
        command_output = super().send_command(command, *args, **kwargs)
        print('Вывод команды:')
        return command_output

    def say_hello(self):
        print('Hello from', self.ip)


r1 = MyNetmiko(**device_params)
print(r1.send_command('sh ip int br', strip_command=False))


### Добавление дополнительного функционала
class ErrorInCommand(Exception):
    pass

class MyNetmiko(CiscoIosBase):
    def send_command(self, command, *args, **kwargs):
        command_output = super().send_command(command, *args, **kwargs)
        if 'Invalid input' in command_output:
            raise ErrorInCommand('Ошибка в команде {}'.format(command))
        return command_output

    def say_hello(self):
        print('Hello from', self.ip)


r1 = MyNetmiko(**device_params)

try:
    r1.send_command('sh ip br', strip_command = False)
except ErrorInCommand as e:
    print(e)


