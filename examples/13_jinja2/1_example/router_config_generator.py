# -*- coding: utf-8 -*-
import yaml
from jinja2 import Template
from router_template import template_r1

routers = yaml.load(open('routers_info.yml'))

for router in routers:
    r1_conf = router['name']+'_r1.txt'
    with open(r1_conf,'w') as f:
        f.write(template_r1.render( router ))
