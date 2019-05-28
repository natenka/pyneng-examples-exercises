import pytest
import warnings
import task_25_1b
import sys
sys.path.append('..')

from common_functions import (check_class_exists, check_attr_or_method,
                              stdout_incorrect_warning)


def test_class_created():
    check_class_exists(task_25_1b, 'Topology')


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = task_25_1b.Topology(topology_with_dupl_links)
    assert getattr(top_with_data, 'topology', None) != None


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    '''Проверка удаления дублей в топологии'''
    top_with_data = task_25_1b.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_method_delete_link(normalized_topology_example, capsys):
    '''Проверка наличия метода delete_link и его работы'''
    norm_top = task_25_1b.Topology(normalized_topology_example)
    assert getattr(norm_top, 'delete_link', None) != None

    delete_link_result = norm_top.delete_link(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
    assert delete_link_result == None, 'Метод delete_link не должен ничего возвращать'

    assert ('R3', 'Eth0/0') not in norm_top.topology

    #проверка удаления зеркального линка
    norm_top.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
    assert ('R3', 'Eth0/2') not in norm_top.topology

    #проверка удаления несуществующего линка
    norm_top.delete_link(('R8', 'Eth0/2'), ('R9', 'Eth0/1'))
    out, err = capsys.readouterr()
    link_msg = 'Такого соединения нет'
    assert link_msg in out

