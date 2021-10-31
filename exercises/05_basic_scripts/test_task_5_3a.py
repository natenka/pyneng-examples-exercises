import sys
from functools import wraps
from importlib import reload

import pytest

sys.path.append("..")

from pyneng_common_functions import check_pytest

check_pytest(__loader__, __file__)


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
        if "номер vlan" in prompt.lower():
            return "55"
        else:
            pytest.fail(
                "Для access портов запрос вланов должен быть таким: "
                "Введите номер VLAN:"
            )


@count_calls
def monkey_input_trunk(prompt):
    __tracebackhide__ = True
    if monkey_input_trunk.total_calls == 1:
        return "trunk"
    elif monkey_input_trunk.total_calls == 2:
        return "Gi0/2"
    elif monkey_input_trunk.total_calls == 3:
        if "разрешенные vlanы" in prompt.lower():
            return "10,11,12"
        else:
            pytest.fail(
                "Для trunk портов запрос вланов должен быть таким: "
                "Введите разрешенные VLANы:"
            )


def test_task_access(capsys, monkeypatch):
    """
    Проверка работы задания при вводе access
    """
    monkeypatch.setattr("builtins.input", monkey_input_access)
    import task_5_3a

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
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


def test_task_trunk(capsys, monkeypatch):
    """
    Проверка работы задания при вводе trunk
    """
    monkeypatch.setattr("builtins.input", monkey_input_trunk)
    if sys.modules.get("task_5_3a"):
        reload(sys.modules["task_5_3a"])
    import task_5_3a

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
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
