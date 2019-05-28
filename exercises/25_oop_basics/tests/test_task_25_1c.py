import pytest
import warnings
import task_25_1c
import sys
sys.path.append('..')

from common_functions import (check_class_exists, check_attr_or_method,
                              stdout_incorrect_warning)


def test_class_created():
    check_class_exists(task_25_1c, 'Topology')


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = task_25_1c.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr='topology')


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    '''Проверка удаления дублей в топологии'''
    top_with_data = task_25_1c.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_method_delete_node(normalized_topology_example, capsys):
    '''Проверка наличия метода delete_node и его работы'''
    norm_top = task_25_1c.Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method='delete_node')

    node = 'SW1'
    delete_node_result = norm_top.delete_node(node)
    assert delete_node_result == None, 'Метод delete_node не должен ничего возвращать'

    ports_with_node = [src for src, dst in norm_top.topology.items()
                       if node in src or node in dst]
    assert len(ports_with_node) == 0
    assert len(norm_top.topology) == 3

    #проверка удаления несуществующего устройства
    norm_top.delete_node(node)
    out, err = capsys.readouterr()
    node_msg = 'Такого устройства нет'
    if not node_msg in out:
        warnings.warn(UserWarning(stdout_incorrect_warning.format(node_msg, out)))

