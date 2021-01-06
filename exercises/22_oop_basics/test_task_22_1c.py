import pytest
import warnings
import task_22_1c
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
    stdout_incorrect_warning,
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
    top_with_data = task_22_1c.Topology(topology_with_dupl_links)
    assert (
        type(top_with_data.topology) == dict
    ), f"По заданию в переменной topology должен быть словарь, а не {type(top_with_data.topology).__name__}"
    assert len(top_with_data.topology) == len(
        normalized_topology_example
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"


def test_method_delete_node_created(
    topology_with_dupl_links, normalized_topology_example
):
    """Проверяем, что в объекте Topology есть метод delete_node"""
    norm_top = task_22_1c.Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method="delete_node")


def test_method_delete_node(normalized_topology_example, capsys):
    """Проверка работы метода delete_node"""
    norm_top = task_22_1c.Topology(normalized_topology_example)

    node = "SW1"
    delete_node_result = norm_top.delete_node(node)
    assert delete_node_result == None, "Метод delete_node не должен ничего возвращать"

    ports_with_node = [
        src for src, dst in norm_top.topology.items() if node in src or node in dst
    ]
    assert len(ports_with_node) == 0, "Соединения с хостом SW1 не были удалены"
    assert (
        len(norm_top.topology) == 3
    ), "В топологии должны остаться только три соединения"

    # проверка удаления несуществующего устройства
    norm_top.delete_node(node)
    out, err = capsys.readouterr()
    node_msg = "Такого устройства нет"
    assert (
        node_msg in out
    ), "При удалении несуществующего устройства, не было выведено сообщение 'Такого устройства нет'"
