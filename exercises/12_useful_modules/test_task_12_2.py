import pytest
import task_12_2
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_12_2, "convert_ranges_to_ip_list")


def test_function_return_value():
    """
    Проверка работы функции
    """
    list_of_ips_and_ranges = ["8.8.4.4", "1.1.1.1-3", "172.21.41.128-172.21.41.132"]
    correct_return_value = [
        "8.8.4.4",
        "1.1.1.1",
        "1.1.1.2",
        "1.1.1.3",
        "172.21.41.128",
        "172.21.41.129",
        "172.21.41.130",
        "172.21.41.131",
        "172.21.41.132",
    ]

    return_value = task_12_2.convert_ranges_to_ip_list(list_of_ips_and_ranges)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    assert (
        sorted(return_value) == sorted(correct_return_value)
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args():
    """
    Проверка работы функции на других адресах
    """
    list_of_ips_and_ranges = ["10.1.1.1", "10.4.10.10-13", "192.168.1.12-192.168.1.15"]
    correct_return_value = [
        "10.1.1.1",
        "10.4.10.10",
        "10.4.10.11",
        "10.4.10.12",
        "10.4.10.13",
        "192.168.1.12",
        "192.168.1.13",
        "192.168.1.14",
        "192.168.1.15",
    ]

    return_value = task_12_2.convert_ranges_to_ip_list(list_of_ips_and_ranges)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        sorted(return_value) == sorted(correct_return_value)
    ), "Функция возвращает неправильное значение"
