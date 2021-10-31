import os
import sys

import task_20_2

sys.path.append("..")

from pyneng_common_functions import check_pytest, render_jinja_template

check_pytest(__loader__, __file__)


def test_templates_exists():
    assert os.path.exists(
        "templates/cisco_router_base.txt"
    ), "Шаблон templates/cisco_router_base.txt не существует"


def test_function_return_value():
    service_section = (
        "service timestamps debug datetime msec localtime show-timezone\n"
        "service timestamps log datetime msec localtime show-timezone\n"
        "service tcp-keepalives-in\n"
        "service tcp-keepalives-out\n"
        "service password-encryption\n"
    )
    alias_section = (
        "alias exec top sh proc cpu sorted | excl 0.00%__0.00%__0.00%\n"
        "alias exec diff sh archive config differences nvram:startup-config system:running-config\n"
        "alias exec bri show ip int bri | exc unass\n"
        "alias exec id show int desc\n"
    )
    eem_section = (
        "event manager applet update-int-desc\n"
        " event neighbor-discovery interface regexp .*Ethernet.* cdp add\n"
        ' action 1.0 cli command "enable"\n'
        ' action 2.0 cli command "config t"\n'
        ' action 3.0 cli command "interface $_nd_local_intf_name"\n'
        ' action 4.0 cli command "description To $_nd_cdp_entry_name $_nd_port_id"\n'
    )

    template = "templates/cisco_router_base.txt"
    data = {"hostname": "R1"}
    return_value = render_jinja_template(template, data)
    assert service_section in return_value, "В итоговой конфигурации нет команд service"
    assert alias_section in return_value, "В итоговой конфигурации нет команд alias"
    assert (
        eem_section in return_value
    ), "В итоговой конфигурации нет настройки event manager"
    assert data["hostname"] in return_value, "В итоговой конфигурации нет hostname"
