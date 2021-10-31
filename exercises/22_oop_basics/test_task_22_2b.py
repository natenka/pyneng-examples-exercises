import sys

import task_22_2b

sys.path.append("..")

from pyneng_common_functions import (check_attr_or_method, check_class_exists,
                                     check_pytest, strip_empty_lines)

check_pytest(__loader__, __file__)


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(task_22_2b, "CiscoTelnet")


def test_send_config_commands_list(first_router_from_devices_yaml):
    r1 = task_22_2b.CiscoTelnet(**first_router_from_devices_yaml)
    check_attr_or_method(r1, method="send_config_commands")

    cfg_comands = ["interface loop55", "ip address 5.5.5.5 255.255.255.255"]
    return_value = r1.send_config_commands(cfg_comands)
    assert (
        cfg_comands[0] in return_value and cfg_comands[1] in return_value
    ), "Метод send_config_commands возвращает неправильное значение"


def test_send_config_command_str(first_router_from_devices_yaml):
    r1 = task_22_2b.CiscoTelnet(**first_router_from_devices_yaml)
    check_attr_or_method(r1, method="send_config_commands")

    cfg_comand = "logging 10.1.1.1"
    return_value = r1.send_config_commands(cfg_comand)
    assert (
        cfg_comand in return_value
    ), "Метод send_config_commands возвращает неправильное значение"


def test_send_config_commands_different_command(first_router_from_devices_yaml):
    r1 = task_22_2b.CiscoTelnet(**first_router_from_devices_yaml)
    check_attr_or_method(r1, method="send_config_commands")

    cfg_comand = "no ip http server"
    return_value = r1.send_config_commands(cfg_comand)
    assert (
        cfg_comand in return_value
    ), "Метод send_config_commands возвращает неправильное значение"

    cfg_comands = [
        "alias configure sh do sh",
        "alias exec ospf sh run | s ^router ospf",
    ]
    return_value = r1.send_config_commands(cfg_comands)
    assert (
        cfg_comands[0] in return_value and cfg_comands[1] in return_value
    ), "Метод send_config_commands возвращает неправильное значение"
