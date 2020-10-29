import pytest
import task_21_1
import os


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_templates_exists():
    """
    Проверка, что функция создана
    """
    assert os.path.exists(
        "templates/sh_ip_dhcp_snooping.template"
    ), "Шаблон templates/sh_ip_dhcp_snooping.template не существует"


def test_template():
    """
    Проверка работы шаблона
    """
    correct_return_value = [
        ["mac", "ip", "vlan", "intf"],
        ["00:09:BB:3D:D6:58", "10.1.10.2", "10", "FastEthernet0/1"],
        ["00:04:A3:3E:5B:69", "10.1.5.2", "5", "FastEthernet0/10"],
        ["00:05:B3:7E:9B:60", "10.1.5.4", "5", "FastEthernet0/9"],
        ["00:09:BC:3F:A6:50", "10.1.10.6", "10", "FastEthernet0/3"],
    ]
    with open("output/sh_ip_dhcp_snooping.txt") as show:
        sh_ip_dhcp_snoop = show.read()
    template = "templates/sh_ip_dhcp_snooping.template"
    return_value = task_21_1.parse_command_output(template, sh_ip_dhcp_snoop)

    assert (
        return_value == correct_return_value
    ), "Шаблон templates/sh_ip_dhcp_snooping.template неправильно парсит данные"
