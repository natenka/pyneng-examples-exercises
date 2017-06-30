# -*- coding: utf-8 -*-

username = raw_input('Введите имя пользователя: ' )
password = raw_input('Введите пароль: ' )

if len(password) < 8:
    print 'Пароль слишком короткий'
elif username in password:
    print 'Пароль содержит имя пользователя'
else:
    print 'Пароль для пользователя %s установлен' % username

"""
Usage example:

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: nata1234
Пароль содержит имя пользователя

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: 123nata123
Пароль содержит имя пользователя

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: 1234
Пароль слишком короткий

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: 123456789
Пароль для пользователя nata установлен
"""
