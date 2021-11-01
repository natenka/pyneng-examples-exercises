import sys

import task_12_3

sys.path.append("..")

from pyneng_common_functions import (check_function_exists, check_pytest,
                                     unified_columns_output)


check_pytest(__loader__, __file__)


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_12_3, "print_ip_table")


def test_function_stdout(capsys):
    """
    Проверка работы задания
    """
    reach_ip = ["10.10.1.7", "10.10.1.8", "10.10.1.9", "10.10.1.15"]
    unreach_ip = ["10.10.2.1", "10.10.1.2"]
    return_value = task_12_3.print_ip_table(reach_ip, unreach_ip)

    stdout, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "Reachable    Unreachable\n"
        "-----------  -------------\n"
        "10.10.1.7    10.10.2.1\n"
        "10.10.1.8    10.10.1.2\n"
        "10.10.1.9\n"
        "10.10.1.15\n"
    )
    assert None == return_value, "Функция должна возвращать None"
    assert correct_stdout == unified_columns_output(
        stdout
    ), "Функция возвращает неправильное значение"
