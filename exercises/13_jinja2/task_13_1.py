# -*- coding: utf-8 -*-

"""
Задание 13.1

Переделать скрипт cfg_gen.py в функцию generate_cfg_from_template.

Функция ожидает два аргумента:
* путь к шаблону
* файл с переменными в формате YAML

Функция должна возвращать конфигурацию, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных data_files/for.yml.

"""

from jinja2 import Environment, FileSystemLoader
import yaml
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

TEMPLATE_DIR, template = sys.argv[1].split('/')
VARS_FILE = sys.argv[2]

env = Environment(loader = FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)
template = env.get_template(template)

vars_dict = yaml.load( open( VARS_FILE ) )

print template.render( vars_dict )
