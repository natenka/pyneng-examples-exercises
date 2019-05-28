import pytest
import task_26_1a
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_26_1a, 'Topology')


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = task_26_1a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr='topology')


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    '''Проверка удаления дублей в топологии'''
    top_with_data = task_26_1a.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_iterable(normalized_topology_example):
    '''Проверка работы Topology как итерируемого объекта'''
    top1 = task_26_1a.Topology(normalized_topology_example)
    try:
        iterator = iter(top1)
    except TypeError as error:
        pytest.fail('Экземпляр класса Topology не итерируемый объект\n', error)

