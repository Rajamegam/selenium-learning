import pytest


@pytest.mark.usefixtures("load_data")
class TestDataLoad():
    def test_editprofile(self,load_data):

        print(load_data)


