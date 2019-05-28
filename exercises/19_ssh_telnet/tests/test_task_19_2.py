import pytest
import task_19_2
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_functions_created():
    check_function_exists(task_19_2, 'send_config_commands')


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    test_commands = [
        'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
    ]
    correct_return_value = r1_test_connection.send_config_set(test_commands)
    return_value = task_19_2.send_config_commands(
        first_router_from_devices_yaml, test_commands)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == str, "Функция должна возвращать строку"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

