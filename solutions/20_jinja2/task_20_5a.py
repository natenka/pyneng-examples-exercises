# -*- coding: utf-8 -*-
"""
Задание 20.5a

Создать функцию configure_vpn, которая использует шаблоны из задания 20.5 для настройки VPN на маршрутизаторах на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству
* dst_device_params - словарь с параметрами подключения к устройству
* src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов и данных на каждом устройстве с помощью netmiko.
Функция возвращает вывод с набором команд с двух марушртизаторов (вывод, которые возвращает метод netmiko send_config_set).

При этом, в словаре data не указан номер интерфейса Tunnel, который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel, взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 9.
И надо будет настроить интерфейс Tunnel 9.

Для этого задания нет теста!
"""
import re

import yaml
from netmiko import ConnectHandler
from task_20_5 import create_vpn_config


def get_free_tunnel_number(src, dst):
    nums = [int(num) for num in re.findall("Tunnel(\d+)", src + dst)]
    if not nums:
        return 0
    return max(nums) + 1


def configure_vpn(
    src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict
):
    with ConnectHandler(**src_device_params) as src, ConnectHandler(
        **dst_device_params
    ) as dst:
        src.enable()
        dst.enable()
        tunnels_src = src.send_command("sh run | include ^interface Tunnel")
        tunnels_dst = dst.send_command("sh run | include ^interface Tunnel")
        tun_num = get_free_tunnel_number(tunnels_src, tunnels_dst)
        vpn_data_dict["tun_num"] = tun_num
        vpn1, vpn2 = create_vpn_config(src_template, dst_template, vpn_data_dict)
        output = src.send_config_set(vpn1.split("\n"))
        output += dst.send_config_set(vpn2.split("\n"))
    return output


if __name__ == "__main__":
    template1 = "templates/gre_ipsec_vpn_1.txt"
    template2 = "templates/gre_ipsec_vpn_2.txt"

    data = {
        "tun_num": None,
        "wan_ip_1": "192.168.100.1",
        "wan_ip_2": "192.168.100.2",
        "tun_ip_1": "10.0.1.1 255.255.255.252",
        "tun_ip_2": "10.0.1.2 255.255.255.252",
    }

    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        r1, r2 = devices[:2]
    configure_vpn(r1, r2, template1, template2, data)
