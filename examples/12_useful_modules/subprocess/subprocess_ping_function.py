import subprocess


def ping_ip(ip_address):
    '''
    Ping IP address and return tuple:
    On success:
        * True
        * command output (stdout)
    On failure:
        * False
        * error output (stderr)
    '''
    reply = subprocess.run(
        ['ping', '-c', '3', '-n', ip_address],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8')
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stderr


print(ping_ip('8.8.8.8'))
print(ping_ip('a'))
