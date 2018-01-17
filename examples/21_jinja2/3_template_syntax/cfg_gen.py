# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os

#$ python cfg_gen.py templates/for.txt data_files/for.yml
TEMPLATE_DIR, template = os.path.split(sys.argv[1])

VARS_FILE = sys.argv[2]

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    trim_blocks=True,
    lstrip_blocks=True)
template = env.get_template(template_file)

vars_dict = yaml.load(open(VARS_FILE))

print(template.render(vars_dict))
