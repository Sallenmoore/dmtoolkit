import pytest
from models.dndmonster import Monster
from models.dndspell import Spell
from models.dnditem import Item


@pytest.mark.skip(reason="takes too long")
def test_monster():
    print("Updating Monster DB...")
    Monster.update_db()


@pytest.mark.skip(reason="takes too long")
def test_spell():
    print("Updating Spell DB...")
    Spell.update_db()


@pytest.mark.skip(reason="takes too long")
def test_item():
    print("Updating Item DB...")
    Item.update_db()
