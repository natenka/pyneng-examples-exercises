import pytest
import task_17_3
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
    check_function_exists(task_17_3, "parse_sh_cdp_neighbors")


def test_function_return_value():
    """
    Проверка работы функции
    """
    with open("sh_cdp_n_sw1.txt") as f:
        sh_cdp_n_sw1 = f.read()

    correct_return_value = {
        "SW1": {
            "Eth 0/1": {"R1": "Eth 0/0"},
            "Eth 0/2": {"R2": "Eth 0/0"},
            "Eth 0/3": {"R3": "Eth 0/0"},
            "Eth 0/4": {"R4": "Eth 0/0"},
        }
    }

    return_value = task_17_3.parse_sh_cdp_neighbors(sh_cdp_n_sw1)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args():
    """
    Проверка работы функции на другом выводе
    """
    with open("sh_cdp_n_sw1.txt") as f:
        sh_cdp_n_sw1 = f.read()

    correct_return_value = {
        "SW1": {
            "Eth 0/1": {"R1": "Eth 0/0"},
            "Eth 0/2": {"R2": "Eth 0/0"},
            "Eth 0/3": {"R3": "Eth 0/0"},
            "Eth 0/4": {"R4": "Eth 0/0"},
        }
    }

    return_value = task_17_3.parse_sh_cdp_neighbors(sh_cdp_n_sw1)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"
