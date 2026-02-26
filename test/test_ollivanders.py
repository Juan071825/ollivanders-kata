
import pytest
from ollivanders import (
    Ollivanders,
    NormalItem,
    ConjuredItem,
    AgedBrie,
    Sulfuras,
    Backstage
)

# -----------------------
# OLLIVANDERS
# -----------------------

def test_inventory_initializes_empty_when_no_items():
    inventory = Ollivanders()
    assert inventory.get_inventory() == []


def test_inventory_initializes_with_items():
    item = NormalItem("Normal", 10, 20)
    inventory = Ollivanders([item])
    assert len(inventory.get_inventory()) == 1


def test_add_item_adds_to_inventory():
    inventory = Ollivanders()
    item = NormalItem("Normal", 10, 20)

    inventory.add_item(item)

    assert len(inventory.get_inventory()) == 1
    assert inventory.get_inventory()[0] == item


def test_add_item_raises_error_if_not_item():
    inventory = Ollivanders()

    with pytest.raises(TypeError):
        inventory.add_item("Not an item")


def test_update_inventory_updates_all_items():
    item1 = NormalItem("Normal", 10, 20)
    item2 = AgedBrie("Aged Brie", 5, 30)

    inventory = Ollivanders([item1, item2])

    inventory.update_inventory()

    assert item1.sell_in == 9
    assert item1.quality == 19

    assert item2.sell_in == 4
    assert item2.quality == 31


def test_update_inventory_empty_does_not_fail():
    inventory = Ollivanders()
    inventory.update_inventory()
    assert inventory.get_inventory() == []

# -----------------------
# NORMAL ITEM
# -----------------------

def test_normal_item_decreases_quality_before_sell_date():
    item = NormalItem("Normal", 10, 20)
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 19


def test_normal_item_degrades_twice_as_fast_after_sell_date():
    item = NormalItem("Normal", 0, 20)
    item.update_quality()
    assert item.sell_in == -1
    assert item.quality == 18


def test_normal_item_quality_never_negative():
    item = NormalItem("Normal", 5, 0)
    item.update_quality()
    assert item.quality == 0


# -----------------------
# CONJURED ITEM
# -----------------------

def test_conjured_item_degrades_twice_as_fast():
    item = ConjuredItem("Conjured", 10, 20)
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 18


def test_conjured_item_degrades_four_after_sell_date():
    item = ConjuredItem("Conjured", 0, 20)
    item.update_quality()
    assert item.sell_in == -1
    assert item.quality == 16


# -----------------------
# AGED BRIE
# -----------------------

def test_aged_brie_increases_quality():
    item = AgedBrie("Aged Brie", 10, 20)
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 21


def test_aged_brie_increases_twice_after_sell_date():
    item = AgedBrie("Aged Brie", 0, 20)
    item.update_quality()
    assert item.sell_in == -1
    assert item.quality == 22


def test_aged_brie_never_exceeds_50():
    item = AgedBrie("Aged Brie", 5, 50)
    item.update_quality()
    assert item.quality == 50


# -----------------------
# SULFURAS
# -----------------------

def test_sulfuras_never_changes():
    item = Sulfuras("Sulfuras", 5, 80)
    item.update_quality()
    assert item.sell_in == 5
    assert item.quality == 80


# -----------------------
# BACKSTAGE
# -----------------------

def test_backstage_increase_by_1_when_more_than_10_days():
    item = Backstage("Backstage", 15, 20)
    item.update_quality()
    assert item.quality == 21


def test_backstage_increase_by_2_when_10_days_or_less():
    item = Backstage("Backstage", 10, 20)
    item.update_quality()
    assert item.quality == 22


def test_backstage_increase_by_3_when_5_days_or_less():
    item = Backstage("Backstage", 5, 20)
    item.update_quality()
    assert item.quality == 23


def test_backstage_drops_to_zero_after_concert():
    item = Backstage("Backstage", 0, 20)
    item.update_quality()
    assert item.quality == 0


def test_backstage_never_exceeds_50():
    item = Backstage("Backstage", 5, 49)
    item.update_quality()
    assert item.quality == 50

