import pytest
import task_19_3
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params


def test_functions_created():
    check_function_exists(task_19_3, 'send_commands')


def test_function_params():
    check_function_params(function=task_19_3.send_commands,
                          param_count=3,
                          param_names=['device', 'config', 'show'])


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    show_command = 'sh ip int br'
    cfg_commands = [
        'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
    ]
    correct_return_value_show = r1_test_connection.send_command(show_command)
    correct_return_value_cfg = r1_test_connection.send_config_set(cfg_commands)
    return_value_show = task_19_3.send_commands(
        first_router_from_devices_yaml, show=show_command)
    return_value_cfg = task_19_3.send_commands(
        first_router_from_devices_yaml, config=cfg_commands)
    assert return_value_show != None, "Функция ничего не возвращает"
    assert type(return_value_show) == str, "Функция должна возвращать строку"
    assert correct_return_value_show == return_value_show,\
            "Функция возвращает неправильное значение при передаче команды show"
    assert correct_return_value_cfg == return_value_cfg,\
            "Функция возвращает неправильное значение при передаче конфигурационных команд"

