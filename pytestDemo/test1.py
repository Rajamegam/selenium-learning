import pytest


class TestClass:
    @pytest.fixture()
    def setup(self):
        print("This will launch the browser")
        yield
        print("close the browser")

    def testMethod(self,setup):
        print("This is my first method")

    def testMethods(self,setup):
        print("This is my second method")