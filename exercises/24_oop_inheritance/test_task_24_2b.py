import pytest
import task_24_2b
from netmiko.cisco.cisco_ios import CiscoIosSSH
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_24_2b, "MyNetmiko")


def test_class_inheritance(first_router_from_devices_yaml):
    r1 = task_24_2b.MyNetmiko(**first_router_from_devices_yaml)
    r1.disconnect()
    assert isinstance(r1, CiscoIosSSH), "Класс MyNetmiko должен наследовать CiscoIosSSH"
    check_attr_or_method(r1, method="send_command")
    check_attr_or_method(r1, method="_check_error_in_command")


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "logging 0255.255.1"),
        ("Incomplete command", "lo"),
        ("Ambiguous command", "a"),
    ],
)
def test_errors(first_router_from_devices_yaml, command, error):
    r1 = task_24_2b.MyNetmiko(**first_router_from_devices_yaml)
    with pytest.raises(Exception) as excinfo:
        return_value = r1.send_config_set(command)
        r1.disconnect()
    assert error in str(
        excinfo
    ), "Метод send_config_commands должен генерировать исключение, когда команда выполнена с ошибкой"
