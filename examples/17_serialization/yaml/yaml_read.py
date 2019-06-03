import yaml
from pprint import pprint

with open('info.yaml') as f:
    templates = yaml.load(f)

pprint(templates)
