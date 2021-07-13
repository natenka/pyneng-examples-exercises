import pytest
import task_23_3a
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_23_3a, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    top_with_data = task_23_3a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Проверка удаления дублей в топологии"""
    top_with_data = task_23_3a.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_iterable(normalized_topology_example):
    """Проверка работы Topology как итерируемого объекта"""
    top1 = task_23_3a.Topology(normalized_topology_example)
    try:
        iterator = iter(top1)
    except TypeError as error:
        pytest.fail("Экземпляр класса Topology не итерируемый объект\n", error)
    else:
        item = next(iterator)
        assert (("R1", "Eth0/0"), ("SW1", "Eth0/1")) == item
