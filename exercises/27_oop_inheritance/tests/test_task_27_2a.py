import pytest
import task_27_2a
from netmiko.cisco.cisco_ios import CiscoIosBase
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_27_2a, 'MyNetmiko')


def test_class_inheritance(first_router_from_devices_yaml):
    r1 = task_27_2a.MyNetmiko(**first_router_from_devices_yaml)
    assert isinstance(r1, CiscoIosBase), "Класс MyNetmiko должен наследовать CiscoIosBase"
    check_attr_or_method(r1, method='send_command')
    with pytest.raises(task_27_2a.ErrorInCommand) as excinfo:
        return_value = r1.send_command('sh ip br')
    r1.disconnect()
