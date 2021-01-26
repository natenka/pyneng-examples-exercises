import pytest
import task_19_4
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
    check_function_exists(task_19_4, "send_commands_to_devices")


def test_function_params(first_router_from_devices_yaml, tmpdir):
    """
    Проверка параметров
    """
    command = "sh ip int br"
    cfg_commands = ["logging buffered 20010"]
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_4.txt")
    with pytest.raises(TypeError) as excinfo:
        # если аргументы show/config передаются не как ключевые,
        # должно генерироваться исключение TypeError
        task_19_4.send_commands_to_devices(
            [first_router_from_devices_yaml], dest_filename, command
        )

    with pytest.raises(ValueError) as excinfo:
        # Если передаются оба аргумента и show и config,
        # должно генерироваться исключение ValueError
        task_19_4.send_commands_to_devices(
            [first_router_from_devices_yaml], dest_filename, show=command, config=cfg_commands
        )


def test_function_return_value_show(
    three_routers_from_devices_yaml, r1_r2_r3_test_connection, tmpdir
):
    """
    Проверка работы функции
    """
    routers_ip = [router["host"] for router in three_routers_from_devices_yaml]
    command = "sh ip int br"
    out1, out2, out3 = [r.send_command(command) for r in r1_r2_r3_test_connection]
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_4.txt")

    return_value = task_19_4.send_commands_to_devices(
        three_routers_from_devices_yaml, show=command, filename=dest_filename, limit=3
    )
    assert return_value == None, "Функция должна возвращать None"

    dest_file_content = dest_filename.read().strip()

    # проверяем, что вывод с каждого устройства есть в файле
    assert (
        out1.strip() in dest_file_content
    ), "В итоговом файле нет вывода с первого устройства"
    assert (
        out2.strip() in dest_file_content
    ), "В итоговом файле нет вывода со второго устройства"
    assert (
        out3.strip() in dest_file_content
    ), "В итоговом файле нет вывода с третьего устройства"


def test_function_return_value_config(
    three_routers_from_devices_yaml, r1_r2_r3_test_connection, tmpdir
):
    routers_ip = [router["host"] for router in three_routers_from_devices_yaml]
    command = "logging 10.5.5.5"
    out1, out2, out3 = [r.send_config_set(command) for r in r1_r2_r3_test_connection]
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_4.txt")

    return_value = task_19_4.send_commands_to_devices(
        three_routers_from_devices_yaml, config=command, filename=dest_filename, limit=3
    )
    assert return_value == None, "Функция должна возвращать None"

    dest_file_content = dest_filename.read().strip()

    # проверяем, что вывод с каждого устройства есть в файле
    assert (
        out1.strip() in dest_file_content
    ), "В итоговом файле нет вывода с первого устройства"
    assert (
        out2.strip() in dest_file_content
    ), "В итоговом файле нет вывода со второго устройства"
    assert (
        out3.strip() in dest_file_content
    ), "В итоговом файле нет вывода с третьего устройства"
