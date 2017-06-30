
# Unpacking positional arguments

def config_interface(intf_name, ip_address, cidr_mask):
    interface = 'interface %s'
    no_shut = 'no shutdown'
    ip_addr = 'ip address %s %s'
    result = []
    result.append(interface % intf_name)
    result.append(no_shut)

    mask_bits = int(cidr_mask.split('/')[-1])
    bin_mask = '1'*mask_bits + '0'*(32-mask_bits)
    dec_mask = '.'.join([ str(int(bin_mask[i:i+8], 2)) for i in [0,8,16,24] ])

    result.append(ip_addr % (ip_address, dec_mask))
    return result

#print config_interface('Fa0/1', '10.0.1.1', '/25')

interfaces_info = [['Fa0/1', '10.0.1.1', '/24'],
                   ['Fa0/2', '10.0.2.1', '/24'],
                   ['Fa0/3', '10.0.3.1', '/24'],
                   ['Fa0/4', '10.0.4.1', '/24'],
                   ['Lo0', '10.0.0.1', '/32']]


for i in interfaces_info:
    print config_interface(*i)

"""
Output:
['interface Fa0/1', 'no shutdown', 'ip address 10.0.1.1 255.255.255.0']
['interface Fa0/2', 'no shutdown', 'ip address 10.0.2.1 255.255.255.0']
['interface Fa0/3', 'no shutdown', 'ip address 10.0.3.1 255.255.255.0']
['interface Fa0/4', 'no shutdown', 'ip address 10.0.4.1 255.255.255.0']
['interface Lo0', 'no shutdown', 'ip address 10.0.0.1 255.255.255.255']
"""

# Unpacking keyword arguments

def config_to_list(cfg_file, delete_excl=True,
                   delete_empty=True, strip_end=True):
    result = []
    with open( cfg_file ) as f:
        for line in f:
            if strip_end:
                line = line.rstrip()
            if delete_empty and not line:
                pass
            elif delete_excl and line.startswith('!'):
                pass
            else:
                result.append(line)
    return result

cfg = [dict(cfg_file='r1.txt', delete_excl=True, delete_empty=True, strip_end=True),
       dict(cfg_file='r2.txt', delete_excl=False, delete_empty=True, strip_end=True),
       dict(cfg_file='r3.txt', delete_excl=True, delete_empty=False, strip_end=True),
       dict(cfg_file='r4.txt', delete_excl=True, delete_empty=True, strip_end=False)]


for d in cfg:
    print config_to_list(**d)

"""
Output:

['service timestamps debug datetime msec localtime show-timezone year', 'service timestamps log datetime msec localtime show-timezone year', 'service password-encryption', 'service sequence-numbers', 'no ip domain lookup', 'ip ssh version 2']
['!', 'service timestamps debug datetime msec localtime show-timezone year', 'service timestamps log datetime msec localtime show-timezone year', 'service password-encryption', 'service sequence-numbers', '!', 'no ip domain lookup', '!', 'ip ssh version 2', '!']
['service timestamps debug datetime msec localtime show-timezone year', 'service timestamps log datetime msec localtime show-timezone year', 'service password-encryption', 'service sequence-numbers', '', '', '', 'ip ssh version 2', '']
['service timestamps debug datetime msec localtime show-timezone year\n', 'service timestamps log datetime msec localtime show-timezone year\n', 'service password-encryption\n', 'service sequence-numbers\n', 'no ip domain lookup\n', 'ip ssh version 2\n']

```
