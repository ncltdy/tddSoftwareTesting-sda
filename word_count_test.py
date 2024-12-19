import pytest
from word_count import *

@pytest.mark.parametrize("string,result", [("auto jede do kopce",4),("",0),("   ",0),("auto",1),(123,1)])
def test_word_count(string,result):
    assert word_count2(string) == result