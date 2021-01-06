import pytest
import task_24_2
from netmiko.cisco.cisco_ios import CiscoIosSSH
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_24_2, "MyNetmiko")


def test_class_inheritance(first_router_from_devices_yaml):
    r1 = task_24_2.MyNetmiko(**first_router_from_devices_yaml)
    assert isinstance(r1, CiscoIosSSH), "Класс MyNetmiko должен наследовать CiscoIosSSH"
    r1.disconnect()
    check_attr_or_method(r1, method="send_command")
    check_attr_or_method(r1, method="send_config_set")


def test_enable(first_router_from_devices_yaml):
    r1 = task_24_2.MyNetmiko(**first_router_from_devices_yaml)
    output = r1.send_command("sh run | i hostname")
    r1.disconnect()
    assert (
        "hostname" in output
    ), "При создании экземпляра класса должно создаваться подключение и переход в режим enable"
