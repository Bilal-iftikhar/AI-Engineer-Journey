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

@pytest.mark.parametrize("c, d, expected", [
    (10, 10, 0),
    (20, 10, 10),
    (5, 5, 0),
    (15, 5, 10),
    (2.5, 2.5, 0)
])

def test_subtract(c, d, expected):
    assert subtract(c, d) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 10, 100),
    (2, 10, 20),
    (5, 5, 25),
    (15, 5, 75),
    (5, 2, 10),
    (-5, 2, -10),
    (2.5, 2, 5.0),
])

def test_multiply(a,b, expected):
    assert multiply(a,b)==expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 10, 1),
    (10, 2, 5),
    (5, 5, 1),
    (15, 5, 3),
    (-10, 2, -5),
    (2.5, 0.5, 5.0),
    (20, 2, 10)
])
def test_divide(a,b, expected):
    assert divide(a , b)==expected

def test_division_by_zero():
    with pytest.raises(
        ZeroDivisionError,
        match="Cannot divide by zero"
    ):
        divide(10, 0)