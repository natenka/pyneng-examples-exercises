import re
from pprint import pprint


def parse_cdp(filename):
    regex = ('Device ID: (?P<device>\S+)\n.*?'
             ' +IP address: (?P<ip>\S+).+?'
             'Platform: (?P<platform>\S+ \S+),.+?'
             'Version (?P<ios>\S+),')

    result = {}

    with open('sh_cdp_neighbors_sw1.txt') as f:
        match_iter = re.finditer(regex, f.read(), re.DOTALL)
        for match in match_iter:
            device = match.group('device')
            groupdict = match.groupdict()
            del groupdict['device']
            result[device] = groupdict

    return result


pprint(parse_cdp('sh_cdp_neighbors_sw1.txt'))
