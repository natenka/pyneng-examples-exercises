# -*- coding: utf-8 -*-

try:
    a = raw_input("Введите первое число: ")
    b = raw_input("Введите второе число: ")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print "Что-то пошло не так..."
else:
    print "Результат в квадрате: ", result**2

"""
Example:

$ python divide_ver3.py
Введите первое число: 10
Введите второе число: 2
Результат в квадрате:  25

$ python divide_ver3.py
Введите первое число: werq
Введите второе число: 3
Что-то пошло не так...
"""
