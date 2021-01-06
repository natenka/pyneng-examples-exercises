import pytest
import task_19_2
import sys
import yaml

sys.path.append("..")

from pyneng_common_functions import (
    check_function_exists,
    strip_empty_lines,
)

from conftest import create_ssh_connect

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
    devices = devices[:3]
    r1, r2, r3 = devices


def test_functions_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_19_2, "send_show_command_to_devices")


@pytest.mark.parametrize(
    "device,command", [(r1, "sh version"), (r2, "sh ip int br"), (r3, "sh int desc")],
)
def test_function_return_value_from_single_device(
    three_routers_from_devices_yaml, r1_r2_r3_test_connection, tmpdir, device, command
):
    """
    Проверка работы функции
    """
    ssh = create_ssh_connect(device)
    output = f"{ssh.find_prompt()}{command}\n{ssh.send_command(command)}\n"
    ssh.disconnect()
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_2.txt")

    return_value = task_19_2.send_show_command_to_devices(
        devices=[device], command=command, filename=dest_filename, limit=3,
    )
    assert return_value == None, "Функция должна возвращать None"
    dest_file_content = dest_filename.read().strip()

    assert strip_empty_lines(output) == strip_empty_lines(
        dest_file_content
    ), f"В итоговом файле нет вывода с {device['host']}"


def test_function_return_value_from_all_devices(
    three_routers_from_devices_yaml, r1_r2_r3_test_connection, tmpdir
):
    command = "sh ip int br"
    out1, out2, out3 = [r.send_command(command) for r in r1_r2_r3_test_connection]
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_2.txt")

    return_value = task_19_2.send_show_command_to_devices(
        devices=three_routers_from_devices_yaml,
        command=command,
        filename=dest_filename,
        limit=3,
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
