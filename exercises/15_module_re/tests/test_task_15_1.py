import pytest
import task_15_1
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_function_created():
    check_function_exists(task_15_1, 'get_ip_from_cfg')


def test_function_return_value():
    correct_return_value = [('10.1.1.1', '255.255.255.255'),
                            ('10.0.13.1', '255.255.255.0'),
                            ('10.0.19.1', '255.255.255.0')]

    return_value = task_15_1.get_ip_from_cfg('config_r1.txt')
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    #Списки сортируются чтобы не было ошибки, если адреса записаны в списке в другом порядке
    #В этом задании порядок кортежей в списке не важен
    assert sorted(return_value) == sorted(correct_return_value), "Функция возвращает неправильное значение"

