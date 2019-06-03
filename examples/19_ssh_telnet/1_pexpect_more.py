import pexpect
import re


def send_command_pexpect(ipaddress, username, password, enable_pass, command):
    print('Connection to device {}'.format(ipaddress))
    with pexpect.spawn('ssh {}@{}'.format(username, ipaddress), timeout=10) as ssh:

        ssh.expect('Password:')
        ssh.sendline(password)

        ssh.expect('[#>]')
        ssh.sendline('enable')

        output = ssh.expect(['[#>]', '[Pp]assword:'])
        if output == 1:
            ssh.sendline(enable_pass)
            ssh.expect('#')

        ssh.sendline(command)
        command_output= ''

        while True:
            match = ssh.expect(['--More--', '#', pexpect.TIMEOUT])
            page = ssh.before.decode('ascii')
            # delete backspace
            page = re.sub('\x08+', '\n', page)
            command_output += page
            if match == 1:
                break
            elif match == 2:
                print('Timeout')
                break
            ssh.send(' ')

    return command_output


if __name__ == '__main__':
    command = 'sh run'
    user = password = enable_pass = 'cisco'
    ip = '192.168.100.1'

    result = send_command_pexpect(ip, user, password, enable_pass, 'sh run')
    with open('result.txt', 'w') as f:
        f.write(result)

