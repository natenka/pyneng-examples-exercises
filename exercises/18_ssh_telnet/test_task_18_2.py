import pytest
import task_18_2
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, strip_empty_lines

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_18_2, "send_config_commands")


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    Проверка работы функции
    """
    test_commands = [
        "logging 10.255.255.1",
        "logging buffered 20010",
        "no logging console",
    ]
    correct_return_value = strip_empty_lines(
        r1_test_connection.send_config_set(test_commands)
    )
    return_value = strip_empty_lines(
        task_18_2.send_config_commands(first_router_from_devices_yaml, test_commands)
    )
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == str
    ), f"По заданию функция должна возвращать строку, а возвращает {type(return_value).__name__}"
    assert (
        correct_return_value == return_value
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args(
    r1_test_connection, first_router_from_devices_yaml
):
    """
    Проверка работы функции с другими аргументами
    """
    test_commands = [
        "interface Loopback 100",
        "ip address 10.1.1.100 255.255.255.255",
    ]
    correct_return_value = strip_empty_lines(
        r1_test_connection.send_config_set(test_commands)
    )
    return_value = strip_empty_lines(
        task_18_2.send_config_commands(first_router_from_devices_yaml, test_commands)
    )
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == str
    ), f"По заданию функция должна возвращать строку, а возвращает {type(return_value).__name__}"
    assert (
        correct_return_value == return_value
    ), "Функция возвращает неправильное значение"
