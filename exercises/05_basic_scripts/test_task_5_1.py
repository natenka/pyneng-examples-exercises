from importlib import reload
import sys
import pytest


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_task_r2(capsys, monkeypatch):
    """
    Проверка работы задания при вводе r2
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "r2")
    import task_5_1

    out, err = capsys.readouterr()
    r2_dict = {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    }

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        str(r2_dict) in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


def test_task_sw1(capsys, monkeypatch):
    """
    Проверка работы задания при вводе sw1
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "sw1")
    if sys.modules.get("task_5_1"):
        reload(sys.modules["task_5_1"])
    import task_5_1

    out, err = capsys.readouterr()
    sw1_dict = {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    }
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        str(sw1_dict) in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
