import pytest


@pytest.fixture(scope='session')
def list_of_ips():
    ips = ['1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']
    return ips


@pytest.fixture(scope='session')
def list_of_ips_and_ranges():
    ips_and_ranges = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    return ips_and_ranges


