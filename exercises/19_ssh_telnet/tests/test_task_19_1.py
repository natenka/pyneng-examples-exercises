import pytest
import task_19_1
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_functions_created():
    check_function_exists(task_19_1, 'send_show_command')


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    Тест проверяет работу функции send_show_command
    first_router_from_devices_yaml - это первое устройство из файла devices.yaml
    r1_test_connection - это сессия SSH с первым устройством из файла devices.yaml
                         Используется для проверки вывода
    """
    correct_return_value = r1_test_connection.send_command('sh ip int br')
    return_value = task_19_1.send_show_command(first_router_from_devices_yaml, 'sh ip int br')
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == str, "Функция должна возвращать строку"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

