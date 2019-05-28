import pytest
import task_22_3
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_functions_created():
    check_function_exists(task_22_3, 'parse_command_dynamic')


def test_function_return_value():
    correct_return_value = [
        {'address': '15.0.15.1', 'intf': 'FastEthernet0/0', 'protocol': 'up', 'status': 'up'},
        {'address': '10.0.12.1', 'intf': 'FastEthernet0/1', 'protocol': 'up', 'status': 'up'},
        {'address': '10.0.13.1', 'intf': 'FastEthernet0/2', 'protocol': 'up', 'status': 'up'},
        {'address': 'unassigned', 'intf': 'FastEthernet0/3', 'protocol': 'up', 'status': 'up'},
        {'address': '10.1.1.1', 'intf': 'Loopback0', 'protocol': 'up', 'status': 'up'},
        {'address': '100.0.0.1', 'intf': 'Loopback100', 'protocol': 'up', 'status': 'up'}
    ]
    with open("output/sh_ip_int_br.txt") as f:
        sh_ip_int_br = f.read()
    attributes = {'Command': 'show ip int br', 'Vendor': 'cisco_ios'}

    return_value = task_22_3.parse_command_dynamic(sh_ip_int_br, attributes)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    assert return_value == correct_return_value,\
            "Функция возвращает неправильное значение"


