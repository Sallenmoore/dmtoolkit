# import pytest
# import requests
# from apis import open5eapi


# # @pytest.mark.skip(reason="Takes too long to run")
# class TestOpen5eapi:
#     def test_dndmonster_build(self):
#         monsters = requests.get("https://api.open5e.com/monsters/?search=goblin").json()["results"]
#         for record in monsters:
#             mob = open5eapi.Open5eMonster._build(record)
#             assert mob["name"] == record["name"]
#             assert mob["type"] == record["type"]

#         monster_data = {
#             "name": "Goblin",
#             "strength": 8,
#             "dexterity": 14,
#             "constitution": 10,
#             "intelligence": 10,
#             "wisdom": 8,
#             "charisma": 8,
#         }
#         mob = open5eapi.Open5eMonster._build(monster_data)
#         # Check that missing fields were set to None
#         assert mob["size"] is None
#         assert mob["type"] is None

#     def test_dndspell_build(self):
#         spell_data = requests.get("https://api.open5e.com/spells/?search=fire").json()["results"]

#         for record in spell_data:
#             spell = open5eapi.Open5eSpell._build(record)
#             assert spell["name"] == record["name"]
#             assert spell["school"] == record["school"]
#             assert spell["desc"] == record["desc"]
#             assert spell["variations"] == record["higher_level"]

#     def test_dnditem_build(self):
#         item_data = requests.get("https://api.open5e.com/magicitems/?search=resistance").json()["results"]
#         item_data += requests.get("https://api.open5e.com/weapons/?search=resistance").json()["results"]
#         item_data += requests.get("https://api.open5e.com/armor/?search=resistance").json()["results"]

#         for record in item_data:
#             item = open5eapi.Open5eItem._build(record)
#             assert item["name"] == record["name"]

#     def test_monster_api_all(self):
#         # Test that all() returns a list of monsters
#         monsters = open5eapi.Open5eMonster.all()
#         assert len(monsters) > 0

#     def test_spell_api_all(self):
#         spells = open5eapi.Open5eSpell.all()
#         assert len(spells) > 0

#     def test_item_api_all(self):
#         items = open5eapi.Open5eItem.all()
#         assert len(items) > 0

#     def test_api_monster_search(self):
#         monsters = open5eapi.Open5eMonster.search("goblin")
#         assert len(monsters) > 00

#     def test_api__spell_search(self):
#         spells = open5eapi.Open5eSpell.search("magic missile")
#         assert len(spells) > 0

#     def test_api_item_search(self):
#         items = open5eapi.Open5eItem.search("leather")
#         assert len(items) > 0

#     def test_api_spell_get(self):
#         spell_url = "https://api.open5e.com/spells/magic-missile/"
#         spell = open5eapi.Open5eSpell.get(spell_url)
#         assert spell["name"] == "Magic Missile"
#         assert spell["school"] == "Evocation"
#         assert (
#             spell["desc"]
#             == "You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several."
#         )

#         assert (
#             spell["variations"]
#             == "When you cast this spell using a spell slot of 2nd level or higher, the spell creates one more dart for each slot level above 1st."
#         )

#     def test_api_monster_get(self):
#         monster_url = "https://api.open5e.com/monsters/aboleth/"
#         monster = open5eapi.Open5eMonster.get(monster_url)
#         assert monster["name"] == "Aboleth"
#         assert monster["size"] == "Large"
#         assert monster["type"] == "Aberration"
#         assert monster["alignment"] == "lawful evil"
#         assert monster["armor_class"] == 17
#         assert monster["hit_points"] == 135
#         assert monster["challenge_rating"] == 10
#         assert monster["special_abilities"][0]["name"] == "Amphibious"

#     def test_api_item_get(self):
#         item_url = "https://api.open5e.com/magicitems/glamoured-studded-leather/"
#         item = open5eapi.Open5eItem.get(item_url)
#         assert item["name"] == "Glamoured Studded Leather"
#         assert item["type"] == "Armor (studded leather)"
#         assert item["rarity"] == "rare"
