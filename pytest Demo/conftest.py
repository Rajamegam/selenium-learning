import pytest


@pytest.fixture()
def setup():
    print("I will be run first")
    yield
    print("I will be run last")

@pytest.fixture(scope="class")
def once():
    print("I will execute only once ")