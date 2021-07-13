import textfsm
import os
import pytest
import task_21_4
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_21_4, "send_and_parse_show_command")


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    Проверка работы функции
    """
    with open("templates/sh_ip_int_br.template") as f:
        re_table = textfsm.TextFSM(f)
    sh_ip_int_br = r1_test_connection.send_command("sh ip int br")
    result = re_table.ParseText(sh_ip_int_br)
    correct_return_value = [dict(zip(re_table.header, line)) for line in result]

    full_pth = os.path.join(os.getcwd(), "templates")
    return_value = task_21_4.send_and_parse_show_command(
        first_router_from_devices_yaml, "sh ip int br", templates_path=full_pth
    )

    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        correct_return_value == return_value
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args(
    r1_test_connection, first_router_from_devices_yaml
):
    """
    Проверка работы функции с другими аргументами
    """
    with open("templates/sh_version.template") as f:
        re_table = textfsm.TextFSM(f)
    sh_version = r1_test_connection.send_command("sh version")
    result = re_table.ParseText(sh_version)
    correct_return_value = [dict(zip(re_table.header, line)) for line in result]

    full_pth = os.path.join(os.getcwd(), "templates")
    return_value = task_21_4.send_and_parse_show_command(
        first_router_from_devices_yaml, "sh version", templates_path=full_pth
    )

    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        correct_return_value == return_value
    ), "Функция возвращает неправильное значение"
