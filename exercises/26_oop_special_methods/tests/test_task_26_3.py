import pytest
from task_26_3 import IPAddress
from common_functions import check_attr_or_method


def test_attr_topology():
    '''Проверяем, что в объекте IPAddress есть атрибуты ip и mask'''
    ip1 = IPAddress('10.1.1.1/24')
    check_attr_or_method(ip1, attr='ip')
    check_attr_or_method(ip1, attr='mask')
    assert ip1.ip == '10.1.1.1', "Значение ip1.ip должно быть равным 10.1.1.1"
    assert ip1.mask == 24, "Значение ip1.mask должно быть равным 24"


def test_wrong_ip():
    with pytest.raises(ValueError) as excinfo:
        ip1 = IPAddress('10.1.1.1/240')
    with pytest.raises(ValueError) as excinfo:
        ip1 = IPAddress('10.1.400.1/24')
