from src.phone import Phone
import pytest


def test_init():
    phone1 = Phone("iphone", 5000, 2, 1)
    assert str(phone1) == 'iphone'
    assert repr(phone1) == "Phone('iphone', 5000, 2, 1)"
    assert phone1.number_of_sim == 1

