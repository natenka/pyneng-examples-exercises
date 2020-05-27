import re

import yaml
import pytest

try:
    import task_19_2c
except OSError:
    pytest.fail(
        "Для этого задания функцию надо ОБЯЗАТЕЛЬНО вызывать в блоке if __name__ == '__main__':"
    )

import sys

sys.path.append("..")

from common_functions import check_function_exists

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


correct_return_value = (
    {
        "ip http server": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#ip http server\n"
        "R1(config)#",
        "logging buffered 20010": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging buffered 20010\n"
        "R1(config)#",
    },
    {
        "a": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#a\n"
        '% Ambiguous command:  "a"\n'
        "R1(config)#",
        "logging": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging\n"
        "% Incomplete command.\n"
        "\n"
        "R1(config)#",
        "logging 0255.255.1": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging 0255.255.1\n"
        "                   ^\n"
        "% Invalid input detected at '^' marker.\n"
        "\n"
        "R1(config)#",
    },
)

commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]
test_commands = commands_with_errors + correct_commands


def test_functions_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_19_2c, "send_config_commands")


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "logging 0255.255.1"),
        ("Incomplete command", "logging"),
        ("Ambiguous command", "a"),
    ],
)
def test_function_stdout(
    error, command, first_router_from_devices_yaml, capsys, monkeypatch
):
    # проверяем сообщения об ошибках, при условии,
    # что было выбрано продолжать выполнять вcе команды
    monkeypatch.setattr("builtins.input", lambda x=None: "y")

    return_value = task_19_2c.send_config_commands(
        first_router_from_devices_yaml, [command], log=False
    )

    # Проверяем вывод информации об ошибках в stdout
    # во входящих данных три команды с ошибками
    # при каждой ошибке, должна выводиться информация:
    # ошибка, IP устройства, команда
    # в тесте проверяется наличие этих полей
    out, err = capsys.readouterr()
    ip = first_router_from_devices_yaml["ip"]
    assert error in out, "В сообщении об ошибке нет самой ошибки"
    assert command in out, "В сообщении об ошибке нет выполняемой команды"
    assert ip in out, "В сообщении об ошибке нет IP-адреса устройства"


def test_function_return_value_continue_yes(
    first_router_from_devices_yaml, capsys, monkeypatch
):
    # проверяем возвращаемое значение, при условии,
    # что было выбрано продолжать выполнять вcе команды
    monkeypatch.setattr("builtins.input", lambda x=None: "y")

    return_value = task_19_2c.send_config_commands(
        first_router_from_devices_yaml, test_commands, log=False
    )

    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == tuple, "Функция должна возвращать кортеж"
    assert len(return_value) == 2 and all(
        type(item) == dict for item in return_value
    ), "Функция должна возвращать кортеж с двумя словарями"
    correct_good, correct_bad = correct_return_value
    return_good, return_bad = return_value
    assert (
        return_good.keys() == correct_good.keys()
        and return_bad.keys() == correct_bad.keys()
    ), "Функция возвращает неправильное значение"


@pytest.mark.parametrize(
    "commands,len_good,len_bad",
    [
        ([*correct_commands[:2], *commands_with_errors[:2]], 2, 1),
        ([commands_with_errors[0], *correct_commands], 0, 1),
        ([correct_commands[0], commands_with_errors[1], correct_commands[1]], 1, 1),
    ],
)
def test_function_return_value_continue_no(
    first_router_from_devices_yaml, capsys, monkeypatch, commands, len_good, len_bad
):
    # проверяем сообщения об ошибках, при условии,
    # что после первой команды с ошибкой, была сделана остановка
    monkeypatch.setattr("builtins.input", lambda x=None: "n")

    return_value = task_19_2c.send_config_commands(
        first_router_from_devices_yaml, commands, log=False
    )

    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == tuple, "Функция должна возвращать кортеж"
    assert len(return_value) == 2 and all(
        type(item) == dict for item in return_value
    ), "Функция должна возвращать кортеж с двумя словарями"
    return_good, return_bad = return_value
    assert (
        len(return_good) == len_good and len(return_bad) == len_bad
    ), "Функция возвращает неправильное значение"
