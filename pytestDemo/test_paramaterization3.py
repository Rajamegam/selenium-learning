import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expected", [(8, 3, 11), (5, 2, 66), (100, 200, 300)])
def test_addition(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b",[(3, 4), (-2, -2), (11, -4)])
def test_positive_number(a, b):
    assert a > 0
    assert b > 0
