import os
import pytest
import task_25_2c
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method, strip_empty_lines


def test_class_created():
    check_class_exists(task_25_2c, 'CiscoTelnet')


def test_class(first_router_from_devices_yaml, capsys):
    r1 = task_25_2c.CiscoTelnet(**first_router_from_devices_yaml)
    check_attr_or_method(r1, method='send_config_commands')

    # команды без ошибок
    correct_commands = ['interface loop55', 'ip address 5.5.5.5 255.255.255.255']
    return_value = r1.send_config_commands(correct_commands)
    assert correct_commands[0] in return_value and correct_commands[1] in return_value,\
            "Метод send_config_commands возвращает неправильное значение"


    command_with_error = 'logging 0255.255.1'
    error = 'Invalid input detected'

    # команда с ошибкой strict=False
    return_value = r1.send_config_commands(command_with_error, strict=False)
    out, err = capsys.readouterr()
    assert error in out,\
            "Метод send_config_commands не выводит сообщение об ошибке"

    # команда с ошибкой strict=True
    with pytest.raises(ValueError) as excinfo:
        return_value = r1.send_config_commands(command_with_error, strict=True)
    assert error in str(excinfo),\
            "Метод send_config_commands должен генерировать исключение, когда strict=True"

