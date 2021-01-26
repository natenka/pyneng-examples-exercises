import pytest


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_task_stdout(capsys):
    """
    Проверка работы задания
    """
    import task_4_5

    out, err = capsys.readouterr()
    correct_stdout = "['1', '3', '8']"
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        out.strip() == correct_stdout
    ), "На стандартный поток вывода выводится неправильная строка"


def test_task_variables():
    """
    Проверка что в задании создана нужная переменная
    и в ней содержится правильный результат
    """
    import task_4_5

    # переменные созданные в задании:
    task_vars = [var for var in dir(task_4_5) if not var.startswith("_")]

    correct_result = ["1", "3", "8"]
    assert (
        "result" in task_vars
    ), "Итоговый список должен быть записан в переменную result"
    assert (
        type(task_4_5.result) == list
    ), f"По заданию в переменной result должен быть список, а в ней {type(task_4_5.result).__name__}"
    assert (
        task_4_5.result == correct_result
    ), f"В переменной result должен быть список {correct_result}"
