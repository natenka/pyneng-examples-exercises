import sys

import pytest
import task_12_1

sys.path.append("..")

from pyneng_common_functions import (check_function_exists, check_pytest,
                                     get_reach_unreach)


check_pytest(__loader__, __file__)


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_12_1, "ping_ip_addresses")


@pytest.mark.skipif(
    not hasattr(task_12_1, "ping_ip_addresses"),
    reason="Этот тест работает только если создана функция ping_ip_addresses",
)
def test_function_return_value():
    """
    Проверка работы функции
    """
    list_of_ips = ["1.1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    correct_return_value = get_reach_unreach(list_of_ips)

    return_value = task_12_1.ping_ip_addresses(list_of_ips)
    assert return_value is not None, "Функция ничего не возвращает"
    assert type(return_value) == tuple and all(
        type(item) == list for item in return_value
    ), "Функция должна возвращать кортеж с двумя списками"
    assert (
        correct_return_value == return_value
    ), "Функция возвращает неправильное значение"
