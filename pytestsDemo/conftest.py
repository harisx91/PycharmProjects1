#Declase the fixture and it will be avail to all .pytest files in that folder
import pytest

@pytest.fixture(scope="class")
def setup():
    print("Will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Haris", "Sumra", "speechtherapyhubnj.com"]

@pytest.fixture(params=[("chrome","Haris","Sumra"), ("Firefox", "Haris"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
