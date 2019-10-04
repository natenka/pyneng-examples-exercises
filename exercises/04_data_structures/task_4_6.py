# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
protocol, prefix, ad_metric, via, n_hop, l_update, intf = ospf_route.split()

show1 = f"""
Protocol:              {protocol}SPF
Prefix:                {prefix}
AD/Metric:             {ad_metric.strip('[]')}
Next-Hop:              {n_hop.rstrip(',')}
Last update:           {l_update.rstrip(',')}
Outbound Interface:    {intf}
"""
print(show1)

template = """
Protocol:              {}SPF
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
"""
show2 = template.format(protocol, prefix, ad_metric.strip('[]'), n_hop.rstrip(','), l_update.rstrip(','), intf)
print(show2)

