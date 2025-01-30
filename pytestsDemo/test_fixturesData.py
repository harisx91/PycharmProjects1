##When you returning fixture globally than parameter is not required
import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self,dataLoad):
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])

