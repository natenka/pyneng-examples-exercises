import sys

import task_18_1a

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_pytest

check_pytest(__loader__, __file__)


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
