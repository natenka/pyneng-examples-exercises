import re
from pprint import pprint
from itertools import dropwhile, takewhile

def get_cdp_neighbor(sh_cdp_neighbor_detail):
    with open(sh_cdp_neighbor_detail) as f:
        while True:
            f = dropwhile(lambda x: not 'Device ID' in x, f)
            lines = takewhile(lambda y: not '-----' in y, f)
            neighbor = ''.join(lines)
            if not neighbor:
                return
            yield neighbor


def parse_cdp(output):
    regex = ('Device ID: (?P<device>\S+)'
             '|IP address: (?P<ip>\S+)'
             '|Platform: (?P<platform>\S+ \S+),'
             '|Cisco IOS Software, (?P<ios>.+), RELEASE')

    result = {}

    match_iter = re.finditer(regex, output)
    for match in match_iter:
        if match.lastgroup == 'device':
            device = match.group(match.lastgroup)
            result[device] = {}
        elif device:
            result[device][match.lastgroup] = match.group(match.lastgroup)

    return result


filename = 'sh_cdp_neighbors_detail.txt'
result = get_cdp_neighbor(filename)

all_cdp = {}
for cdp in result:
    all_cdp.update(parse_cdp(cdp))

pprint(all_cdp)

