from src.phone import Phone
from src.item import Item

import pytest


def test_init():
    phone1 = Phone("iphone", 5000, 2, 1)
    assert str(phone1) == 'iphone'
    assert repr(phone1) == "Phone('iphone', 5000, 2, 1)"
    assert phone1.number_of_sim == 1

def test_add_items():
    phone1 = Phone("iphone", 5000, 4, 3)
    item1 = Item("iphone", 5000, 5)
    assert phone1 + phone1 == 8
    assert phone1 + item1 == 9




