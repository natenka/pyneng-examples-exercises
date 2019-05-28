import pytest
import task_25_1a
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_25_1a, 'Topology')


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = task_25_1a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr='topology')


def test_method_normalize(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть метод _normalize'''
    top_with_data = task_25_1a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, method='_normalize')


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    '''Проверка удаления дублей в топологии'''
    top_with_data = task_25_1a.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


