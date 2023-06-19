from src.item import Item
import pytest

item1 = Item("Гаджет", 5000, 2)


def test_init():
    assert item1.price == 5000
    assert item1.name == "Гаджет"
    assert item1.quantity == 2


def test_calculate_total_price():
    assert item1.calculate_total_price() == 10000


def test_apply_discount():
    assert item1.apply_discount() == None
