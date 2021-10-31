import sys

import pytest
from base_connect_class import BaseSSH
from netmiko.ssh_exception import SSHException

try:
    import task_24_1a
except OSError:
    pytest.fail(
        "Для этого задания функцию надо ОБЯЗАТЕЛЬНО вызывать в блоке if __name__ == '__main__':"
    )

sys.path.append("..")

from pyneng_common_functions import (check_attr_or_method, check_class_exists,
                                     check_pytest)

check_pytest(__loader__, __file__)


def test_class_created():
    check_class_exists(task_24_1a, "CiscoSSH")


def test_class_inheritance(first_router_from_devices_yaml):
    ssh = task_24_1a.CiscoSSH(**first_router_from_devices_yaml)
    ssh.ssh.disconnect()
    assert isinstance(ssh, BaseSSH), "Класс CiscoSSH должен наследовать BaseSSH"
    check_attr_or_method(ssh, method="send_show_command")
    check_attr_or_method(ssh, method="send_cfg_commands")


def test_params_without_password(first_router_from_devices_yaml, monkeypatch):
    params = first_router_from_devices_yaml.copy()
    password = first_router_from_devices_yaml.get("password")
    del params["password"]
    monkeypatch.setattr("builtins.input", lambda x=None: password)
    try:
        ssh = task_24_1a.CiscoSSH(**params)
        ssh.ssh.disconnect()
    except SSHException:
        pytest.fail("Ошибка при подключении")
