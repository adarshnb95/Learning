import unittesttry

def test_add():
    assert unittesttry.add(10, 3) == 13
    assert unittesttry.add(10) == 12

def test_product():
    assert unittesttry.product(10, 3) == 30
    assert unittesttry.product(4) == 8

def test_add_strings():
    assert unittesttry.add("Hello", " World") == "Hello World"

