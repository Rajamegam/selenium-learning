import pytest


class Testclass:
    @pytest.mark.parametrize('num1,num2', [(1, 1), (2, 3), (3, 3), (4, 5)])
    def test_calculation(self, num1, num2):
        assert num1 == num2
