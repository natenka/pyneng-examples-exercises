import pytest
import task_18_1a
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_18_1a, "send_show_command")


def test_function_return_value(capsys, first_router_wrong_pass):
    """
    Проверка работы функции
    """
    return_value = task_18_1a.send_show_command(first_router_wrong_pass, "sh ip int br")
    correct_stdout = "Authentication fail"
    out, err = capsys.readouterr()
    assert out != "", "Сообщение об ошибке не выведено на stdout"
    assert correct_stdout in out, "Выведено неправильное сообщение об ошибке"
