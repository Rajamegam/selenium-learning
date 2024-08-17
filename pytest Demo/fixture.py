import pytest


@pytest.fixture()
def setup():
    print("I will be run first")
    yield
    print("I will be run last")

def test_fixtureDemo(setup):
    print("i will execute steps in fixtureDemo method")