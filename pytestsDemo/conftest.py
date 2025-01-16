#Declase the fixture and it will be avail to all .pytest files in that folder
import pytest

@pytest.fixture(scope="class")
def setup():
    print("Will be executed first")
    yield
    print("I will be executed last")
