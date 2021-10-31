import sys

import task_15_5

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_pytest

check_pytest(__loader__, __file__)


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_15_5, "generate_description_from_cdp")


def test_function_return_value():
    """
    Проверка работы функции
    """
    correct_return_value = {
        "Eth 0/1": "description Connected to R1 port Eth 0/0",
        "Eth 0/2": "description Connected to R2 port Eth 0/0",
        "Eth 0/3": "description Connected to R3 port Eth 0/0",
        "Eth 0/5": "description Connected to R6 port Eth 0/1",
    }
    return_value = task_15_5.generate_description_from_cdp("sh_cdp_n_sw1.txt")
    assert return_value is not None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert (
        correct_return_value == return_value
    ), "Функция возвращает неправильное значение"
