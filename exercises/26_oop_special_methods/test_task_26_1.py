import pytest
import task_26_1
import sys

sys.path.append("..")

from common_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_26_1, "IPAddress")


def test_attr_topology():
    """Проверяем, что в объекте IPAddress есть атрибуты ip и mask"""
    ip1 = task_26_1.IPAddress("10.1.1.1/24")
    check_attr_or_method(ip1, attr="ip")
    check_attr_or_method(ip1, attr="mask")
    assert ip1.ip == "10.1.1.1", "Значение ip1.ip должно быть равным 10.1.1.1"
    assert ip1.mask == 24, "Значение ip1.mask должно быть равным 24"


def test_wrong_ip():
    with pytest.raises(ValueError) as excinfo:
        ip1 = task_26_1.IPAddress("10.1.1.1/240")
    with pytest.raises(ValueError) as excinfo:
        ip1 = task_26_1.IPAddress("10.1.400.1/24")
