import pytest
import yaml
from netmiko import ConnectHandler


@pytest.fixture()
def topology_with_dupl_links():
    topology = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    return topology


@pytest.fixture()
def normalized_topology_example():
    normalized_topology = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    }
    return normalized_topology


@pytest.fixture(scope="module")
def first_router_from_devices_yaml():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        r1 = devices[0]
    return r1


@pytest.fixture(scope="module")
def r1_test_telnet_connection():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    r1_params = devices[0]
    options = {"device_type": "cisco_ios_telnet"}
    r1_params.update(options)
    r1 = ConnectHandler(**r1_params)
    r1.enable()
    yield r1
    r1.disconnect()
