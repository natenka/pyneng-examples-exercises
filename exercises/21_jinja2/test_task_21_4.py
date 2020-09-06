import os
import pytest
import task_21_1
import sys

sys.path.append("..")

from common_functions import check_function_exists, strip_empty_lines

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_templates_exists():
    assert os.path.exists(
        "templates/add_vlan_to_switch.txt"
    ), "Шаблон templates/add_vlan_to_switch.txt не существует"


def test_function_return_value():
    correct_value_vlan = "vlan 10\n" "name Marketing"
    correct_value_access = (
        "interface Fa0/1\n" "switchport mode access\n" "switchport access vlan 10"
    )
    correct_value_trunk1 = "interface Fa0/23\n" "switchport trunk allowed vlan add 10\n"
    correct_value_trunk2 = "interface Fa0/24\n" "switchport trunk allowed vlan add 10"

    template = "templates/add_vlan_to_switch.txt"
    data = {
        "vlan_id": 10,
        "name": "Marketing",
        "trunk": ["Fa0/23", "Fa0/24"],
        "access": ["Fa0/1"],
    }

    return_value = task_21_1.generate_config(template, data)
    return_value = strip_empty_lines(return_value)

    assert (
        correct_value_vlan in return_value
    ), "В итоговой конфигурации не создан VLAN и/или не назначено имя VLAN"
    assert (
        correct_value_access in return_value
    ), "В итоговой конфигурации неправильная настройка access"
    assert (
        correct_value_trunk1 in return_value and correct_value_trunk2 in return_value
    ), "В итоговой конфигурации неправильная настройка trunk"
