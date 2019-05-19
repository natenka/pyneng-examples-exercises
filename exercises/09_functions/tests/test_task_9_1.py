import pytest
import task_9_1
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params


def test_function_created():
    check_function_exists(task_9_1, 'generate_access_config')


def test_function_params():
    check_function_params(function=task_9_1.generate_access_config,
                          param_count=2, param_names=['intf_vlan_mapping', 'access_template'])


def test_function_return_value():
    access_vlans_mapping = {
        'FastEthernet0/12': 10,
        'FastEthernet0/14': 11,
        'FastEthernet0/16': 17
    }
    template_access_mode = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]
    correct_return_value = ['interface FastEthernet0/12',
                            'switchport mode access',
                            'switchport access vlan 10',
                            'switchport nonegotiate',
                            'spanning-tree portfast',
                            'spanning-tree bpduguard enable',
                            'interface FastEthernet0/14',
                            'switchport mode access',
                            'switchport access vlan 11',
                            'switchport nonegotiate',
                            'spanning-tree portfast',
                            'spanning-tree bpduguard enable',
                            'interface FastEthernet0/16',
                            'switchport mode access',
                            'switchport access vlan 17',
                            'switchport nonegotiate',
                            'spanning-tree portfast',
                            'spanning-tree bpduguard enable']

    return_value = task_9_1.generate_access_config(access_vlans_mapping, template_access_mode)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

