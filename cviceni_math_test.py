import pytest
from cviceni_math import *

@pytest.mark.skip
@pytest.mark.parametrize("number,result", [(1,False),(2,True),(0,False),(6,False),(7,True),(101,True),(-101,False),(999999000001,True)])
def test_is_prime(number,result):
    assert is_prime(number) == result


@pytest.mark.skip
def test_is_prime_exeption():
    with pytest.raises(TypeError):
        is_prime("101")


@pytest.mark.parametrize("number,result", [(5,120),(10,3628800), (-5,None), (0,1),(1,1),(2,2),(3,6)])
def test_factorial(number,result):
    assert factorial2(number) == result

def test_factorial_exeption():
    with pytest.raises(TypeError):
        factorial2("5")