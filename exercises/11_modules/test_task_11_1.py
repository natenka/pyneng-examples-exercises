import pytest
import task_11_1
import sys

sys.path.append("..")

from common_functions import check_function_exists, check_function_params

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_11_1, "parse_cdp_neighbors")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_11_1.parse_cdp_neighbors,
        param_count=1,
        param_names=["command_output"],
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
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
        ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
    }

    return_value = task_11_1.parse_cdp_neighbors(sh_cdp_n_sw1)
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
    sh_cdp_n_r3 = (
        "R3>show cdp neighbors\n"
        "Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\n"
        "                  S - Switch, H - Host, I - IGMP, r - Repeater\n\n"
        "Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID\n"
        "SW1              Eth 0/0            131          S I      WS-C3750- Eth 0/3\n"
        "R4               Eth 0/1            145        R S I      2811      Eth 0/0\n"
        "R5               Eth 0/2            123        R S I      2811      Eth 0/0\n"
    )
    correct_return_value = {
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    }

    return_value = task_11_1.parse_cdp_neighbors(sh_cdp_n_r3)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"
