import pytest

try:
    import task_24_1a
except OSError:
    pytest.fail(
        "Для этого задания функцию надо ОБЯЗАТЕЛЬНО вызывать в блоке if __name__ == '__main__':"
    )

from base_connect_class import BaseSSH
from netmiko.ssh_exception import SSHException
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_24_1a, "CiscoSSH")


def test_class_inheritance(first_router_from_devices_yaml):
    r1 = task_24_1a.CiscoSSH(**first_router_from_devices_yaml)
    r1.ssh.disconnect()
    assert isinstance(r1, BaseSSH), "Класс CiscoSSH должен наследовать BaseSSH"
    check_attr_or_method(r1, method="send_show_command")
    check_attr_or_method(r1, method="send_cfg_commands")


def test_params_without_password(first_router_from_devices_yaml, monkeypatch):
    params = first_router_from_devices_yaml.copy()
    password = first_router_from_devices_yaml.get("password")
    del params["password"]
    monkeypatch.setattr("builtins.input", lambda x=None: password)
    try:
        r1 = task_24_1a.CiscoSSH(**params)
        r1.ssh.disconnect()
    except SSHException:
        pytest.fail("Ошибка при подключении")
