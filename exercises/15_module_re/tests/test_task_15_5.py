import pytest
import task_15_5
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_function_created():
    check_function_exists(task_15_5, 'generate_description_from_cdp')


def test_function_return_value():
    correct_return_value = {'Eth 0/1': 'description Connected to R1 port Eth 0/0',
                            'Eth 0/2': 'description Connected to R2 port Eth 0/0',
                            'Eth 0/3': 'description Connected to R3 port Eth 0/0',
                            'Eth 0/5': 'description Connected to R6 port Eth 0/1'}
    return_value = task_15_5.generate_description_from_cdp('sh_cdp_n_sw1.txt')
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == dict, "Функция должна возвращать словарь"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

