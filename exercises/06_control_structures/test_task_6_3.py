import sys

sys.path.append("..")

from pyneng_common_functions import check_pytest

check_pytest(__loader__, __file__)


def test_task(capsys):
    """
    Проверка работы задания при вводе access
    """
    import task_6_3

    out, err = capsys.readouterr()
    correct_stdout = (
        "interface FastEthernet0/1\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan add 10,20\n"
        "interface FastEthernet0/2\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan 11,30\n"
        "interface FastEthernet0/4\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan remove 17\n"
        "interface FastEthernet0/5\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan add 10,21\n"
        "interface FastEthernet0/7\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan 30"
    )

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
