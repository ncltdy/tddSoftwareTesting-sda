import pytest
from matrix import *

@pytest.mark.parametrize("matrix,result", [([[1,2],[3,4]],[[1,3],[2,4]]),([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]])])
def test_matice_transpozice(matrix,result):
    assert  Matrix(matrix).transpose() == Matrix(result)


@pytest.mark.parametrize("matrix1,matrix2,result", [([[1,2],[3,4]],[[5,6],[7,8]],[[6,8],[10,12]])])
def test_matice_add(matrix1,matrix2,result):
    assert  Matrix(matrix1).add(Matrix(matrix2)) == Matrix(result)

def test_add_exeption():
    with pytest.raises(ValueError):
        Matrix([[1,2],[3,4]]).add(Matrix([[1,2,3],[4,5,6]]))