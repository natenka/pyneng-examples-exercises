import os
import sys

import task_17_3b

sys.path.append("..")

from pyneng_common_functions import (check_function_exists, check_pytest,
                                     unify_topology_dict)

check_pytest(__loader__, __file__)


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_17_3b, "transform_topology")


def test_function_return_value():
    """
    Проверка работы функции
    """
    correct_return_value = unify_topology_dict(
        {
            ("R1", "Eth 0/0"): ("SW1", "Eth 0/1"),
            ("R2", "Eth 0/0"): ("SW1", "Eth 0/2"),
            ("R2", "Eth 0/1"): ("R5", "Eth 0/0"),
            ("R2", "Eth 0/2"): ("R6", "Eth 0/1"),
            ("R3", "Eth 0/0"): ("SW1", "Eth 0/3"),
            ("R4", "Eth 0/0"): ("SW1", "Eth 0/4"),
            ("R4", "Eth 0/1"): ("R5", "Eth 0/1"),
        }
    )

    assert os.path.exists("topology.yaml"), "Файл topology.yaml не существует"
    return_value = task_17_3b.transform_topology("topology.yaml")
    assert return_value is not None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert len(correct_return_value) == len(
        return_value
    ), "В словаре, который описывает топологию есть дублирующиеся линки"
    assert correct_return_value == unify_topology_dict(
        return_value
    ), "Функция возвращает неправильное значение"
