import pytest
import task_19_2a
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_functions_created():
    check_function_exists(task_19_2a, 'send_config_commands')


def test_function_return_value(capsys, r1_test_connection,
                               first_router_from_devices_yaml):
    test_commands = [
        'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
    ]
    correct_return_value = r1_test_connection.send_config_set(test_commands)
    return_value = task_19_2a.send_config_commands(
        first_router_from_devices_yaml, test_commands)
    # проверяем возвращаемое значение
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == str, "Функция должна возвращать строку"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

    # по умолчанию, verbose должно быть равным True
    # и на stdout должно выводиться сообщение
    correct_stdout = f'{r1_test_connection.host}'
    out, err = capsys.readouterr()
    assert out != '', "Сообщение об ошибке не выведено на stdout"
    assert correct_stdout in out, "Выведено неправильное сообщение об ошибке"

    # проверяем, что с verbose=False вывода в stdout нет
    return_value = task_19_2a.send_config_commands(
        first_router_from_devices_yaml, test_commands, verbose=False)
    correct_stdout = ''
    out, err = capsys.readouterr()
    assert out == correct_stdout,\
            "Сообщение об ошибке не должно выводиться на stdout, когда verbose=False"
