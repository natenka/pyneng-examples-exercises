import textfsm
import os
import pytest
import task_22_4
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_functions_created():
    check_function_exists(task_22_4, 'send_and_parse_show_command')


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    with open('templates/sh_ip_int_br.template') as f:
        re_table = textfsm.TextFSM(f)
    sh_ip_int_br = r1_test_connection.send_command('sh ip int br')
    result = re_table.ParseText(sh_ip_int_br)
    correct_return_value = [dict(zip(re_table.header, line)) for line in result]

    full_pth = os.path.join(os.getcwd(), 'templates')
    return_value = task_22_4.send_and_parse_show_command(
        first_router_from_devices_yaml, 'sh ip int br', full_pth)

    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    assert return_value == correct_return_value,\
            "Функция возвращает неправильное значение"


