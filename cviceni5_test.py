import pytest
from cviceni5_data import Warehouse, Product

def test_add():
    test_warehouse = Warehouse(1000.456)
    auto_1 = Product("Fordka", 3.478)
    auto_2 = Product("Mergl", 5.478)
    assert test_warehouse.add(auto_1) == 996.98

@pytest.fixture()
def products():
    return [Product("Fordka", 3.478),
            Product("Mergl", 5.478),
            Product("Skudka", 7.12),
            Product("Oplik", 1.448),
            Product("Ferari", 2.2)]

@pytest.mark.parametrize("capacity,result",[(1000.456,980.73),(500,480.28),(10,1.04)])
def test_add_fixtura(capacity,result,products):
    test_warehouse = Warehouse(capacity)
    for product in products:
        test_warehouse.add(product)
    assert round(test_warehouse.free_space,2) == result


def test_negative_cap():
    with pytest.raises(ValueError):
        test_warehouse = Warehouse(-5)

def test_negative_volume():
    with pytest.raises(ValueError):
        p1 = Product("sss",-5)