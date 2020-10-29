# -*- coding: utf-8 -*-
"""
Задание 20.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

"""
import os
from jinja2 import Environment, FileSystemLoader
import yaml


def generate_config(template, data_dict):
    templ_dir, templ_file = os.path.split(template)
    env = Environment(
        loader=FileSystemLoader(templ_dir), trim_blocks=True, lstrip_blocks=True
    )
    templ = env.get_template(templ_file)
    return templ.render(data_dict)


if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))
