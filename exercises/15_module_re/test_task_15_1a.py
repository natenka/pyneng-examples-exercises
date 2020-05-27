import pytest
import task_15_1a
import sys

sys.path.append("..")

from common_functions import check_function_exists

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_15_1a, "get_ip_from_cfg")


def test_function_return_value():
    """
    Проверка работы функции
    """
    correct_return_value = {
        "Loopback0": ("10.1.1.1", "255.255.255.255"),
        "Ethernet0/0": ("10.0.13.1", "255.255.255.0"),
        "Ethernet0/2": ("10.0.19.1", "255.255.255.0"),
    }

    return_value = task_15_1a.get_ip_from_cfg("config_r1.txt")
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args():
    """
    Проверка работы функции с другими аргументами
    """
    correct_return_value = {
        "Loopback0": ("10.3.3.3", "255.255.255.255"),
        "Ethernet0/0": ("10.0.13.3", "255.255.255.0"),
    }

    return_value = task_15_1a.get_ip_from_cfg("config_r3.txt")
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"
