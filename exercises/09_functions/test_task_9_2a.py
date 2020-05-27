import pytest
import task_9_2a
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
    check_function_exists(task_9_2a, "generate_trunk_config")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_9_2a.generate_trunk_config,
        param_count=2,
        param_names=["intf_vlan_mapping", "trunk_template"],
    )


def test_function_return_value():
    """
    Проверка работы функции
    """
    trunk_vlans_mapping = {
        "FastEthernet0/1": [10, 20, 30],
        "FastEthernet0/2": [11, 30],
        "FastEthernet0/4": [17],
    }
    template_trunk_mode = [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan",
    ]
    correct_return_value = {
        "FastEthernet0/1": [
            "switchport mode trunk",
            "switchport trunk native vlan 999",
            "switchport trunk allowed vlan 10,20,30",
        ],
        "FastEthernet0/2": [
            "switchport mode trunk",
            "switchport trunk native vlan 999",
            "switchport trunk allowed vlan 11,30",
        ],
        "FastEthernet0/4": [
            "switchport mode trunk",
            "switchport trunk native vlan 999",
            "switchport trunk allowed vlan 17",
        ],
    }

    return_value = task_9_2a.generate_trunk_config(
        trunk_vlans_mapping, template_trunk_mode
    )
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == dict
    ), f"По заданию функция должна возвращать словарь, а возвращает {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"
