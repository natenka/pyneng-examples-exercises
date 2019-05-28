import pytest
import task_17_2
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_function_created():
    check_function_exists(task_17_2, 'parse_sh_cdp_neighbors')


def test_function_return_value():
    with open('sh_cdp_n_sw1.txt') as f:
        sh_cdp_n_sw1 = f.read()

    correct_return_value = {'SW1': {'Eth 0/1': {'R1': 'Eth 0/0'},
                                    'Eth 0/2': {'R2': 'Eth 0/0'},
                                    'Eth 0/3': {'R3': 'Eth 0/0'},
                                    'Eth 0/4': {'R4': 'Eth 0/0'}}}

    return_value = task_17_2.parse_sh_cdp_neighbors(sh_cdp_n_sw1)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == dict, "Функция должна возвращать словарь"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

