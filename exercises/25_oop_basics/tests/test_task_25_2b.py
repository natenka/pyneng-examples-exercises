import os
import pytest
import task_25_2b
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method, strip_empty_lines


def test_class_created():
    check_class_exists(task_25_2b, 'CiscoTelnet')


def test_class(first_router_from_devices_yaml):
    r1 = task_25_2b.CiscoTelnet(**first_router_from_devices_yaml)
    assert getattr(r1, 'send_config_commands', None) != None,\
            'У класса CiscoTelnet должен быть метод send_config_commands'

    cfg_comand = 'logging 10.1.1.1'
    return_value = r1.send_config_commands(cfg_comand)
    assert cfg_comand in return_value,\
            "Метод send_config_commands возвращает неправильное значение"

    cfg_comands = ['interface loop55', 'ip address 5.5.5.5 255.255.255.255']
    return_value = r1.send_config_commands(cfg_comands)
    assert cfg_comands[0] in return_value and cfg_comands[1] in return_value,\
            "Метод send_config_commands возвращает неправильное значение"

