import yaml
import pytest


@pytest.fixture(scope="module")
def first_two_routers_from_devices_yaml():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        r1 = devices[0]
        r2 = devices[1]
    return r1, r2

