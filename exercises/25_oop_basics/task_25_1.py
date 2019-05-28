

# Все отлично

# вариант решения

class Topology:
    def __init__(self, topology_dict):
        self.topo = {}
        for local, remote in topology_dict.items():
            if not self.topo.get(remote) == local:
                self.topo[local] = remote
    def topology(self):
        pass


if __name__ == "__main__":
    top = Topology(topology_example)
    print(top.topology)
