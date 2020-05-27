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
        "templates/ospf.txt"
    ), "Шаблон templates/ospf.txt не существует"


def test_function_return_value():
    correct_return_value_router = (
        "router ospf 10\n"
        "router-id 10.0.0.1\n"
        "auto-cost reference-bandwidth 20000\n"
        "network 10.255.0.1 0.0.0.0 area 0\n"
        "network 10.255.1.1 0.0.0.0 area 0\n"
        "network 10.255.2.1 0.0.0.0 area 0\n"
        "network 10.0.10.1 0.0.0.0 area 2\n"
        "network 10.0.20.1 0.0.0.0 area 2\n"
        "passive-interface Fa0/0.10\n"
        "passive-interface Fa0/0.20\n"
    )
    correct_return_value_intf = (
        "interface Fa0/1\n"
        "ip ospf hello-interval 1\n"
        "interface Fa0/1.100\n"
        "ip ospf hello-interval 1\n"
        "interface Fa0/1.200\n"
        "ip ospf hello-interval 1\n"
    )

    template = "templates/ospf.txt"
    data = {
        "ospf_intf": [
            {"area": 0, "ip": "10.255.0.1", "name": "Fa0/1", "passive": False},
            {"area": 0, "ip": "10.255.1.1", "name": "Fa0/1.100", "passive": False},
            {"area": 0, "ip": "10.255.2.1", "name": "Fa0/1.200", "passive": False},
            {"area": 2, "ip": "10.0.10.1", "name": "Fa0/0.10", "passive": True},
            {"area": 2, "ip": "10.0.20.1", "name": "Fa0/0.20", "passive": True},
        ],
        "process": 10,
        "ref_bw": 20000,
        "router_id": "10.0.0.1",
    }

    return_value = task_21_1.generate_config(template, data)
    correct_lines_router = set(correct_return_value_router.splitlines())
    correct_lines_interface = set(correct_return_value_intf.splitlines())

    return_value = strip_empty_lines(return_value)
    return_lines = set(return_value.splitlines())

    # проверяем что строки из correct_return_value_router содержатся в return_value
    assert correct_lines_router.issubset(
        return_lines
    ), "В итоговой конфигурации режима router ospf не все строки"
    # проверяем что строки из correct_return_value_intf содержатся в return_value
    assert correct_lines_interface.issubset(
        return_lines
    ), "В итоговой конфигурации интерфейсов не все строки"
