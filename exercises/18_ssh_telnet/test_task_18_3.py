import pytest
import task_18_3
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_function_exists,
    check_function_params,
    strip_empty_lines,
)

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_18_3, "send_commands")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_18_3.send_commands,
        param_count=3,
        param_names=["device", "config", "show"],
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
    correct_return_value_show = r1_test_connection.send_command(show_command)
    correct_return_value_cfg = r1_test_connection.send_config_set(cfg_commands)
    return_value_show = task_18_3.send_commands(
        first_router_from_devices_yaml, show=show_command
    )
    return_value_cfg = task_18_3.send_commands(
        first_router_from_devices_yaml, config=cfg_commands
    )
    assert return_value_show != None, "Функция ничего не возвращает"
    assert (
        type(return_value_show) == str
    ), f"По заданию функция должна возвращать строку, а возвращает {type(return_value).__name__}"
    assert strip_empty_lines(correct_return_value_show) == strip_empty_lines(
        return_value_show
    ), "Функция возвращает неправильное значение при передаче команды show"
    assert strip_empty_lines(correct_return_value_cfg) == strip_empty_lines(
        return_value_cfg
    ), "Функция возвращает неправильное значение при передаче конфигурационных команд"
