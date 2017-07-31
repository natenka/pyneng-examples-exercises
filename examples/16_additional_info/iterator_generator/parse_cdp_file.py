import re
from pprint import pprint

def get_cdp_neighbor(sh_cdp_neighbor_detail):
    with open(sh_cdp_neighbor_detail) as f:
        line = ''
        while True:
            while not 'Device ID' in line:
                line = f.readline()
            neighbor = ''
            neighbor += line
            for line in f:
                if line.startswith('-----'):
                    break
                neighbor += line
            yield neighbor
            line = f.readline()
            if not line:
                return


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

