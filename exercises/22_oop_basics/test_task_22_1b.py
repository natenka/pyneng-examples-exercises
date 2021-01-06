import pytest
import warnings
import task_22_1b
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
    check_class_exists(task_22_1b, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    top_with_data = task_22_1b.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Проверка удаления дублей в топологии"""
    top_with_data = task_22_1b.Topology(topology_with_dupl_links)
    assert (
        type(top_with_data.topology) == dict
    ), f"По заданию в переменной topology должен быть словарь, а не {type(top_with_data.topology).__name__}"
    assert len(top_with_data.topology) == len(
        normalized_topology_example
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"


def test_method_delete_link_created(
    topology_with_dupl_links, normalized_topology_example
):
    """Проверяем, что в объекте Topology есть метод delete_link"""
    norm_top = task_22_1b.Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method="delete_link")


def test_method_delete_link(normalized_topology_example, capsys):
    """Проверка работы метода delete_link"""
    norm_top = task_22_1b.Topology(normalized_topology_example)
    delete_link_result = norm_top.delete_link(("R3", "Eth0/0"), ("SW1", "Eth0/3"))
    assert delete_link_result == None, "Метод delete_link не должен ничего возвращать"

    assert ("R3", "Eth0/0") not in norm_top.topology, "Соединение не было удалено"

    # проверка удаления зеркального линка
    norm_top.delete_link(("R5", "Eth0/0"), ("R3", "Eth0/2"))
    assert ("R3", "Eth0/2") not in norm_top.topology, "Соединение не было удалено"

    # проверка удаления несуществующего линка
    norm_top.delete_link(("R8", "Eth0/2"), ("R9", "Eth0/1"))
    out, err = capsys.readouterr()
    link_msg = "Такого соединения нет"
    assert (
        link_msg in out
    ), "При удалении несуществующего соединения, не было выведено сообщение 'Такого соединения нет'"
