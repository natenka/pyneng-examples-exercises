# -*- coding: utf-8 -*-

"""
Задание 13.2

На основе конфигурации config_r1.txt, создать шаблоны:
* templates/cisco_base.txt - в нем должны быть все строки, кроме настройки alias и event manager
 * имя хоста должно быть переменной hostname
* templates/alias.txt - в этот шаблон перенести все alias
* templates/eem_int_desc.txt - в этом шаблоне должен быть event manager applet

В шаблонах templates/alias.txt и templates/eem_int_desc.txt переменных нет.

Создать шаблон templates/cisco_router_base.txt.
В шаблон должно быть включено содержимое шаблонов:
* templates/cisco_base.txt
* templates/alias.txt
* templates/eem_int_desc.txt

При этом, нельзя копировать текст шаблонов.

Проверьте шаблон templates/cisco_router_base.txt,
с помощью функции generate_cfg_from_template из задания 13.1-13.1d.
Не копируйте код функции.

В качестве данных, используйте словарь router_info

"""

router_info = { 'hostname': 'R1' }
