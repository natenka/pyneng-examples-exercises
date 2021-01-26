import sys
import re
import pytest


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def unified_columns_output(output):
    lines = [re.split(r"  +", line.strip()) for line in output.strip().split("\n")]
    formatted = [("{:25}" * len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


@pytest.mark.parametrize(
    "vlan,result",
    [
        (
            "10",
            "10       0a1b.1c80.7000      Gi0/4\n10       01ab.c5d0.70d0      Gi0/8",
        ),
        (
            "1000",
            "1000     0a4b.c380.7d00      Gi0/9",
        ),
    ],
    ids=["vlan 10", "vlan 1000"]
)
def test_task_stdout(capsys, monkeypatch, vlan, result):
    """
    Проверка работы задания
    """
    monkeypatch.setattr("builtins.input", lambda x=None: vlan)
    if sys.modules.get("task_7_3b"):
        del sys.modules["task_7_3b"]
    import task_7_3b

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(result)
    assert (
        unified_columns_output(out.strip()) == correct_stdout
    ), "На стандартный поток вывода выводится неправильная строка"
