import re
import yaml
import pytest
from netmiko import ConnectHandler


@pytest.fixture(scope="module")
def first_router_from_devices_yaml():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        r1 = devices[0]
    return r1


@pytest.fixture(scope="module")
def r1_test_connection():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    r1_params = devices[0]
    r1 = ConnectHandler(**r1_params)
    r1.enable()
    yield r1
    r1.disconnect()
