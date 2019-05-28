import pytest
from task_25_1d import Topology
import warnings
from common_functions import check_attr_or_method, stdout_incorrect_warning


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr='topology')


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    '''Проверка удаления дублей в топологии'''
    top_with_data = Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_method_add_link(normalized_topology_example, capsys):
    '''Проверка наличия метода add_link и его работы'''
    norm_top = Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method='add_link')

    add_link_result = norm_top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    assert add_link_result == None, 'Метод add_link не должен ничего возвращать'

    assert ('R1', 'Eth0/4') in norm_top.topology
    assert len(norm_top.topology) == 7

    #проверка добавления существующего линка
    norm_top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    out, err = capsys.readouterr()
    link_msg = 'Такое соединение существует\n'
    if not out == link_msg:
        warnings.warn(UserWarning(stdout_incorrect_warning.format(link_msg, out)))

    #проверка добавления линка с существующим портом
    norm_top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
    out, err = capsys.readouterr()
    port_msg = 'Cоединение с одним из портов существует\n'
    if not out == port_msg:
        warnings.warn(UserWarning(stdout_incorrect_warning.format(port_msg, out)))

