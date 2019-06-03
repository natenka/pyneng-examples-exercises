import pexpect
import getpass
import sys


command = sys.argv[1]
user = input('Username: ')
password = getpass.getpass()
enable_pass = getpass.getpass(prompt='Enter enable password: ')

devices_ip = ['192.168.100.1', '192.168.100.2', '192.168.100.3']

for ip in devices_ip:
    print('Connection to device {}'.format(ip))
    with pexpect.spawn('ssh {}@{}'.format(user, ip)) as ssh:

        ssh.expect('Password:')
        ssh.sendline(password)

        ssh.expect('[#>]')
        ssh.sendline('enable')

        ssh.expect('Password:')
        ssh.sendline(enable_pass)

        ssh.expect('#')
        ssh.sendline('terminal length 0')

        ssh.expect('#')
        ssh.sendline(command)

        ssh.expect('#')
        print(ssh.before.decode('ascii'))
