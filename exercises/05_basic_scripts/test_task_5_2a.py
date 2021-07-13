import re
from importlib import reload
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import unified_columns_output


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_task_10_5_5_1_24(capsys, monkeypatch):
    """
    Проверка работы задания при вводе 10.5.5.1/24
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.5.5.1/24")
    import task_5_2a

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "Network:\n"
        "10        5         5         0\n"
        "00001010  00000101  00000101  00000000\n\n"
        "Mask:\n"
        "/24\n"
        "255       255       255       0\n"
        "11111111  11111111  11111111  00000000"
    )

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert correct_stdout == stdout, "Выведено неправильное значение"


def test_task_10_1_1_193_28(capsys, monkeypatch):
    """
    Проверка работы задания при вводе 10.1.1.193/28
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.1.1.193/28")
    if sys.modules.get("task_5_2a"):
        reload(sys.modules["task_5_2a"])
    import task_5_2a

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "Network:\n"
        "10        1         1         192\n"
        "00001010  00000001  00000001  11000000\n\n"
        "Mask:\n"
        "/28\n"
        "255       255       255       240\n"
        "11111111  11111111  11111111  11110000"
    )

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert correct_stdout == stdout, "Выведено неправильное значение"


def test_task_172_16_100_237_29(capsys, monkeypatch):
    """
    Проверка работы задания при вводе 172.16.100.237/29
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "172.16.100.237/29")
    if sys.modules.get("task_5_2a"):
        reload(sys.modules["task_5_2a"])
    import task_5_2a

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "Network:\n"
        "172       16        100       232\n"
        "10101100  00010000  01100100  11101000\n\n"
        "Mask:\n"
        "/29\n"
        "255       255       255       248\n"
        "11111111  11111111  11111111  11111000"
    )

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert correct_stdout == stdout, "Выведено неправильное значение"
