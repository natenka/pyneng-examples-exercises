import paramiko
import time
import paramiko.ssh_exception


def send_command_paramiko(ipaddress, username, password, enable_pass, command):
    print('Connection to device {}'.format(ipaddress))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        hostname=ipaddress,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False)

    with client.invoke_shell() as ssh:
        ssh.settimeout(5)

        ssh.send('enable\n')
        ssh.send(enable_pass + '\n')
        time.sleep(1)

        ssh.recv(1000)
        ssh.send(command + '\n')
        time.sleep(1)

        result = ''
        while True:
            try:
                page = ssh.recv(5000).decode('ascii')
            except paramiko.ssh_exception.socket.timeout:
                break
            result += page
            if 'More' in page:
                ssh.send(' ')

    return result


if __name__ == "__main__":
    command = 'sh run'
    user = password = enable_pass = 'cisco'
    ip = '192.168.100.1'

    result = send_command_paramiko(ip, user, password, enable_pass, 'sh run')
    with open('result.txt', 'w') as f:
        f.write(result)

