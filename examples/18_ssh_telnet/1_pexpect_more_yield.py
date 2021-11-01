import re
import time

import pexpect


def connect_ssh_cisco_ios(command, ip, username, password, enable, disable_paging=True):
    print("Connection to device {}".format(ip))
    with pexpect.spawn("ssh {}@{}".format(username, ip)) as ssh:

        ssh.expect("Password:")
        ssh.sendline(password)

        ssh.expect("[#>]")
        ssh.sendline("enable")

        ssh.expect("Password:")
        ssh.sendline(enable)

        if disable_paging:
            ssh.expect("#")
            ssh.sendline("terminal length 0")

            ssh.expect("#")
            ssh.sendline(command)

            ssh.expect("#")
            return ssh.before.decode("ascii")

        ssh.expect("#")
        ssh.sendline(command)

        while True:
            time.sleep(0.1)
            match = ssh.expect(["--More--", "#"], timeout=5)
            page = ssh.before.decode("ascii")
            page = re.sub("\x08+", "\n", page)
            yield page
            if match == 1:
                break
            ssh.send(" ")


if __name__ == "__main__":
    command = "sh run"
    r1 = "192.168.100.1"
    result = connect_ssh_cisco_ios(
        command, r1, "cisco", "cisco", "cisco", disable_paging=False
    )
    with open("result.txt", "w") as f:
        for page in result:
            f.write(page)
