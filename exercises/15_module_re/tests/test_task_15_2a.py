import pytest
import task_15_2a
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_function_created():
    check_function_exists(task_15_2a, 'convert_to_dict')


def test_function_return_value():
    parsed_sh_ip_int_br = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
                           ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
                           ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
                           ('FastEthernet0/3', 'unassigned', 'administratively down', 'down'),
                           ('Loopback0', '10.1.1.1', 'up', 'up'),
                           ('Loopback100', '100.0.0.1', 'up', 'up')]

    correct_return_value = [{'interface': 'FastEthernet0/0', 'address': '15.0.15.1',
                             'status': 'up', 'protocol': 'up'},
                            {'interface': 'FastEthernet0/1', 'address': '10.0.12.1',
                             'status': 'up', 'protocol': 'up'},
                            {'interface': 'FastEthernet0/2', 'address': '10.0.13.1',
                             'status': 'up', 'protocol': 'up'},
                            {'interface': 'FastEthernet0/3', 'address': 'unassigned',
                             'status': 'administratively down', 'protocol': 'down'},
                            {'interface': 'Loopback0', 'address': '10.1.1.1',
                             'status': 'up', 'protocol': 'up'},
                            {'interface': 'Loopback100', 'address': '100.0.0.1',
                             'status': 'up', 'protocol': 'up'}]

    headers = ['interface', 'address', 'status', 'protocol']
    return_value = task_15_2a.convert_to_dict(headers, parsed_sh_ip_int_br)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

