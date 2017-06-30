# -*- coding: utf-8 -*-
'''
Задание 3.1
Обработать строку ospf_route и вывести информацию в виде:
Protocol:				OSPF
Prefix:					10.0.24.0/24
AD/Metric:				110/41
Next-Hop:				10.0.13.3
Last update:			3d18h
Outbound Interface:		FastEthernet0/0


> В разделе [Форматирование строк](https://natenka.gitbooks.io/pyneng/content/book/03_data_structures/4b_string_format.html) добавились примеры, которые помогут с отображением вывода столбцами.
'''

ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
