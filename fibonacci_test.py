import pytest
from fibonacci import *

@pytest.mark.parametrize("number,result", [(5,3),(16,610),(-5,None)])
def test_fibonacci(number,result):
    assert fibonacci2(number) == result