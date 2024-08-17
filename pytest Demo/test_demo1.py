import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_program_one():
    print("Hello")

def test_secondprogram():
    print("Rajamegam")

@pytest.mark.xfail
def test_thirdprogram():
    print("Rajamegam")


