import sys

import task_22_2

sys.path.append("..")

from pyneng_common_functions import (check_attr_or_method, check_class_exists,
                                     check_pytest, strip_empty_lines)

check_pytest(__loader__, __file__)


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
