import pytest
import task_22_1
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_functions_created():
    check_function_exists(task_22_1, 'parse_command_output')


def test_function_return_value():
    correct_return_value = [
        ['intf', 'address', 'status', 'protocol'],
        ['FastEthernet0/0', '15.0.15.1', 'up', 'up'],
        ['FastEthernet0/1', '10.0.12.1', 'up', 'up'],
        ['FastEthernet0/2', '10.0.13.1', 'up', 'up'],
        ['FastEthernet0/3', 'unassigned', 'up', 'up'],
        ['Loopback0', '10.1.1.1', 'up', 'up'],
        ['Loopback100', '100.0.0.1', 'up', 'up']
    ]
    with open("output/sh_ip_int_br.txt") as f:
        sh_ip_int_br = f.read()
    template = "templates/sh_ip_int_br.template"

    return_value = task_22_1.parse_command_output(template, sh_ip_int_br)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    assert return_value == correct_return_value,\
            "Функция возвращает неправильное значение"


