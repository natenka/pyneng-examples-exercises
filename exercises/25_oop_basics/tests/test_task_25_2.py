import pytest
import task_25_2
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method, strip_empty_lines


def test_class_created():
    check_class_exists(task_25_2, 'CiscoTelnet')


def test_class(first_router_from_devices_yaml, r1_test_telnet_connection):
    r1 = task_25_2.CiscoTelnet(**first_router_from_devices_yaml)
    assert getattr(r1, '_write_line', None) != None,\
            'У класса CiscoTelnet должен быть метод _write_line'
    assert getattr(r1, 'send_show_command', None) != None,\
            'У класса CiscoTelnet должен быть метод send_show_command'

    correct_return_value = strip_empty_lines(
        r1_test_telnet_connection.send_command('sh ip int br'))
    return_value = strip_empty_lines(r1.send_show_command('sh ip int br'))
    assert correct_return_value in return_value, "Метод send_show_command возвращает неправильное значение"



