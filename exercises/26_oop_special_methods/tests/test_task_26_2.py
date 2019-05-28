import pytest
from task_26_2 import CiscoTelnet
from common_functions import check_attr_or_method
from conftest import strip_empty_lines


def test_method__enter__(first_router_from_devices_yaml):
    r1 = CiscoTelnet(**first_router_from_devices_yaml)
    assert getattr(r1, '__enter__', None) != None,\
            'У класса CiscoTelnet должен быть метод __enter__'

    assert getattr(r1, '__exit__', None) != None,\
            'У класса CiscoTelnet должен быть метод __exit__'
