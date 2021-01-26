import re
from functools import wraps
import pytest

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_task(capsys, monkeypatch):
    """
    Проверка работы задания при вводе access
    """
    monkeypatch.setattr("sys.argv", ["task_7_2.py", "config_sw1.txt"])
    import task_7_2

    out, err = capsys.readouterr()
    correct_stdout = (
        "Current configuration : 2033 bytes\n"
        "version 15.0\n"
        "service timestamps debug datetime msec\n"
        "service timestamps log datetime msec\n"
        "no service password-encryption\n"
        "hostname sw1\n"
        "interface Ethernet0/0\n"
        " duplex auto\n"
        "interface Ethernet0/1\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport trunk allowed vlan 100\n"
        " switchport mode trunk\n"
        " duplex auto\n"
        " spanning-tree portfast edge trunk\n"
        "interface Ethernet0/2\n"
        " duplex auto\n"
        "interface Ethernet0/3\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport trunk allowed vlan 100\n"
        " duplex auto\n"
        " switchport mode trunk\n"
        " spanning-tree portfast edge trunk\n"
    )
    config_part = re.search(r"(Current configuration.*?)interface Ethernet1/0", out, re.DOTALL).group(1)

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        config_part == correct_stdout
    ), "На стандартный поток вывода выводится неправильный вывод"

