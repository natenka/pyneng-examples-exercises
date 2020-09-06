import pytest
import warnings
import task_25_1d
import sys

sys.path.append("..")

from common_functions import (
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
    check_class_exists(task_25_1d, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    top_with_data = task_25_1d.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Проверка удаления дублей в топологии"""
    top_with_data = task_25_1d.Topology(topology_with_dupl_links)
    assert (
        type(top_with_data.topology) == dict
    ), f"По заданию в переменной topology должен быть словарь, а не {type(top_with_data.topology).__name__}"
    assert len(top_with_data.topology) == len(
        normalized_topology_example
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"


def test_method_add_link_created(normalized_topology_example):
    """Проверяем, что в объекте Topology есть метод add_link"""
    norm_top = task_25_1d.Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method="add_link")


def test_method_add_link(normalized_topology_example, capsys):
    """Проверка работы метода add_link"""
    norm_top = task_25_1d.Topology(normalized_topology_example)

    add_link_result = norm_top.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    assert add_link_result == None, "Метод add_link не должен ничего возвращать"

    assert (
        "R1",
        "Eth0/4",
    ) in norm_top.topology, "После добавления соединения через метод add_link, оно должно существовать в топологии"
    assert (
        len(norm_top.topology) == 7
    ), "После добавления соединения количество соединений должно быть равно 7"

    # проверка добавления существующего линка
    norm_top.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    out, err = capsys.readouterr()
    link_msg = "Такое соединение существует"
    assert (
        link_msg in out
    ), "При добавлении существующего соединения, не было выведено сообщение 'Такое соединение существует'"

    # проверка добавления линка с существующим портом
    norm_top.add_link(("R1", "Eth0/4"), ("R7", "Eth0/5"))
    out, err = capsys.readouterr()
    port_msg = "Cоединение с одним из портов существует"
    assert (
        port_msg in out
    ), "При добавлении соединения с существующим портом, не было выведено сообщение 'Cоединение с одним из портов существует'"
