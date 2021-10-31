import sys

import task_22_1

sys.path.append("..")

from pyneng_common_functions import (check_attr_or_method, check_class_exists,
                                     check_pytest, unify_topology_dict)

check_pytest(__loader__, __file__)


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(task_22_1, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    return_value = task_22_1.Topology(topology_with_dupl_links)
    check_attr_or_method(return_value, attr="topology")


def test_topology_normalization():
    """Проверка удаления дублей в топологии"""
    topology_with_dupl_links = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    correct_topology = unify_topology_dict(
        {
            ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
            ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
            ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
            ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
            ("R3", "Eth0/1"): ("R4", "Eth0/0"),
            ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        }
    )

    return_value = task_22_1.Topology(topology_with_dupl_links)
    return_topology = unify_topology_dict(return_value.topology)
    assert (
        type(return_value.topology) == dict
    ), f"По заданию в переменной topology должен быть словарь, а не {type(return_value.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"
    assert (
        correct_topology == return_topology
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"
