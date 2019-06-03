import subprocess


def ping_ip_addresses(ip_list):
    reachable = []
    unreachable = []
    result = []
    for ip in ip_list:
        p = subprocess.Popen(['ping', '-c', '3', '-n', ip],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        result.append(p)
    for ip, p in zip(ip_list, result):
        returncode = p.wait()
        if returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    return reachable, unreachable


if __name__ == "__main__":
    print(ping_ip_addresses(['8.8.8.8', '192.168.100.22', '192.168.100.1']))
