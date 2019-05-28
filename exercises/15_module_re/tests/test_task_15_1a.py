import pytest
import task_15_1a
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_function_created():
    check_function_exists(task_15_1a, 'get_ip_from_cfg')


def test_function_return_value():
    correct_return_value = {'Loopback0': ('10.1.1.1', '255.255.255.255'),
                            'Ethernet0/0': ('10.0.13.1', '255.255.255.0'),
                            'Ethernet0/2': ('10.0.19.1', '255.255.255.0')}

    return_value = task_15_1a.get_ip_from_cfg('config_r1.txt')
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == dict, "Функция должна возвращать словарь"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

