import pytest
import task_17_2
import sys

sys.path.append("..")

from common_functions import check_function_exists, read_all_csv_content_as_list

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Проверка, что функции созданы
    """
    check_function_exists(task_17_2, "parse_sh_version")
    check_function_exists(task_17_2, "write_inventory_to_csv")


def test_parse_sh_version_return_value():
    """
    Проверка работы функции
    """
    with open("sh_version_r1.txt") as f:
        sh_version_r1 = f.read()
    with open("sh_version_r2.txt") as f:
        sh_version_r2 = f.read()

    correct_return_value_r1 = (
        "12.4(15)T1",
        "flash:c1841-advipservicesk9-mz.124-15.T1.bin",
        "15 days, 8 hours, 32 minutes",
    )
    correct_return_value_r2 = (
        "12.4(4)T",
        "disk0:c7200-js-mz.124-4.T",
        "45 days, 8 hours, 22 minutes",
    )

    return_value_r1 = task_17_2.parse_sh_version(sh_version_r1)
    assert return_value_r1 != None, "Функция ничего не возвращает"
    assert (
        type(return_value_r1) == tuple
    ), f"По заданию функция должна возвращать кортеж, а возвращает {type(return_value_r1).__name__}"
    assert (
        return_value_r1 == correct_return_value_r1
    ), "Функция возвращает неправильное значение для вывода r1"
    return_value_r2 = task_17_2.parse_sh_version(sh_version_r2)
    assert (
        return_value_r2 == correct_return_value_r2
    ), "Функция возвращает неправильное значение для вывода r2"


def test_write_to_csv_return_value(tmpdir):
    """
    Проверка работы функции
    """
    routers_inventory = [
        ["hostname", "ios", "image", "uptime"],
        [
            "r1",
            "12.4(15)T1",
            "flash:c1841-advipservicesk9-mz.124-15.T1.bin",
            "15 days, 8 hours, 32 minutes",
        ],
        ["r2", "12.4(4)T", "disk0:c7200-js-mz.124-4.T", "45 days, 8 hours, 22 minutes"],
        ["r3", "12.4(4)T", "disk0:c7200-js-mz.124-4.T", "5 days, 18 hours, 2 minutes"],
    ]
    sh_version_files = ["sh_version_r1.txt", "sh_version_r2.txt", "sh_version_r3.txt"]
    dest_filename = tmpdir.mkdir("test_tasks").join("routers_inventory.csv")
    return_value = task_17_2.write_inventory_to_csv(sh_version_files, dest_filename)
    csv_content = read_all_csv_content_as_list(dest_filename)
    correct_return_value = sorted(routers_inventory)

    assert (
        return_value == None
    ), f"По заданию функция должна возвращать None, а возвращает {type(return_value).__name__}"
    assert (
        sorted(csv_content) == correct_return_value
    ), "Функция возвращает неправильное значение"
