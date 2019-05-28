import pytest
import task_25_1
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_25_1, 'Topology')


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = task_25_1.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr='topology')


def test_topology_normalization():
    '''Проверка удаления дублей в топологии'''
    topology_with_dupl_links = {
        ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
        ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
        ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
        ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
        ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
        ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
        ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
        ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
        ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')
    }
    normalized_topology_example = {
        ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
        ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
        ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
        ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
        ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
        ('R3', 'Eth0/2'): ('R5', 'Eth0/0')
    }

    top_with_data = task_25_1.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)

