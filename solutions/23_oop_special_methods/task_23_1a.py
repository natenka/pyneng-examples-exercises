# -*- coding: utf-8 -*-

"""
Задание 23.1a

Скопировать и изменить класс IPAddress из задания 23.1.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""
import ipaddress

class IPAddress:
    def __init__(self, ipaddress):
        ip, mask = ipaddress.split("/")
        self._check_ip(ip)
        self._check_mask(mask)
        self.ip, self.mask = ip, int(mask)

    def _check_ip(self, ip):
        octets = ip.split(".")
        correct_octets = [
            octet for octet in octets if octet.isdigit() and 0 <= int(octet) <= 255
        ]
        if len(octets) == 4 and len(correct_octets) == 4:
            return True
        else:
            raise ValueError("Incorrect IPv4 address")

    def _check_mask(self, mask):
        if mask.isdigit() and 8 <= int(mask) <= 32:
            return True
        else:
            raise ValueError("Incorrect mask")

    def __str__(self):
        return f"IP address {self.ip}/{self.mask}"

    def __repr__(self):
        return f"IPAddress('{self.ip}/{self.mask}')"
