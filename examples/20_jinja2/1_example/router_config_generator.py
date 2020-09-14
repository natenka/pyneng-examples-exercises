# -*- coding: utf-8 -*-
import yaml
from router_template import template_r1

with open('routers_info.yml') as f
    routers = yaml.safe_load(f)

for router in routers:
    r1_conf = router['name'] + '_r1.txt'
    with open(r1_conf, 'w') as f:
        f.write(template_r1.render(router))
