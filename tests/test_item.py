from src.item import Item
import pytest

item1 = Item("Гаджет", 5000, 2)


def test_init():
    assert item1.price == 5000
    assert item1.name == "Гаджет"
    assert item1.quantity == 2


def test_calculate_total_price():
    assert item1.calculate_total_price() == 10000


def test_item1_quantity():
    assert item1.quantity == 2


def test_apply_discount():
    assert item1.apply_discount() == None


def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item1_from_csv_name():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
