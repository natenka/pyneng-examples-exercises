# -*- coding: utf-8 -*-

try:
    a = raw_input("Введите первое число: ")
    b = raw_input("Введите второе число: ")
    print "Результат: ", int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print "Что-то пошло не так..."

"""
Example:

$ python divide_ver2.py
Введите первое число: wer
Введите второе число: 4
Результат:  Что-то пошло не так...

$ python divide_ver2.py
Введите первое число: 5
Введите второе число: 0
Результат:  Что-то пошло не так...
"""
