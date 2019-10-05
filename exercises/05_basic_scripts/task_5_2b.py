# -*- coding: utf-8 -*-
from sys import argv

'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip, pr = argv[1].split('/')
ip1, ip2, ip3, ip4 = ip.split('.')
prefix = int(pr)

ip_bin = f'{int(ip1):08b}{int(ip2):08b}{int(ip3):08b}{int(ip4):08b}'
net_bin = (ip_bin[0:prefix]) + ('0' * (32 - prefix))
net_ip1, net_ip2, net_ip3, net_ip4 = int(net_bin[0:8], 2), int(net_bin[8:16], 2), int(net_bin[16:24], 2), int(net_bin[24:32], 2)

mask = ('1' * prefix) + ((32 - prefix) * '0')
mask1, mask2, mask3, mask4 = int(mask[0:8], 2), int(mask[8:16], 2), int(mask[16:24], 2), int(mask[24:32], 2)


show = f"""
{net_ip1:<8}  {net_ip2:<8}  {net_ip3:<8}  {net_ip4:<8}
{net_ip1:08b}  {net_ip2:08b}  {net_ip3:08b}  {net_ip4:08b}

Mask:
/{prefix}
{mask1:<8}  {mask2:<8}  {mask3:<8}  {mask4:<8}
{mask1:08b}  {mask2:08b}  {mask3:08b}  {mask4:08b}
"""

print(show)

