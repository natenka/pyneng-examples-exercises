import sys

import pytest

import task_18_3

sys.path.append("..")

from pyneng_common_functions import (check_function_exists,
                                     check_pytest,
                                     strip_empty_lines)

check_pytest(__loader__, __file__)


def test_functions_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_18_3, "send_commands")


def test_function_params(r1_test_connection, first_router_from_devices_yaml):
    """
    Проверка параметров
    """
    show_command = "sh ip int br"
    cfg_commands = ["logging buffered 20010"]
    with pytest.raises(TypeError) as excinfo:
        # если аргументы show/config передаются не как ключевые,
        # должно генерироваться исключение TypeError
        task_18_3.send_commands(first_router_from_devices_yaml, show_command)

    with pytest.raises(ValueError) as excinfo:
        # Если передаются оба аргумента и show и config,
        # должно генерироваться исключение ValueError
        task_18_3.send_commands(
            first_router_from_devices_yaml, show=show_command, config=cfg_commands
        )


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    Проверка работы функции
    """
    show_command = "sh ip int br"
    cfg_commands = [
        "logging 10.255.255.1",
        "logging buffered 20010",
        "no logging console",
    ]
    correct_return_value_show = strip_empty_lines(
        r1_test_connection.send_command(show_command)
    )
    correct_return_value_cfg = strip_empty_lines(
        r1_test_connection.send_config_set(cfg_commands)
    )
    return_value_show = strip_empty_lines(
        task_18_3.send_commands(first_router_from_devices_yaml, show=show_command)
    )
    return_value_cfg = strip_empty_lines(
        task_18_3.send_commands(first_router_from_devices_yaml, config=cfg_commands)
    )
    assert return_value_show is not None, "Функция ничего не возвращает"
    assert (
        type(return_value_show) == str
    ), f"По заданию функция должна возвращать строку, а возвращает {type(return_value).__name__}"
    assert (
        correct_return_value_show == return_value_show
    ), "Функция возвращает неправильное значение при передаче команды show"
    assert (
        correct_return_value_cfg == return_value_cfg
    ), "Функция возвращает неправильное значение при передаче конфигурационных команд"
