import pytest
import warnings
import task_25_1d
import sys
sys.path.append('..')

from common_functions import (check_class_exists, check_attr_or_method,
                              stdout_incorrect_warning)


def test_class_created():
    check_class_exists(task_25_1d, 'Topology')


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = task_25_1d.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr='topology')


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    '''Проверка удаления дублей в топологии'''
    top_with_data = task_25_1d.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_method_add_link(normalized_topology_example, capsys):
    '''Проверка наличия метода add_link и его работы'''
    norm_top = task_25_1d.Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method='add_link')

    add_link_result = norm_top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    assert add_link_result == None, 'Метод add_link не должен ничего возвращать'

    assert ('R1', 'Eth0/4') in norm_top.topology
    assert len(norm_top.topology) == 7

    #проверка добавления существующего линка
    norm_top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    out, err = capsys.readouterr()
    link_msg = 'Такое соединение существует'
    if not link_msg in out:
        warnings.warn(UserWarning(stdout_incorrect_warning.format(link_msg, out)))

    #проверка добавления линка с существующим портом
    norm_top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
    out, err = capsys.readouterr()
    port_msg = 'Cоединение с одним из портов существует'
    if not port_msg in out:
        warnings.warn(UserWarning(stdout_incorrect_warning.format(port_msg, out)))

