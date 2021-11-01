# -*- coding: utf-8 -*-
import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('router_template.txt')

with open('routers_info.yml') as f:
    routers = yaml.safe_load(f)

for router in routers:
    r1_conf = router['name'] + '_r1.txt'
    with open(r1_conf, 'w') as f:
        f.write(template.render(router))
