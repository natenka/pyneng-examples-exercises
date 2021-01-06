import pytest
import task_15_2
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
    check_function_exists(task_15_2, "parse_sh_ip_int_br")


def test_function_return_value():
    """
    Проверка работы функции
    """
    correct_return_value = [
        ("FastEthernet0/0", "15.0.15.1", "up", "up"),
        ("FastEthernet0/1", "10.0.12.1", "up", "up"),
        ("FastEthernet0/2", "10.0.13.1", "up", "up"),
        ("FastEthernet0/3", "unassigned", "administratively down", "down"),
        ("Loopback0", "10.1.1.1", "up", "up"),
        ("Loopback100", "100.0.0.1", "up", "up"),
    ]

    return_value = task_15_2.parse_sh_ip_int_br("sh_ip_int_br.txt")
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    # Списки сортируются чтобы не было ошибки, если строки записаны в списке в другом порядке
    # В этом задании порядок кортежей в списке не важен
    assert sorted(return_value) == sorted(
        correct_return_value
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args():
    """
    Проверка работы функции с другими аргументами
    """
    correct_return_value = [
        ("FastEthernet0/0", "15.0.15.2", "up", "up"),
        ("FastEthernet0/1", "10.0.12.2", "up", "up"),
        ("FastEthernet0/2", "10.0.13.2", "down", "down"),
        ("FastEthernet0/3", "unassigned", "administratively down", "down"),
        ("Loopback0", "10.2.2.2", "up", "up"),
    ]

    return_value = task_15_2.parse_sh_ip_int_br("sh_ip_int_br_2.txt")
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    # Списки сортируются чтобы не было ошибки, если строки записаны в списке в другом порядке
    # В этом задании порядок кортежей в списке не важен
    assert sorted(return_value) == sorted(
        correct_return_value
    ), "Функция возвращает неправильное значение"
