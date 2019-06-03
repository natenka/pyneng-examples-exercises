import telnetlib
import time


def send_command_telnetlib(ipaddress, username, password, enable_pass, command):
    t = telnetlib.Telnet('192.168.100.1')

    t.read_until(b'Username:')
    t.write(username.encode('ascii') + b'\n')

    t.read_until(b'Password:')
    t.write(password.encode('ascii') + b'\n')
    t.write(b'enable\n')

    t.read_until(b'Password:')
    t.write(enable_pass.encode('ascii') + b'\n')

    t.read_until(b'#')

    t.write(command.encode('ascii') + b'\n')
    result = ''

    while True:
        index, match, output = t.expect([b'--More--', b'#'], timeout=5)
        result += output.decode('ascii')
        if index == 1:
            break
        t.write(b' ')
        time.sleep(1)

    return result


if __name__ == "__main__":
    command = 'sh run'
    user = password = enable_pass = 'cisco'
    ip = '192.168.100.1'

    print(send_command_telnetlib(ip, user, password, enable_pass, 'sh run'))

