import sys

import task_22_1d

sys.path.append("..")

from pyneng_common_functions import (check_attr_or_method, check_class_exists,
                                     check_pytest, stdout_incorrect_warning,
                                     unify_topology_dict)

check_pytest(__loader__, __file__)


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(task_22_1d, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    return_value = task_22_1d.Topology(topology_with_dupl_links)
    check_attr_or_method(return_value, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Проверка удаления дублей в топологии"""
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = task_22_1d.Topology(topology_with_dupl_links)
    assert (
        type(return_value.topology) == dict
    ), f"По заданию в переменной topology должен быть словарь, а не {type(return_value.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"


def test_method_add_link_created(normalized_topology_example):
    """Проверяем, что в объекте Topology есть метод add_link"""
    return_value = task_22_1d.Topology(normalized_topology_example)
    check_attr_or_method(return_value, method="add_link")


def test_method_add_link(normalized_topology_example, capsys):
    """Проверка работы метода add_link"""
    return_value = task_22_1d.Topology(normalized_topology_example)

    add_link_result = return_value.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    assert None == add_link_result, "Метод add_link не должен ничего возвращать"

    assert (
        "R1",
        "Eth0/4",
    ) in return_value.topology, "После добавления соединения через метод add_link, оно должно существовать в топологии"
    assert 7 == len(
        return_value.topology
    ), "После добавления соединения количество соединений должно быть равно 7"

    # проверка добавления существующего линка
    return_value.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    out, err = capsys.readouterr()
    assert (
        "Такое соединение существует" in out
    ), "При добавлении существующего соединения, не было выведено сообщение 'Такое соединение существует'"

    # проверка добавления линка с существующим портом
    return_value.add_link(("R1", "Eth0/4"), ("R7", "Eth0/5"))
    out, err = capsys.readouterr()
    assert (
        "Соединение с одним из портов существует" in out
    ), "При добавлении соединения с существующим портом, не было выведено сообщение 'Соединение с одним из портов существует'"
