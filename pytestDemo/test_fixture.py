import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("ABC")

    def test_fixtureDemo3(self):
        print("DEF")
@pytest.mark.usefixtures("once")
class TestExample2:

    def test_f1(self):
        print("print f1")

    def test_f2(self):
        print("print f2")

    def test_f3(self):
        print("print f3")