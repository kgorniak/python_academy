import pytest


@pytest.fixture(autouse=True)
def setup_method(self, method):
    print("setup_method")


@pytest.fixture(autouse=True)
def teardown_method(self, method):
    print("teardown_method")
