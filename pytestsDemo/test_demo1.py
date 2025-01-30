##Any pyTest fild should start with test_ or ends with _test
#Pytest method names should start with test
#ANy code should be wrapped in method only
import pytest

@pytest.mark.smoke

def test_firstProgram(setup):
    print("Hello")

def test_secondProgram():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

