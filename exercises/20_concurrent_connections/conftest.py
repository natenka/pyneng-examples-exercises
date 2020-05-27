import yaml
import pytest
from netmiko import ConnectHandler


@pytest.fixture(scope="module")
def three_routers_from_devices_yaml():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        devices = devices[:3]
        options = {"timeout": 5, "fast_cli": True}
        for device in devices:
            device.update(options)
    return devices


@pytest.fixture(scope="module")
def r1_r2_r3_test_connection(three_routers_from_devices_yaml):
    connections = []
    for params in three_routers_from_devices_yaml:
        router = ConnectHandler(**params)
        router.enable()
        connections.append(router)
    yield connections
    for r in connections:
        r.disconnect()


def create_ssh_connect(device):
    connection = ConnectHandler(**device)
    connection.enable()
    return connection
