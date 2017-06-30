import sw_int_templates
from sw_data import sw1_fast_int


def generate_access_cfg(sw_dict):
    result = []
    for intf in sw_dict['access']:
        result.append('interface FastEthernet' + intf)
        for command in sw_int_templates.access_template:
            if command.endswith('access vlan'):
                result.append(' %s %s' % (command, sw_dict['access'][intf]))
            else:
                result.append(' %s' % command)
    return result

if __name__ == "__main__":
    print '\n'.join(generate_access_cfg(sw1_fast_int))

