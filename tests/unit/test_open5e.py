import pytest
import requests
from apis.open5e.open5eitem import Open5eItem
from apis.open5e.open5emonster import Open5eMonster
from apis.open5e.open5espell import Open5eSpell


class TestOpen5eapi:
    def test_dndmonster_api(self):
        mob = requests.get("https://www.dnd5eapi.co/api/monsters/goblin").json()
        assert mob["name"] == "Goblin"
        assert mob["type"] == "humanoid"

    def test_dndspell_api(self):
        spell_data = requests.get(
            "https://www.dnd5eapi.co/api/spells/animal-friendship"
        ).json()

        assert spell_data["name"] == "Animal Friendship"

    def test_dnditem_api(self):
        item_data = requests.get(
            "https://www.dnd5eapi.co/api/magic-items/ammunition-3"
        ).json()

        assert "Ammunition, +3" == item_data["name"]

    # def test_monster_api_all(self):
    #     # Test that all() returns a list of monsters
    #     monsters = Open5eMonster.all()
    #     assert len(monsters) > 0

    # def test_spell_api_all(self):
    #     spells = Open5eSpell.all()
    #     assert len(spells) > 0

    # def test_item_api_all(self):
    #     items = Open5eItem.all()
    #     assert len(items) > 0

    def test_api_monster_search(self):
        monsters = Open5eMonster.search("goblin")
        assert len(monsters) > 0

    def test_api_spell_search(self):
        spells = Open5eSpell.search("magic missile")
        assert len(spells) > 0

    def test_api_item_search(self):
        items = Open5eItem.search("leather")
        assert len(items) > 0
