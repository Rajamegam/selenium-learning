import pytest


@pytest.fixture()
def setup():
    print("I will be run first")
    yield
    print("I will be run last")


@pytest.fixture(scope="class")
def once():
    print("I will execute only once ")


@pytest.fixture()
def load_data():
    print(" the value will be passed here for user creation")
    return ["rajamegam", "govindaraj", "rajamegam7@gmail.com"]


@pytest.fixture(params=["chrome", "firefox", "IE"])
def datasets(request):
    return request.param
