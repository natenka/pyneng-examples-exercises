import paramiko
import time
import socket
from pprint import pprint


def send_show_command(
    ip,
    username,
    password,
    enable,
    command,
    prompt="#",
    wait_for_recv=5,
    max_bytes=60000,
    short_pause=1,
    long_pause=5,
):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(
        hostname=ip,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    with cl.invoke_shell() as ssh:
        ssh.send("enable\n")
        ssh.send(enable + "\n")
        time.sleep(short_pause)
        ssh.send("terminal length 0\n")
        time.sleep(short_pause)
        ssh.recv(max_bytes)

        result = {}
        ssh.send(f"{command}\n")
        ssh.settimeout(wait_for_recv)

        output = ""
        while True:
            try:
                part = ssh.recv(20).decode("utf-8")
                output += part
                print(part)
                if prompt in part:
                    break
                time.sleep(0.5)
            except socket.timeout:
                break
        return output


if __name__ == "__main__":
    devices = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    commands = ["sh clock", "sh arp"]
    result = send_show_command(
        "192.168.100.1", "cisco", "cisco", "cisco", "ping 10.1.1.1 repeat 20"
    )
    pprint(result, width=120)
