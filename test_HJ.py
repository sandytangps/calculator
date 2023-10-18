from calculator import*
import pytest

@pytest.mark.parametrize("num1,num2,result",[(-3, -2,-5),(-1,0,-1), (1,2,3), (3,4,7),(-1,1,0)])
def test_add(num1, num2, result):
    assert add(num1, num2) == result

@pytest.mark.parametrize("num1,num2,result",[(-3, -1,-2),(-2,0,-2), (0,2,-2), (3,-3,6),(-3,4,-7)])
def test_subtract(num1,num2,result):
    assert subtract(num1, num2) == result

@pytest.mark.parametrize("num1,num2,result",[(-3, -2,6),(-1,0,0), (1,2,2), (3,-4,-12),(0,0,0),(-2,4,-8)])
def test_multiply(num1,num2,result):
    assert multiply(num1, num2) == result

@pytest.mark.parametrize("num1,num2,result",[(-4, -2,2),(-1,0,"Cannot divide by zero"), (1,2,0.5), (3,-4,-0.75),(0,-1,0),(0,0,"Cannot divide by zero")])
def test_divide(num1,num2,result):
    assert divide(num1, num2) == result