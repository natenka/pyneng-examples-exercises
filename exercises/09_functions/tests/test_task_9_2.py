import pytest
import task_9_2
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params


def test_function_created():
    check_function_exists(task_9_2, 'generate_trunk_config')


def test_function_params():
    check_function_params(function=task_9_2.generate_trunk_config,
                          param_count=2, param_names=['intf_vlan_mapping', 'trunk_template'])


def test_function_return_value():
    trunk_vlans_mapping = {
        'FastEthernet0/1': [10, 20, 30],
        'FastEthernet0/2': [11, 30],
        'FastEthernet0/4': [17]
    }
    template_trunk_mode = [
        'switchport mode trunk', 'switchport trunk native vlan 999',
        'switchport trunk allowed vlan'
    ]
    correct_return_value = ['interface FastEthernet0/1',
                            'switchport mode trunk',
                            'switchport trunk native vlan 999',
                            'switchport trunk allowed vlan 10,20,30',
                            'interface FastEthernet0/2',
                            'switchport mode trunk',
                            'switchport trunk native vlan 999',
                            'switchport trunk allowed vlan 11,30',
                            'interface FastEthernet0/4',
                            'switchport mode trunk',
                            'switchport trunk native vlan 999',
                            'switchport trunk allowed vlan 17']

    return_value = task_9_2.generate_trunk_config(trunk_vlans_mapping, template_trunk_mode)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

