import pytest
import task_19_3
import yaml
import sys

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
    check_function_exists(task_19_3, "send_command_to_devices")


@pytest.mark.parametrize(
    "device,command_dict",
    [
        (r1, {r1["host"]: "sh version | include IOS"}),
        (r2, {r2["host"]: "sh ip int br"}),
        (r3, {r3["host"]: "sh int desc"}),
    ],
)
def test_function_return_value_from_single_device(
    three_routers_from_devices_yaml,
    r1_r2_r3_test_connection,
    tmpdir,
    device,
    command_dict,
):
    """
    Проверка работы функции
    """
    device_ip = device["host"]
    command = command_dict[device_ip]
    ssh = create_ssh_connect(device)
    correct_output = strip_empty_lines(
        f"{ssh.find_prompt()}{command}\n{ssh.send_command(command)}\n"
    )
    ssh.disconnect()
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_3.txt")

    return_value = task_19_3.send_command_to_devices(
        devices=[device],
        commands_dict=command_dict,
        filename=dest_filename,
        limit=3,
    )
    assert None == return_value, "Функция должна возвращать None"
    dest_file_content = strip_empty_lines(dest_filename.read().strip())

    assert (
        correct_output == dest_file_content
    ), f"В итоговом файле нет вывода с {device_ip}"


def test_function_return_value_from_all_devices(
    three_routers_from_devices_yaml, r1_r2_r3_test_connection, tmpdir
):
    """
    Проверка работы функции
    """
    routers_ip = [router["host"] for router in three_routers_from_devices_yaml]
    commands = ["sh ip int br", "show ip int bri | exc unass", "show int desc"]
    out1, out2, out3 = [
        r.send_command(command)
        for r, command in zip(r1_r2_r3_test_connection, commands)
    ]
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_3.txt")

    return_value = task_19_3.send_command_to_devices(
        three_routers_from_devices_yaml,
        dict(zip(routers_ip, commands)),
        dest_filename,
        limit=3,
    )
    assert None == return_value, "Функция должна возвращать None"

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
