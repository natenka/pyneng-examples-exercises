# -*- coding: utf-8 -*-

"""
Задание 11.5a

После выполнения задания 11.5, в таблице dhcp есть новое поле last_active.

Обновите скрипт add_data.py, таким образом, чтобы он удалял все записи,
которые были активными более 7 дней назад.

Для того, чтобы получить такие записи, можно просто вручную обновить поле last_active.

В файле задания описан пример работы с объектами модуля datetime.
Обратите внимание, что объекты, как и строки с датой, которые пишутся в БД,
можно сравнивать между собой.

"""

from datetime import timedelta, datetime

now = datetime.today().replace(microsecond=0)
week_ago = now - timedelta(days = 7)

#print now
#print week_ago
#print now > week_ago
#print str(now) > str(week_ago)

