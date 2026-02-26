
import pytest
from ollivanders import (
    NormalItem,
    ConjuredItem,
    AgedBrie,
    Sulfuras,
    Backstage
)

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

