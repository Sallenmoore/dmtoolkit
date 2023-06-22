import pytest
from models.dndplayer import Player
from models.dndnpc import NPC
from models.dndshop import Shop

from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def monster():
    return {
        "name": "Goblin",
        "type": "humanoid",
        "size": "Small",
        "alignment": "neutral evil",
        "armor_class": 15,
        "hit_points": 7,
        "speed": {"walk": 30},
        "strength": 8,
        "dexterity": 14,
        "constitution": 10,
        "intelligence": 10,
        "wisdom": 8,
        "charisma": 8,
        "skills": {"stealth": 6},
        "damage_vulnerabilities": "none",
        "damage_resistances": "none",
        "damage_immunities": "none",
        "condition_immunities": "none",
        "senses": {"darkvision": 60},
        "languages": "Common, Goblin",
        "cr": 0.25,
        "actions": [
            {
                "name": "Scimitar",
                "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.",
                "attack_bonus": 4,
                "damage_dice": "1d6",
                "damage_bonus": 2,
            },
            {
                "name": "Shortbow",
                "desc": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
                "attack_bonus": 4,
                "damage_dice": "1d6",
                "damage_bonus": 2,
            },
        ],
    }


@pytest.fixture
def spell():
    return {
        "name": "Magic Missile",
        "school": "Evocation",
        "desc": [
            "You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously and you can direct them to hit one creature or several."
        ],
        "higher_level": [
            "When you cast this spell using a spell slot of 2nd level or higher, the spell creates one more dart for each slot level above 1st."
        ],
    }


@pytest.fixture
def item():
    return {
        "name": "Sword of Sharpness",
        "type": "Weapon",
        "img_main": "https://i.imgur.com/abcdefg.png",
        "rarity": "Rare",
        "cost": "2000 gp",
        "category": "Martial Weapons",
        "requires_attunement": True,
        "damage_dice": "2d6",
        "damage_type": "Slashing",
        "weight": "6 lb.",
        "ac_string": None,
        "strength_requirement": 15,
        "stealth_disadvantage": True,
        "properties": ["Finesse", "Versatile (1d8)"],
        "desc": "This magical sword has a keen edge that seems to glide effortlessly through even the toughest armor.",
    }


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
def player():
    return {
        "name": "test",
        "age": 0,
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
            "featureB": {
                "catB": {"name": "TestB", "description": "This is a description B"}
            },
            "featureC": {
                "catC": {
                    "name": "TestC",
                    "snippet": "This is a snippet C",
                    "description": "This is a description C",
                }
            },
        },
        "options": {
            "featureA": {
                "definition": {"name": "TestA", "snippet": "This is a smippet A"}
            },
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
            "spellA": {
                "definition": {"name": "TestA", "snippet": "This is a snippet A"}
            },
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
def npc():
    return {
        "name": "test",
        "backstory": "This is a test",
        "race": "test",
        "class_name": "test",
        "age": 1,
        "hp": 1,
        "desc": "This is a test",
        "inventory": [
            {
                "name": "item a",
                "description": "item a description",
            },
            {
                "name": "item b",
                "description": "item b description",
            },
        ],
        "strength": 1,
        "dexterity": 2,
        "constitution": 3,
        "wisdom": 4,
        "intelligence": 5,
        "charisma": 6,
    }


@pytest.fixture
def pop_db(shop, player, npc):
    dndplayer = Player(**player)
    dndplayer.save()
    dndshop = Shop(**shop)
    dndshop.save()
    dndnpc = NPC(npc)
    dndnpc.save()
    data = {"player": dndplayer, "shop": dndshop, "npc": dndnpc}
    yield data
    for p in Player.all():
        if p.name == player["name"]:
            p.delete()

    for p in NPC.all():
        if p.name == npc["name"]:
            p.delete()

    for p in Shop.all():
        if p.name == shop["name"]:
            p.delete()
