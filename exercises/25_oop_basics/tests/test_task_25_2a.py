import os
import pytest
import task_25_2a
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method, strip_empty_lines


def test_class_created():
    check_class_exists(task_25_2a, 'CiscoTelnet')


def test_class(first_router_from_devices_yaml, r1_test_telnet_connection):
    full_pth = os.path.join(os.getcwd(), 'templates')
    os.environ['NET_TEXTFSM'] = full_pth

    r1 = task_25_2a.CiscoTelnet(**first_router_from_devices_yaml)
    assert getattr(r1, 'send_show_command', None) != None,\
            'У класса CiscoTelnet должен быть метод send_show_command'

    correct_return_value = r1_test_telnet_connection.send_command(
        'sh ip int br', use_textfsm=True)
    return_value = r1.send_show_command('sh ip int br', templates='templates', parse=True)
    assert correct_return_value == return_value, "Метод send_show_command возвращает неправильное значение"

