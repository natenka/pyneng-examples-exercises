import pytest
import task_11_2a
import glob
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_function_exists,
    check_function_params,
    unify_topology_dict,
)

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_11_2a, "unique_network_map")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_11_2a.unique_network_map,
        param_count=1,
        param_names=["topology_dict"],
    )


def test_function_return_value():
    """
    Проверка работы функции
    """
    input_value = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
        ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
    }
    correct_return_value = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("R6", "Eth0/1"): ("SW1", "Eth0/5"),
    }

    return_value = task_11_2a.unique_network_map(input_value)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert len(correct_return_value) == len(
        return_value
    ), "В словаре, который описывает топологию есть дублирующиеся линки"
    unified_return_value = unify_topology_dict(return_value)
    assert (
        correct_return_value == unified_return_value
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args():
    """
    Проверка работы функции на другом выводе
    """
    input_value = {
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("R4", "Eth0/0"): ("R3", "Eth0/1"),
        ("R5", "Eth0/0"): ("R3", "Eth0/2"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    }
    correct_return_value = {
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    }

    return_value = task_11_2a.unique_network_map(input_value)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert len(correct_return_value) == len(
        return_value
    ), "В словаре, который описывает топологию есть дублирующиеся линки"
    unified_return_value = unify_topology_dict(return_value)
    assert (
        correct_return_value == unified_return_value
    ), "Функция возвращает неправильное значение"
