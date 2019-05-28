import pytest
import task_26_2
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method, strip_empty_lines


def test_class_created():
    check_class_exists(task_26_2, 'CiscoTelnet')


def test_method__enter__(first_router_from_devices_yaml):
    r1 = task_26_2.CiscoTelnet(**first_router_from_devices_yaml)
    assert getattr(r1, '__enter__', None) != None,\
            'У класса CiscoTelnet должен быть метод __enter__'

    assert getattr(r1, '__exit__', None) != None,\
            'У класса CiscoTelnet должен быть метод __exit__'
