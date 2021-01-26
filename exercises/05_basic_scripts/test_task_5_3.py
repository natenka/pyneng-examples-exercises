from functools import wraps
from importlib import reload
import sys
import pytest


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        __tracebackhide__ = True
        wrapper.total_calls += 1
        result = func(*args, **kwargs)
        return result
    wrapper.total_calls = 0
    return wrapper


@count_calls
def monkey_input_access(prompt):
    __tracebackhide__ = True
    if monkey_input_access.total_calls == 1:
        return "access"
    elif monkey_input_access.total_calls == 2:
        return "Gi0/3"
    elif monkey_input_access.total_calls == 3:
        return "55"


@count_calls
def monkey_input_trunk(prompt):
    __tracebackhide__ = True
    if monkey_input_trunk.total_calls == 1:
        return "trunk"
    elif monkey_input_trunk.total_calls == 2:
        return "Gi0/2"
    elif monkey_input_trunk.total_calls == 3:
        return "10,11,12"


def test_task_access(capsys, monkeypatch):
    """
    Проверка работы задания при вводе access
    """
    monkeypatch.setattr("builtins.input", monkey_input_access)
    import task_5_3

    out, err = capsys.readouterr()
    correct_stdout = (
        "interface Gi0/3\n"
        "switchport mode access\n"
        "switchport access vlan 55\n"
        "switchport nonegotiate\n"
        "spanning-tree portfast\n"
        "spanning-tree bpduguard enable"
    )

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


def test_task_trunk(capsys, monkeypatch):
    """
    Проверка работы задания при вводе trunk
    """
    monkeypatch.setattr("builtins.input", monkey_input_trunk)
    if sys.modules.get("task_5_3"):
        reload(sys.modules["task_5_3"])
    import task_5_3

    out, err = capsys.readouterr()
    correct_stdout = (
        "interface Gi0/2\n"
        "switchport trunk encapsulation dot1q\n"
        "switchport mode trunk\n"
        "switchport trunk allowed vlan 10,11,12"
    )
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
