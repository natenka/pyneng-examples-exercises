import re
import pytest


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def unified_columns_output(output):
    lines = [re.split(r"  +", line.strip()) for line in output.strip().split("\n")]
    formatted = [("{:25}"*len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


def test_task_stdout(capsys):
    """
    Проверка работы задания
    """
    import task_7_3a

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "10       01ab.c5d0.70d0      Gi0/8\n"
        "10       0a1b.1c80.7000      Gi0/4\n"
        "100      01bb.c580.7000      Gi0/1\n"
        "200      0a4b.c380.7c00      Gi0/2\n"
        "200      1a4b.c580.7000      Gi0/6\n"
        "300      0a1b.5c80.70f0      Gi0/7\n"
        "300      a2ab.c5a0.700e      Gi0/3\n"
        "500      02b1.3c80.7b00      Gi0/5\n"
        "1000     0a4b.c380.7d00      Gi0/9"
    )
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        unified_columns_output(out.strip()) == correct_stdout
    ), "На стандартный поток вывода выводится неправильная строка"
