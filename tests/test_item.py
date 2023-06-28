from src.item import Item
import pytest


# item1 = Item("Гаджет", 5000, 2)


def test_init():
    item1 = Item("Гаджет", 5000, 2)
    assert item1.price == 5000
    assert item1.name == "Гаджет"
    assert item1.quantity == 2


def test_calculate_total_price():
    item1 = Item("Гаджет", 5000, 2)
    assert item1.calculate_total_price() == 10000


def test_item1_quantity():
    item1 = Item("Гаджет", 5000, 2)
    assert item1.quantity == 2


def test_apply_discount():
    item1 = Item("Гаджет", 5000, 2)
    assert item1.apply_discount() == None


def test_item_string_to_number():
    item1 = Item("Гаджет", 5000, 2)
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item1_from_csv_name():
    item1 = Item("Гаджет", 5000, 2)
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_item_instantiate_from_csv():
    item1 = Item("Гаджет", 5000, 2)
    Item.instantiate_from_csv()
    assert len(Item.all) == 10


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'
