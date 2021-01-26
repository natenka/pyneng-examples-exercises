import re
from importlib import reload
import sys
import pytest


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def unified_columns_output(output):
    lines = [re.split(r" +", line.strip()) for line in output.strip().split("\n")]
    formatted = [("{:10}"*len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


def test_task_10_5_5_1_24(capsys, monkeypatch):
    """
    Проверка работы задания при вводе 10.5.5.1/24
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.5.5.1/24")
    import task_5_2a

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout_network = unified_columns_output(
        "10        5         5         0\n"
        "00001010  00000101  00000101  00000000"
    )

    correct_stdout_mask = unified_columns_output(
        "/24\n"
        "255       255       255       0\n"
        "11111111  11111111  11111111  00000000"
    )

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout_network in stdout
    ), "Выведено неправильное значение сети"
    assert (
        correct_stdout_mask in stdout
    ), "Выведено неправильное значение маски"


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
    correct_stdout_network = unified_columns_output(
        "10        1         1         192\n"
        "00001010  00000001  00000001  11000000"
    )

    correct_stdout_mask = unified_columns_output(
        "/28\n"
        "255       255       255       240\n"
        "11111111  11111111  11111111  11110000"
    )

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout_network in stdout
    ), "Выведено неправильное значение сети"
    assert (
        correct_stdout_mask in stdout
    ), "Выведено неправильное значение маски"


