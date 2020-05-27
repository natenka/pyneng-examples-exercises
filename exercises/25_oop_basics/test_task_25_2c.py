import os
import pytest
import task_25_2c
import sys

sys.path.append("..")

from common_functions import check_class_exists, check_attr_or_method, strip_empty_lines

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(task_25_2c, "CiscoTelnet")


def test_send_config_commands_correct_commands(first_router_from_devices_yaml, capsys):
    r1 = task_25_2c.CiscoTelnet(**first_router_from_devices_yaml)
    check_attr_or_method(r1, method="send_config_commands")

    # команды без ошибок
    correct_commands = ["interface loop55", "ip address 5.5.5.5 255.255.255.255"]
    return_value = r1.send_config_commands(correct_commands)
    assert (
        correct_commands[0] in return_value and correct_commands[1] in return_value
    ), "Метод send_config_commands возвращает неправильное значение"


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "logging 0255.255.1"),
        ("Incomplete command", "logging"),
        ("Ambiguous command", "a"),
    ],
)
def test_send_config_commands_wrong_commands(
    first_router_from_devices_yaml, capsys, error, command
):
    r1 = task_25_2c.CiscoTelnet(**first_router_from_devices_yaml)

    # команда с ошибкой strict=False
    return_value = r1.send_config_commands(command, strict=False)
    out, err = capsys.readouterr()
    assert error in out, "Метод send_config_commands не выводит сообщение об ошибке"

    # команда с ошибкой strict=True
    with pytest.raises(ValueError) as excinfo:
        return_value = r1.send_config_commands(command, strict=True)
    assert error in str(
        excinfo
    ), "Метод send_config_commands должен генерировать исключение, когда strict=True"
