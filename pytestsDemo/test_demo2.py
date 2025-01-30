##Any pyTest fild should start with test_ or ends with _test
#Pytest method names should start with test
#ANy code should be wrapped in method only
#Method name should have sense
# - k stands for method name execution, -s logo in out out and -v stands for more info methadata
#you can run specified with py.test <filename>
#mark(tag) the test case and tell your CMD to runs only those mark tests such as -m
#mark(tage) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail (it will run but wont give report)
#fixtures are used for setup and tear down methods eneralize fixture for test cases - conftest files to ges
#fixtures make it avail to all test cases
#Data driven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke #for smoke test
@pytest.mark.skip #for skipping
def test_firstProgram():
    msg = "Hello" #operation
    assert msg == "Hi" , "Test failed because string did not match"

@pytest.mark.xfail #It will run but wont report
def test_secondProgram():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition did not match"

@pytest.fixture()
def setup():
    print("Will be executed first")

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")

    
