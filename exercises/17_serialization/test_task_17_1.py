import pytest
import task_17_1
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, read_all_csv_content_as_list

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_17_1, "write_dhcp_snooping_to_csv")


def test_return_value(tmpdir):
    """
    Проверка работы функции
    """
    correct_return_value = sorted(
        [
            ["switch", "mac", "ip", "vlan", "interface"],
            ["sw1", "00:09:BB:3D:D6:58", "10.1.10.2", "10", "FastEthernet0/1"],
            ["sw1", "00:04:A3:3E:5B:69", "10.1.5.2", "5", "FastEthernet0/10"],
            ["sw1", "00:05:B3:7E:9B:60", "10.1.5.4", "5", "FastEthernet0/9"],
            ["sw1", "00:07:BC:3F:A6:50", "10.1.10.6", "10", "FastEthernet0/3"],
            ["sw1", "00:09:BC:3F:A6:50", "192.168.100.100", "1", "FastEthernet0/7"],
            ["sw2", "00:A9:BB:3D:D6:58", "10.1.10.20", "10", "FastEthernet0/7"],
            ["sw2", "00:B4:A3:3E:5B:69", "10.1.5.20", "5", "FastEthernet0/5"],
            ["sw2", "00:C5:B3:7E:9B:60", "10.1.5.40", "5", "FastEthernet0/9"],
            ["sw2", "00:A9:BC:3F:A6:50", "10.1.10.60", "20", "FastEthernet0/2"],
            ["sw3", "00:E9:BC:3F:A6:50", "100.1.1.6", "3", "FastEthernet0/20"],
            ["sw3", "00:E9:22:11:A6:50", "100.1.1.7", "3", "FastEthernet0/21"],
        ]
    )
    sh_dhcp_snoop_files = [
        "sw1_dhcp_snooping.txt",
        "sw2_dhcp_snooping.txt",
        "sw3_dhcp_snooping.txt",
    ]
    dest_filename = tmpdir.mkdir("test_tasks").join("output.csv")
    return_value = task_17_1.write_dhcp_snooping_to_csv(
        sh_dhcp_snoop_files, dest_filename
    )
    csv_content = read_all_csv_content_as_list(dest_filename)

    assert (
        None == return_value
    ), f"По заданию функция должна возвращать None, а возвращает {type(return_value).__name__}"
    assert correct_return_value == sorted(
        csv_content
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args(tmpdir):
    """
    Проверка работы функции с другими аргументами
    """
    correct_return_value = sorted(
        [
            ["switch", "mac", "ip", "vlan", "interface"],
            ["sw1", "00:09:BB:3D:D6:58", "10.1.10.2", "10", "FastEthernet0/1"],
            ["sw1", "00:04:A3:3E:5B:69", "10.1.5.2", "5", "FastEthernet0/10"],
            ["sw1", "00:05:B3:7E:9B:60", "10.1.5.4", "5", "FastEthernet0/9"],
            ["sw1", "00:07:BC:3F:A6:50", "10.1.10.6", "10", "FastEthernet0/3"],
            ["sw1", "00:09:BC:3F:A6:50", "192.168.100.100", "1", "FastEthernet0/7"],
            ["sw3", "00:E9:BC:3F:A6:50", "100.1.1.6", "3", "FastEthernet0/20"],
            ["sw3", "00:E9:22:11:A6:50", "100.1.1.7", "3", "FastEthernet0/21"],
        ]
    )
    sh_dhcp_snoop_files = [
        "sw1_dhcp_snooping.txt",
        "sw3_dhcp_snooping.txt",
    ]
    dest_filename = tmpdir.mkdir("test_tasks").join("output2.csv")
    return_value = task_17_1.write_dhcp_snooping_to_csv(
        sh_dhcp_snoop_files, dest_filename
    )
    csv_content = read_all_csv_content_as_list(dest_filename)

    assert (
        None == return_value
    ), f"По заданию функция должна возвращать None, а возвращает {type(return_value).__name__}"
    assert correct_return_value == sorted(
        csv_content
    ), "Функция возвращает неправильное значение"
