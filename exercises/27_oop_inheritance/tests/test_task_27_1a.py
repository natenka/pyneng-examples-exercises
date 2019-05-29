import pytest
import task_27_1a
from base_connect_class import BaseSSH
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_27_1a, 'CiscoSSH')


def test_class_inheritance(first_router_from_devices_yaml):
    r1 = task_27_1a.CiscoSSH(**first_router_from_devices_yaml)
    assert isinstance(r1, BaseSSH), "Класс CiscoSSH должен наследовать BaseSSH"
    check_attr_or_method(r1, method='send_show_command')
    check_attr_or_method(r1, method='send_cfg_commands')
