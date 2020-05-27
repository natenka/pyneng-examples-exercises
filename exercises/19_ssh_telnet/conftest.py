import yaml
import pytest
from netmiko import ConnectHandler


@pytest.fixture(scope="module")
def first_router_from_devices_yaml():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        r1 = devices[0]
        options = {"timeout": 5, "fast_cli": True}
        r1.update(options)
    return r1


@pytest.fixture(scope="module")
def r1_test_connection(first_router_from_devices_yaml):
    r1 = ConnectHandler(**first_router_from_devices_yaml)
    r1.enable()
    yield r1
    r1.disconnect()


@pytest.fixture(scope="module")
def first_router_wrong_pass(first_router_from_devices_yaml):
    r1 = first_router_from_devices_yaml.copy()
    r1["password"] = "wrong"
    return r1


@pytest.fixture(scope="module")
def first_router_wrong_ip(first_router_from_devices_yaml):
    r1 = first_router_from_devices_yaml.copy()
    r1["ip"] = "unreachable"
    return r1
