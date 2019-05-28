import pytest
import task_15_4
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_function_created():
    check_function_exists(task_15_4, 'get_ints_without_description')


def test_function_return_value():
    correct_return_value = ['Loopback0', 'Tunnel0', 'Ethernet0/1',
                            'Ethernet0/3.100', 'Ethernet1/0']
    return_value = task_15_4.get_ints_without_description('config_r1.txt')
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    assert sorted(return_value) == sorted(correct_return_value),\
            "Функция возвращает неправильное значение"

