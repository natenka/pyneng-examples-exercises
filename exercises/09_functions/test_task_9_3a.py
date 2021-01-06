import pytest
import task_9_3a
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_9_3a, "get_int_vlan_map")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_9_3a.get_int_vlan_map,
        param_count=1,
        param_names=["config_filename"],
    )


def test_function_return_value():
    """
    Проверка работы функции
    """
    correct_return_value = (
        {
            "FastEthernet0/0": 10,
            "FastEthernet0/2": 20,
            "FastEthernet1/0": 20,
            "FastEthernet1/1": 30,
            "FastEthernet1/3": 1,
            "FastEthernet2/0": 1,
            "FastEthernet2/1": 1,
        },
        {
            "FastEthernet0/1": [100, 200],
            "FastEthernet0/3": [100, 300, 400, 500, 600],
            "FastEthernet1/2": [400, 500, 600],
        },
    )

    return_value = task_9_3a.get_int_vlan_map("config_sw2.txt")
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == tuple
    ), f"По заданию функция должна возвращать кортеж, а возвращает {type(return_value).__name__}"
    assert len(return_value) == 2 and all(
        type(item) == dict for item in return_value
    ), "Функция должна возвращать кортеж с двумя словарями"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"
