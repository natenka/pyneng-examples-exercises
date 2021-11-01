import sys

import task_24_2a
import task_24_2c
from netmiko.cisco.cisco_ios import CiscoIosSSH

sys.path.append("..")

from pyneng_common_functions import (check_attr_or_method, check_class_exists,
                                     check_pytest)

check_pytest(__loader__, __file__)


def test_class_created():
    check_class_exists(task_24_2c, "MyNetmiko")


def test_class_inheritance(first_router_from_devices_yaml):
    ssh = task_24_2c.MyNetmiko(**first_router_from_devices_yaml)
    ssh.disconnect()
    assert isinstance(
        ssh, CiscoIosSSH
    ), "Класс MyNetmiko должен наследовать CiscoIosSSH"
    check_attr_or_method(ssh, method="send_command")


def test_netmiko_args(first_router_from_devices_yaml):
    ssh = task_24_2c.MyNetmiko(**first_router_from_devices_yaml)
    command = "sh version"
    output_with_command = ssh.send_command(command, strip_command=False)
    assert command in output_with_command
    output_without_command = ssh.send_command(command, strip_command=True)
    ssh.disconnect()
    assert command not in output_without_command
