import pytest
from person import Person

@pytest.mark.parametrize(
    "name, age",
    [
        ("Alice", 30),
        ("Bob", 0),
        ("Charlie", 99),
    ]
)
def test_person_initialization(name, age):
    p = Person(name, age)
    assert p.name == name
    assert p.age == age

@pytest.mark.parametrize(
    "name, initial_age, expected_age",
    [
        ("Bob", 0, 1),
        ("Alice", 29, 30),
        ("Charlie", 99, 100),
    ]
)
def test_birthday_increments_age(name, initial_age, expected_age):
    p = Person(name, initial_age)
    p.birthday()
    assert p.age == expected_age

def test_birthday_increments_age_none():
    p = Person("Bob", 2)
    assert p.birthday() is None

def test_birthday_increments_age_erro():
    p = Person("Bob", "2")
    assert p.birthday() == 'TypeError: can only concatenate str (not "int") to str'