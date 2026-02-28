
import pytest
from src.ollivanders import (
    Ollivanders,
    NormalItem,
    ConjuredItem,
    AgedBrie,
    Sulfuras,
    Backstage
)


# ------------------------
# NormalItem
# ------------------------

def test_normal_item_decreases_quality_before_sell_date():
    item = NormalItem("Normal", 10, 20)
    item.update_quality()
    assert item.quality == 19
    assert item.sell_in == 9


def test_normal_item_decreases_quality_twice_after_sell_date():
    item = NormalItem("Normal", -1, 20)
    item.update_quality()
    assert item.quality == 18
    assert item.sell_in == -2


def test_normal_item_quality_never_negative():
    item = NormalItem("Normal", 5, 0)
    item.update_quality()
    assert item.quality == 0


# ------------------------
# ConjuredItem
# ------------------------

def test_conjured_item_degrades_twice_as_fast():
    item = ConjuredItem("Conjured", 5, 20)
    item.update_quality()
    assert item.quality == 18


def test_conjured_item_degrades_four_after_expiry():
    item = ConjuredItem("Conjured", -1, 20)
    item.update_quality()
    assert item.quality == 16


# ------------------------
# AgedBrie
# ------------------------

def test_aged_brie_increases_quality():
    item = AgedBrie("Brie", 5, 10)
    item.update_quality()
    assert item.quality == 11


def test_aged_brie_never_exceeds_50():
    item = AgedBrie("Brie", 5, 50)
    item.update_quality()
    assert item.quality == 50


# ------------------------
# Sulfuras
# ------------------------

def test_sulfuras_never_changes():
    item = Sulfuras("Sulfuras", 0, 80)
    item.update_quality()
    assert item.quality == 80
    assert item.sell_in == 0


# ------------------------
# Backstage
# ------------------------

@pytest.mark.parametrize("sell_in, expected_quality", [
    (15, 21),  # >10
    (10, 22),  # <=10
    (5, 23),   # <=5
])
def test_backstage_quality_increase(sell_in, expected_quality):
    item = Backstage("Backstage", sell_in, 20)
    item.update_quality()
    assert item.quality == expected_quality


def test_backstage_drops_to_zero_after_concert():
    item = Backstage("Backstage", 0, 20)
    item.update_quality()
    assert item.quality == 0


# ------------------------
# Ollivanders integration
# ------------------------

def test_ollivanders_updates_all_items():
    items = [
        NormalItem("Normal", 5, 10),
        AgedBrie("Brie", 5, 10)
    ]
    shop = Ollivanders(items)
    shop.update_inventory()

    assert items[0].quality == 9
    assert items[1].quality == 11