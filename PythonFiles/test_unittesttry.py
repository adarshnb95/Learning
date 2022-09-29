import unittesttry
import pytest

@pytest.fixture(scope='module')
def db():
    print("-------setup-------")
    db = unittesttry.StudentDB()
    db.connect('data.json')
    yield db
    print("-------teardown-------")
    db.close()

@pytest.mark.numbers
def test_add():
    assert unittesttry.add(10, 3) == 13
    assert unittesttry.add(10) == 12

@pytest.mark.numbers
def test_product():
    assert unittesttry.product(10, 3) == 30
    assert unittesttry.product(4) == 8

@pytest.mark.strings
def test_add_strings():
    assert unittesttry.add("Hello", " World") == "Hello World"

@pytest.mark.strings
def test_product_strings():
    assert unittesttry.product("Hello ", 3) == "Hello Hello Hello "
    assert unittesttry.product("Hello ") == "Hello Hello "

@pytest.mark.parametrize('num1, num2, result',
                            [
                                (7, 3, 10),
                                ("Hello ", "World", "Hello World"),
                                (10.5, 25.6, 36.1)
                            ]
                        )
def test_add_all(num1, num2, result):
    assert unittesttry.add(num1, num2) == result

@test
def test_Scott_data(db):
    print("performing scott test")
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_Mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'



