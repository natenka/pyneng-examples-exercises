import pytest
import task_22_2
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method, strip_empty_lines

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(task_22_2, "CiscoTelnet")


def test_send_show_command(first_router_from_devices_yaml, r1_test_telnet_connection):
    r1 = task_22_2.CiscoTelnet(**first_router_from_devices_yaml)
    check_attr_or_method(r1, method="_write_line")
    check_attr_or_method(r1, method="send_show_command")

    correct_return_value = strip_empty_lines(
        r1_test_telnet_connection.send_command("sh ip int br")
    )
    return_value = strip_empty_lines(r1.send_show_command("sh ip int br"))
    assert (
        correct_return_value in return_value
    ), "Метод send_show_command возвращает неправильное значение"


def test_send_show_command_different_command(
    first_router_from_devices_yaml, r1_test_telnet_connection
):
    r1 = task_22_2.CiscoTelnet(**first_router_from_devices_yaml)

    correct_return_value = strip_empty_lines(
        r1_test_telnet_connection.send_command("sh ip int | i address")
    )
    return_value = strip_empty_lines(r1.send_show_command("sh ip int | i address"))
    assert (
        correct_return_value in return_value
    ), "Метод send_show_command возвращает неправильное значение"
