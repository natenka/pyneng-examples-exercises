import pytest
from task_25_1 import Topology
from common_functions import check_attr_or_method


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr='topology')


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    '''Проверка удаления дублей в топологии'''
    top_with_data = Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)

