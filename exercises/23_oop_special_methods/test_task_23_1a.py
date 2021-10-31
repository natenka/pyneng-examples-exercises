import sys

import task_23_1a

sys.path.append("..")

from pyneng_common_functions import (check_attr_or_method, check_class_exists,
                                     check_pytest)

check_pytest(__loader__, __file__)


def test_class_created():
    check_class_exists(task_23_1a, "IPAddress")


def test_attr_topology():
    """Проверяем, что в объекте IPAddress есть атрибуты ip и mask"""
    return_ip = task_23_1a.IPAddress("10.1.1.1/24")
    check_attr_or_method(return_ip, attr="ip")
    check_attr_or_method(return_ip, attr="mask")
    assert (
        "10.1.1.1" == return_ip.ip
    ), "Значение return_ip.ip должно быть равным 10.1.1.1"
    assert 24 == return_ip.mask, "Значение return_ip.mask должно быть равным 24"


def test_str_method():
    """Проверяем __str__"""
    return_ip = task_23_1a.IPAddress("10.5.5.5/24")
    assert "IP address 10.5.5.5/24" == str(
        return_ip
    ), "Метод __str__ должен возвращать 'IP address 10.5.5.5/24'"


def test_repr_method():
    """Проверяем __repr__"""
    return_ip = task_23_1a.IPAddress("10.5.5.5/24")
    assert "IPAddress('10.5.5.5/24')" == repr(return_ip).replace(
        '"', "'"
    ), "Метод __repr__ должен возвращать IPAddress('10.5.5.5/24')"
