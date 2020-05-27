import pytest
import task_22_3
import sys

sys.path.append("..")

from common_functions import check_function_exists

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_22_3, "parse_command_dynamic")


def test_function_return_value():
    """
    Проверка работы функции
    """
    correct_return_value = [
        {
            "address": "15.0.15.1",
            "intf": "FastEthernet0/0",
            "protocol": "up",
            "status": "up",
        },
        {
            "address": "10.0.12.1",
            "intf": "FastEthernet0/1",
            "protocol": "up",
            "status": "up",
        },
        {
            "address": "10.0.13.1",
            "intf": "FastEthernet0/2",
            "protocol": "up",
            "status": "up",
        },
        {
            "address": "unassigned",
            "intf": "FastEthernet0/3",
            "protocol": "up",
            "status": "up",
        },
        {"address": "10.1.1.1", "intf": "Loopback0", "protocol": "up", "status": "up"},
        {
            "address": "100.0.0.1",
            "intf": "Loopback100",
            "protocol": "up",
            "status": "up",
        },
    ]
    with open("output/sh_ip_int_br.txt") as f:
        sh_ip_int_br = f.read()
    attributes = {"Command": "show ip int br", "Vendor": "cisco_ios"}

    return_value = task_22_3.parse_command_dynamic(sh_ip_int_br, attributes)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args():
    """
    Проверка работы функции с другими аргументами
    """
    correct_return_value = [
        {
            "hostname": "R1_LONDON",
            "uptime": "1 day, 15 hours, 32 minutes",
            "version": "15.3(2)S1",
        }
    ]
    with open("output/sh_version.txt") as f:
        sh_version = f.read()
    attributes = {"Command": "show version", "Vendor": "cisco_ios"}

    return_value = task_22_3.parse_command_dynamic(sh_version, attributes)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"
