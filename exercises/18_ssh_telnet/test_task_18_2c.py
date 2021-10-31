import sys

import pytest

try:
    import task_18_2c
except OSError:
    pytest.fail(
        "Для этого задания функцию надо ОБЯЗАТЕЛЬНО вызывать в блоке if __name__ == '__main__':"
    )


sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_pytest

check_pytest(__loader__, __file__)


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
    check_function_exists(task_18_2c, "send_config_commands")


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

    return_value = task_18_2c.send_config_commands(
        first_router_from_devices_yaml, [command], log=False
    )

    # Проверяем вывод информации об ошибках в stdout
    # во входящих данных три команды с ошибками
    # при каждой ошибке, должна выводиться информация:
    # ошибка, IP устройства, команда
    # в тесте проверяется наличие этих полей
    stdout, err = capsys.readouterr()
    ip = first_router_from_devices_yaml["host"]
    assert error in stdout, "В сообщении об ошибке нет самой ошибки"
    assert command in stdout, "В сообщении об ошибке нет выполняемой команды"
    assert ip in stdout, "В сообщении об ошибке нет IP-адреса устройства"


def test_function_return_value_continue_yes(
    first_router_from_devices_yaml, capsys, monkeypatch
):
    # проверяем возвращаемое значение, при условии,
    # что было выбрано продолжать выполнять вcе команды
    monkeypatch.setattr("builtins.input", lambda x=None: "y")

    return_value = task_18_2c.send_config_commands(
        first_router_from_devices_yaml, test_commands, log=False
    )

    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == tuple, "Функция должна возвращать кортеж"
    assert 2 == len(return_value) and all(
        type(item) == dict for item in return_value
    ), "Функция должна возвращать кортеж с двумя словарями"
    correct_good, correct_bad = correct_return_value
    return_good, return_bad = return_value
    assert (
        correct_good.keys() == return_good.keys()
    ), "Функция возвращает неправильное значение для словаря с командами без ошибок"
    assert (
        correct_bad.keys() == return_bad.keys()
    ), "Функция возвращает неправильное значение для словаря с командами с ошибками"


@pytest.mark.parametrize(
    "c_map,commands_1,commands_2",
    [
        (("good", "bad"), correct_commands[:2], commands_with_errors[:2]),
        (("bad", "good"), commands_with_errors[:1], correct_commands),
        (("good", "bad"), correct_commands[:1], commands_with_errors[1:2]),
    ],
)
def test_function_return_value_continue_no(
    first_router_from_devices_yaml, capsys, monkeypatch, c_map, commands_1, commands_2
):
    # проверяем сообщения об ошибках, при условии,
    # что после первой команды с ошибкой, была сделана остановка
    monkeypatch.setattr("builtins.input", lambda x=None: "n")
    commands = commands_1 + commands_2

    return_value = task_18_2c.send_config_commands(
        first_router_from_devices_yaml, commands, log=False
    )

    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == tuple, "Функция должна возвращать кортеж"
    assert 2 == len(return_value) and all(
        type(item) == dict for item in return_value
    ), "Функция должна возвращать кортеж с двумя словарями"
    return_good, return_bad = return_value
    if c_map[0] == "bad":
        commands_with_errors, correct_commands = commands_1, commands_2
        assert [] == list(return_good) and commands_with_errors[:1] == sorted(
            return_bad
        ), "Функция возвращает неправильное значение"
    else:
        commands_with_errors, correct_commands = commands_2, commands_1
        assert correct_commands == list(return_good) and commands_with_errors[
            :1
        ] == list(return_bad), "Функция возвращает неправильное значение"
