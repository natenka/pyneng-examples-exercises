import pexpect
import getpass
import sys


def send_ios_show_pexpect(ip, command, username=None, password=None, enable=None):
    if not username: username = input('Username: ')
    if not password:
        password = getpass.getpass()
    if not enable:
        enable = getpass.getpass(prompt='Enter enable password: ')
    print('Connection to device {}'.format(ip))
    with pexpect.spawn('ssh {}@{}'.format(username, ip), encoding='ascii') as ssh:
        ssh.logfile_read = sys.stdout

        ssh.expect('Password:')
        ssh.sendline(password)

        ssh.expect('[#>]')
        ssh.sendline('enable')

        ssh.expect('Password:')
        ssh.sendline(enable)

        ssh.expect('#')
        ssh.sendline('terminal length 0')

        ssh.expect('#')
        ssh.sendline(command)

        ssh.expect('#')
        return ssh.before


if __name__ == "__main__":
    command = sys.argv[1]
    devices_ip = ['192.168.100.1', '192.168.100.2', '192.168.100.3']
    for ip in devices_ip:
        print(send_ios_show_pexpect(ip, command, *['cisco']*3))

