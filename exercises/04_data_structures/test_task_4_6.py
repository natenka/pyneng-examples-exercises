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
    import task_4_6

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "Prefix                10.0.24.0/24\n"
        "AD/Metric             110/41\n"
        "Next-Hop              10.0.13.3\n"
        "Last update           3d18h\n"
        "Outbound Interface    FastEthernet0/0\n"
    )
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        unified_columns_output(out.strip()) == correct_stdout
    ), "На стандартный поток вывода выводится неправильная строка"
