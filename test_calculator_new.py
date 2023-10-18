import pytest
import calculator
from pytest import approx

# addition tests
def test_addition_1():
    assert calculator.add(2, 3) == 5
def test_addition_2():
    assert calculator.add(-1, 1) == 0
def test_addition_3():
    assert calculator.add(-2, -3) == -5

# subtraction tests
def test_subtraction_1():
    assert calculator.subtract(5,2) == 3
def test_subtraction_2():
    assert calculator.subtract(5,45) == -40
def test_subtraction_3():
    assert calculator.subtract(5,-4) == 9
def test_subtraction_4():    
    assert calculator.subtract(0,5) == -5

# multiplication tests
def test_multiply_1():
    assert calculator.multiply(5,2) == 10
def test_multiply_2():
    assert calculator.multiply(5,-4) == -20
def test_multiply_3():
    assert calculator.multiply(5,0) == 0

# division
def test_divide_1():
    assert round(calculator.divide(5,3),2) == 1.67
def test_divide_2():
    assert round(calculator.divide(5,-3),2) == -1.67
def test_divide_3():
    assert calculator.divide(5,0) == "Cannot divide by 0"

# using parametrize for a cleaner test case
@pytest.mark.parametrize("num1,num2,expected_result",[(2,3,5),(-1,1,0),(-2,-3,-5)])
def test_addition_params(num1, num2, expected_result):
    result = calculator.add(num1, num2)
    assert result == expected_result

@pytest.mark.parametrize("num1,num2,expected_result",[(5,2,3),(5,45,-40),(5,-4,9),(0,5,-5)])
def test_subtraction_params(num1, num2, expected_result):
    result = calculator.subtract(num1, num2)
    assert result == expected_result

@pytest.mark.parametrize("num1,num2,expected_result",[(5,2,10),(5,-4,-20),(5,0,0)])
def test_multiply_params(num1, num2, expected_result):
    result = calculator.multiply(num1, num2)
    assert result == expected_result

@pytest.mark.parametrize("num1,num2,expected_result",[(5,3,1.67),(5,-3,-1.67)])
def test_divide_params(num1, num2, expected_result):
    result = round(calculator.divide(num1, num2),2)
    assert result == expected_result