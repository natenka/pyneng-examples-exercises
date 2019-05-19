import subprocess


def ping_ip(ip_address):
    reply = subprocess.run(
        ['ping', '-c', '3', '-n', ip_address],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if reply.returncode == 0:
        return True
    else:
        return False


ip1 = '8.8.8.8'
ip2 = '10.2.2'

print('Ping ip...')
print(ip1, ping_ip(ip1))
print(ip2, ping_ip(ip2))
