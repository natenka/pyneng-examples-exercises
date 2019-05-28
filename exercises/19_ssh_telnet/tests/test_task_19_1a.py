import pytest
import task_19_1a
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_functions_created():
    check_function_exists(task_19_1a, 'send_show_command')


def test_function_return_value(capsys, first_router_wrong_pass):
    return_value = task_19_1a.send_show_command(first_router_wrong_pass,
                                                'sh ip int br')
    correct_stdout = 'Authentication failure: unable to connect'
    out, err = capsys.readouterr()
    assert out != '', "Сообщение об ошибке не выведено на stdout"
    assert correct_stdout in out, "Выведено неправильное сообщение об ошибке"
