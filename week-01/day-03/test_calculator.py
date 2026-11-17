import pytest
from calculator import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [
    (10, 10, 20),
    (20, 10, 30),
    (5, 5, 10),
    (-5, 5, 0),
    (2.5, 2.5, 5.0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
    
def test_add():
    assert  add(10 ,10) == 20
    assert  add(20 ,10) == 30
    
def test_subtract():
    assert  subtract(10 ,10) == 0
    assert  subtract(20 ,10) == 10
    assert  subtract(20 ,30) == -10

def test_multiply():
    assert  multiply(10 ,2) == 20
    assert  multiply(2 ,2) == 4
    assert  multiply(10 ,-2) == -20

def test_divide():
    assert  divide(10 ,2) == 5
    assert  divide(20 ,2) == 10
    assert  divide(40 , 2) == 20

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(40 , 0) 
        divide(20 , 0) # this will not excuted as the exception raise and this will be stopped
    