import pytest
from models.dndmonster import Monster
from models.dndspell import Spell
from models.dnditem import Item


@pytest.mark.skip(reason="takes too long")
class TestDB:
    # @pytest.mark.skip(reason="takes too long")
    def test_monster(self):
        print("Updating Monster DB...")
        Monster.update_db()

    # @pytest.mark.skip(reason="takes too long")
    def test_spell(self):
        print("Updating Spell DB...")
        Spell.update_db()

    # @pytest.mark.skip(reason="takes too long")
    def test_item(self):
        print("Updating Item DB...")
        Item.update_db()
