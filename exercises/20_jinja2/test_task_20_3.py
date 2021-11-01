import os
import sys

sys.path.append("..")

from pyneng_common_functions import (check_pytest,
                                     render_jinja_template, strip_empty_lines)

check_pytest(__loader__, __file__)


def test_templates_exists():
    assert os.path.exists(
        "templates/ospf.txt"
    ), "Шаблон templates/ospf.txt не существует"


def test_function_return_value():
    correct_return_value = (
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

    return_value = render_jinja_template(template, data)
    correct_lines = set(correct_return_value.splitlines())
    return_value = strip_empty_lines(return_value)
    return_lines = set(return_value.splitlines())

    assert correct_lines == return_lines, "В итоговой конфигурации ospf не все строки"


def test_function_different_input():
    correct_return_value = (
        "router ospf 1\n"
        "router-id 10.0.0.1\n"
        "auto-cost reference-bandwidth 30000\n"
        "network 10.55.1.1 0.0.0.0 area 0\n"
        "network 10.55.2.1 0.0.0.0 area 5\n"
        "network 10.55.3.1 0.0.0.0 area 5\n"
        "passive-interface Fa0/1.100\n"
        "passive-interface Fa0/1.200\n"
        "passive-interface Fa0/1.300\n"
    )

    template = "templates/ospf.txt"
    data = {
        "ospf_intf": [
            {"area": 0, "ip": "10.55.1.1", "name": "Fa0/1.100", "passive": True},
            {"area": 5, "ip": "10.55.2.1", "name": "Fa0/1.200", "passive": True},
            {"area": 5, "ip": "10.55.3.1", "name": "Fa0/1.300", "passive": True},
        ],
        "process": 1,
        "ref_bw": 30000,
        "router_id": "10.0.0.1",
    }

    return_value = render_jinja_template(template, data)
    correct_lines = set(correct_return_value.splitlines())
    return_value = strip_empty_lines(return_value)
    return_lines = set(return_value.splitlines())

    assert correct_lines == return_lines, "В итоговой конфигурации ospf не все строки"
