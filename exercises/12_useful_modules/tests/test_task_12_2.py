import pytest
import task_12_2
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_function_created():
    check_function_exists(task_12_2, 'convert_ranges_to_ip_list')


def test_function_return_value():
    list_of_ips_and_ranges = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    correct_return_value = ['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3',
                            '172.21.41.128', '172.21.41.129', '172.21.41.130',
                            '172.21.41.131', '172.21.41.132']

    return_value = task_12_2.convert_ranges_to_ip_list(list_of_ips_and_ranges)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

