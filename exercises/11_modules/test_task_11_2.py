import pytest
import task_11_2
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
    check_function_exists(task_11_2, "create_network_map")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_11_2.create_network_map, param_count=1, param_names=["filenames"]
    )


def test_function_return_value():
    """
    Проверка работы функции
    """
    sh_cdp_n_sw1 = (
        "SW1>show cdp neighbors\n\n"
        "Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\n"
        "                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone\n\n"
        "Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID\n"
        "R1           Eth 0/1         122           R S I           2811       Eth 0/0\n"
        "R2           Eth 0/2         143           R S I           2811       Eth 0/0\n"
        "R3           Eth 0/3         151           R S I           2811       Eth 0/0\n"
        "R6           Eth 0/5         121           R S I           2811       Eth 0/1"
    )
    correct_return_value = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("R6", "Eth0/1"): ("SW1", "Eth0/5"),
    }

    return_value = task_11_2.create_network_map(
        ['sh_cdp_n_r2.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_sw1.txt', 'sh_cdp_n_r3.txt']
    )
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert len(return_value) == len(
        correct_return_value
    ), "В словаре, который описывает топологию есть дублирующиеся линки"
    unified_return_value = unify_topology_dict(return_value)
    assert (
        unified_return_value == correct_return_value
    ), "Функция возвращает неправильное значение"
