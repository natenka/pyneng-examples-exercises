import sys

import task_15_1b

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_pytest


check_pytest(__loader__, __file__)


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_15_1b, "get_ip_from_cfg")


def test_function_return_value():
    """
    Проверка работы функции
    """
    correct_return_value = {
        "Loopback0": [("10.2.2.2", "255.255.255.255")],
        "Ethernet0/0": [("10.0.23.2", "255.255.255.0")],
        "Ethernet0/1": [
            ("10.255.2.2", "255.255.255.0"),
            ("10.254.2.2", "255.255.255.0"),
        ],
        "Ethernet0/2": [("10.0.29.2", "255.255.255.0")],
    }

    return_value = task_15_1b.get_ip_from_cfg("config_r2.txt")
    assert return_value is not None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert (
        correct_return_value == return_value
    ), "Функция возвращает неправильное значение"
