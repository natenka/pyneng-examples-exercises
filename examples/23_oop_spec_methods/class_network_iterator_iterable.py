import ipaddress


# Iterator
class Network:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]
        self._index = 0

    def __iter__(self):
        print('Вызываю __iter__')
        return self

    def __next__(self):
        print('Вызываю __next__')
        if self._index < len(self.addresses):
            current_address = self.addresses[self._index]
            self._index += 1
            return current_address
        else:
            raise StopIteration


net1 = Network('10.1.1.192/30')

for ip in net1:
    print(ip)

'''
Вызываю __iter__
Вызываю __next__
10.1.1.193
Вызываю __next__
10.1.1.194
Вызываю __next__
'''

# Iterable
class Network:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]

    def __iter__(self):
        return iter(self.addresses)

net1 = Network('10.1.1.192/30')

for ip in net1:
    print(ip)


