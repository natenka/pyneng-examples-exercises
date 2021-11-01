import sys

import task_23_2

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_pytest

check_pytest(__loader__, __file__)


def test_class_created():
    check_class_exists(task_23_2, "CiscoTelnet")


def test_method_enter_exit(first_router_from_devices_yaml):
    assert (
        getattr(task_23_2.CiscoTelnet, "__enter__", None) != None
    ), "У класса CiscoTelnet должен быть метод __enter__"

    assert (
        getattr(task_23_2.CiscoTelnet, "__exit__", None) != None
    ), "У класса CiscoTelnet должен быть метод __exit__"

    with task_23_2.CiscoTelnet(**first_router_from_devices_yaml) as r1:
        r1.send_show_command("sh clock")
