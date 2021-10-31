from pprint import pprint

import yaml

with open('info.yaml') as f:
    templates = yaml.safe_load(f)

pprint(templates)
