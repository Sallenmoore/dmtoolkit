import pytest
from models import Character, Monster, Spell, Item, Shop

from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def shop():
    return {
        "name": "test",
        "owner_id": None,
        "description": "A Test Shop",
        "inventory": [
            {
                "name": "test item A",
                "description": "this is a test item A",
                "cost": 1,
            },
            {
                "name": "test item B",
                "description": "this is a test item B",
                "cost": 2,
            },
        ],
        "location": "TEST",
    }


@pytest.fixture
def character():
    return {
        "name": "test",
        "age": 0,
        "desc": "this is a test",
        "npc": True,
        "decorations": {"avatarUrl": "test"},
        "notes": {"desc": "this is a test", "backstory": "this is a test"},
        "race": {"fullName": "test"},
        "speed": {"weightSpeeds": {"normal": {"walk": 1}}},
        "class_name": "test",
        "age": 0,
        "baseHitPoints": 0,
        "bonusHitPoints": 0,
        "removedHitPoints": 0,
        "temporaryHitPoints": 0,
        "currencies": {"test": 1},
        "stats": [
            {"id": 1, "name": None, "value": 12},
            {"id": 2, "name": None, "value": 14},
            {"id": 3, "name": None, "value": 17},
            {"id": 4, "name": None, "value": 13},
            {"id": 5, "name": None, "value": 14},
            {"id": 6, "name": None, "value": 18},
        ],
        "bonusStats": [
            {"id": 1, "name": None, "value": None},
            {"id": 2, "name": None, "value": None},
            {"id": 3, "name": None, "value": 1},
            {"id": 4, "name": None, "value": None},
            {"id": 5, "name": None, "value": None},
            {"id": 6, "name": None, "value": None},
        ],
        "inventory": [
            {
                "definition": {
                    "name": "item a",
                    "description": "item a description",
                },
                "equipped": True,
            },
            {
                "definition": {
                    "name": "item b",
                    "description": "item b description",
                    "armorTypeId": 1,
                    "armorClass": 1,
                },
                "equipped": True,
            },
        ],
        "actions": {
            "featureA": {"catA": {"name": "TestA", "snippet": "This is a smippet A"}},
            "featureB": {"catB": {"name": "TestB", "description": "This is a description B"}},
            "featureC": {
                "catC": {
                    "name": "TestC",
                    "snippet": "This is a snippet C",
                    "description": "This is a description C",
                }
            },
        },
        "options": {
            "featureA": {"definition": {"name": "TestA", "snippet": "This is a smippet A"}},
            "featureB": {
                "definition": {
                    "name": "TestB",
                    "description": "This is a description B",
                }
            },
            "featureC": {
                "definition": {
                    "name": "TestC",
                    "snippet": "This is a snippet C",
                    "description": "This is a description C",
                }
            },
        },
        "spells": {
            "spellA": {"definition": {"name": "TestA", "snippet": "This is a snippet A"}},
            "spellB": {
                "definition": {
                    "name": "TestB",
                    "description": "This is a description B",
                }
            },
            "spellC": {
                "definition": {
                    "name": "TestC",
                    "snippet": "This is a snippet C",
                    "description": "This is a description C",
                }
            },
        },
        "classSpells": {
            "spells": [
                {"definition": {"name": "TestA", "snippet": "This is a snippet A"}},
                {
                    "definition": {
                        "name": "TestB",
                        "description": "This is a description B",
                    }
                },
                {
                    "definition": {
                        "name": "TestC",
                        "snippet": "This is a snippet C",
                        "description": "This is a description C",
                    }
                },
            ]
        },
        "modifiers": {
            "testA": [
                {
                    "fixedValue": 100,
                    "type": "bonus",
                    "subType": "armor-class",
                }
            ],
            "testB": [
                {
                    "fixedValue": 99,
                    "type": "bonus",
                    "subType": "none",
                }
            ],
            "testC": [
                {
                    "fixedValue": 98,
                    "type": "none",
                    "subType": "armor-class",
                }
            ],
            "testD": [
                {
                    "type": "resistance",
                    "subType": "Is resistant to D",
                }
            ],
            "testE": [
                {
                    "type": "nothing",
                    "subType": "IS nothing",
                }
            ],
        },
    }


@pytest.fixture
def pop_db(shop, character):
    items = Character.all() + Shop.all() + Item.all() + Monster.all() + Spell.all()
    for p in items:
        p.delete()
    dndplayer = Character(**character)
    dndplayer.save()
    dndshop = Shop(**shop)
    dndshop.save()
    Monster.search(name="goblin")
    Item.search(name="resistance")
    Spell.search(name="fire")
    data = {"character": dndplayer, "shop": dndshop}
    yield data
    items = Character.all() + Shop.all() + Item.all() + Monster.all() + Spell.all()
    for p in items:
        p.delete()
