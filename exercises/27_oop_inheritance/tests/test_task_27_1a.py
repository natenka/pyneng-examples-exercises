import pytest
import task_27_1a
from common_functions import check_attr_or_method
from base_connect_class import BaseSSH


def test_class_created():
    assert hasattr(task_27_1a, 'CiscoSSH'), "Надо создать класс CiscoSSH"


def test_class_inheritance(first_router_from_devices_yaml):
    r1 = task_27_1a.CiscoSSH(**first_router_from_devices_yaml)
    assert isinstance(r1, BaseSSH), "Класс CiscoSSH должен наследовать BaseSSH"
    check_attr_or_method(r1, attr='send_show_command')
    check_attr_or_method(r1, attr='send_cfg_commands')
