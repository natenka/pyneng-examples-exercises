# Unpacking positional arguments

def config_interface(intf_name, ip_address, mask):
    interface = f'interface {intf_name}'
    no_shut = 'no shutdown'
    ip_addr = f'ip address {ip_address} {mask}'
    result = [interface, no_shut, ip_addr]
    return result

interfaces_info = [['Fa0/1', '10.0.1.1', '255.255.255.0'],
                   ['Fa0/2', '10.0.2.1', '255.255.255.0'],
                   ['Fa0/3', '10.0.3.1', '255.255.255.0'],
                   ['Fa0/4', '10.0.4.1', '255.255.255.0'],
                   ['Lo0', '10.0.0.1', '255.255.255.255']]


for info in interfaces_info:
    print(config_interface(*info))

'''
Output:

['interface Fa0/1', 'no shutdown', 'ip address 10.0.1.1 255.255.255.0']
['interface Fa0/2', 'no shutdown', 'ip address 10.0.2.1 255.255.255.0']
['interface Fa0/3', 'no shutdown', 'ip address 10.0.3.1 255.255.255.0']
['interface Fa0/4', 'no shutdown', 'ip address 10.0.4.1 255.255.255.0']
['interface Lo0', 'no shutdown', 'ip address 10.0.0.1 255.255.255.255']
'''
