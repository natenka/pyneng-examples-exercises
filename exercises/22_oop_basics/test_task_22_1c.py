import pytest
import warnings
import task_22_1c
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
    stdout_incorrect_warning,
    unify_topology_dict,
)

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(task_22_1c, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    top_with_data = task_22_1c.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Проверка удаления дублей в топологии"""
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = task_22_1c.Topology(topology_with_dupl_links)
    return_topology = unify_topology_dict(return_value.topology)
    assert (
        type(return_value.topology) == dict
    ), f"По заданию в переменной topology должен быть словарь, а не {type(top_with_data.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"


def test_method_delete_node_created(
    topology_with_dupl_links, normalized_topology_example
):
    """Проверяем, что в объекте Topology есть метод delete_node"""
    return_value = task_22_1c.Topology(normalized_topology_example)
    check_attr_or_method(return_value, method="delete_node")


def test_method_delete_node(normalized_topology_example, capsys):
    """Проверка работы метода delete_node"""
    return_value = task_22_1c.Topology(normalized_topology_example)

    node = "SW1"
    delete_node_result = return_value.delete_node(node)
    assert None == delete_node_result, "Метод delete_node не должен ничего возвращать"

    ports_with_node = [
        src for src, dst in return_value.topology.items() if node in src or node in dst
    ]
    assert 0 == len(ports_with_node), "Соединения с хостом SW1 не были удалены"
    assert 3 == len(
        return_value.topology
    ), "В топологии должны остаться только три соединения"

    # проверка удаления несуществующего устройства
    return_value.delete_node(node)
    out, err = capsys.readouterr()
    assert (
        "Такого устройства нет" in out
    ), "При удалении несуществующего устройства, не было выведено сообщение 'Такого устройства нет'"
