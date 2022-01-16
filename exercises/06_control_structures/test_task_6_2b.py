import sys
from functools import wraps

import pytest

sys.path.append("..")

from pyneng_common_functions import check_pytest

check_pytest(__loader__, __file__)


@pytest.mark.parametrize(
    "ip_add,ip_type",
    [
        ("10.1.1.1", "unicast"),
        ("230.1.1.1", "multicast"),
        ("255.255.255.255", "local broadcast"),
        ("0.0.0.0", "unassigned"),
        ("250.1.1.1", "unused"),
    ],
)
def test_task_correct_ip(capsys, monkeypatch, ip_add, ip_type):
    """
    Проверка работы задания при вводе multicast адреса
    """
    monkeypatch.setattr("builtins.input", lambda x=None: ip_add)
    if sys.modules.get("task_6_2b"):
        del sys.modules["task_6_2b"]
    import task_6_2b

    out, err = capsys.readouterr()
    correct_stdout = ip_type
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        __tracebackhide__ = True
        wrapper.total_calls += 1
        result = func(*args, **kwargs)
        return result

    wrapper.total_calls = 0
    return wrapper


def monkey_input_ip(ip_add):
    __tracebackhide__ = True

    @count_calls
    def inner(prompt):
        __tracebackhide__ = True
        if inner.total_calls == 1:
            return ip_add
        elif inner.total_calls == 2:
            return "10.1.1.1"

    return inner


@pytest.mark.parametrize(
    "ip_add,ip_type",
    [
        ("10.1.1", "неправильный ip-адрес"),
        ("10.a.2.a", "неправильный ip-адрес"),
        ("10.1.1.1.1", "неправильный ip-адрес"),
        ("10.1.1.", "неправильный ip-адрес"),
        ("300.1.1.1", "неправильный ip-адрес"),
        ("30,1.1.1.1", "неправильный ip-адрес"),
    ],
)
def test_task_wrong_first_ip_correct_second(capsys, monkeypatch, ip_add, ip_type):
    """
    Проверка работы задания при вводе multicast адреса
    """
    monkeypatch.setattr("builtins.input", monkey_input_ip(ip_add))
    if sys.modules.get("task_6_2b"):
        del sys.modules["task_6_2b"]
    import task_6_2b

    out, err = capsys.readouterr()
    correct_stdout = ip_type
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip().lower()
    ), "На стандартный поток вывода выводится неправильный вывод"
