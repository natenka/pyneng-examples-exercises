import sys

import task_22_1a

sys.path.append("..")

from pyneng_common_functions import (check_attr_or_method, check_class_exists,
                                     check_pytest, unify_topology_dict)

check_pytest(__loader__, __file__)


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(task_22_1a, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    top_with_data = task_22_1a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_method_normalize(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть метод _normalize"""
    top_with_data = task_22_1a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, method="_normalize")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Проверка удаления дублей в топологии"""
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = task_22_1a.Topology(topology_with_dupl_links)
    return_topology = unify_topology_dict(return_value.topology)
    assert (
        type(return_value.topology) == dict
    ), f"По заданию в переменной topology должен быть словарь, а не {type(top_with_data.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"
    assert (
        correct_topology == return_topology
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"
