import pytest
import task_19_1b
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_functions_created():
    check_function_exists(task_19_1b, 'send_show_command')


def test_function_return_value(capsys, first_router_wrong_ip):
    return_value = task_19_1b.send_show_command(
        first_router_wrong_ip, 'sh ip int br')
    correct_stdout = 'Connection to device timed-out'
    out, err = capsys.readouterr()
    assert out != '', "Сообщение об ошибке не выведено на stdout"
    assert correct_stdout in out, "Выведено неправильное сообщение об ошибке"
