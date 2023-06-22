from dmtoolkit.apis import open5eapi


class TestOpen5eapi:
    def test_dndmonster_build(self, monster):
        monster = open5eapi.Open5eMonster._build(monster)
        assert monster["name"] == monster["name"]
        assert monster["type"] == monster["type"]
        assert monster["size"] == monster.get("size")
        assert monster["subtype"] == monster.get("subtype")
        assert monster["alignment"] == monster.get("alignment")
        assert monster["armor_class"] == monster.get("armor_class")
        assert monster["armor_desc"] == monster.get("armor_desc")
        assert monster["hit_points"] == monster.get("hit_points")
        assert monster["hit_dice"] == monster.get("hit_dice")
        assert monster["speed"] == monster.get("speed")
        assert monster["strength"] == monster.get("strength")
        assert monster["dexterity"] == monster.get("dexterity")
        assert monster["constitution"] == monster.get("constitution")
        assert monster["intelligence"] == monster.get("intelligence")
        assert monster["wisdom"] == monster.get("wisdom")
        assert monster["charisma"] == monster.get("charisma")
        assert monster["strength_save"] == monster.get("strength_save")
        assert monster["dexterity_save"] == monster.get("dexterity_save")
        assert monster["constitution_save"] == monster.get("constitution_save")
        assert monster["intelligence_save"] == monster.get("intelligence_save")
        assert monster["wisdom_save"] == monster.get("wisdom_save")
        assert monster["charisma_save"] == monster.get("charisma_save")
        assert monster["perception"] == monster.get("perception")
        assert monster["skills"] == monster.get("skills")
        assert monster["vulnerabilities"] == monster.get("damage_vulnerabilities")
        assert monster["resistances"] == monster.get("damage_resistances")
        assert (
            monster["immunities"]
            == f"{monster['damage_immunities']}; {monster['condition_immunities']}"
        )
        assert monster["senses"] == monster.get("senses")
        assert monster["languages"] == monster.get("languages")
        assert monster["challenge_rating"] == monster.get("cr")
        assert monster["actions"] == monster.get("actions")
        assert monster["reactions"] == monster.get("reactions")
        assert monster["special_abilities"] == monster.get("special_abilities")

        monster_data = {
            "name": "Goblin",
            "type": "humanoid",
            "size": "small",
            "strength": 8,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 8,
            "charisma": 8,
        }
        monster = open5eapi.Open5eMonster._build(monster_data)

        # Check that missing fields were set to None
        assert monster["name"] == monster_data["name"]
        assert monster["type"] == monster_data["type"]

    def test_dndspell_build(self, spell):
        spell_data = spell
        spell = open5eapi.Open5eSpell._build(spell)
        assert spell["name"] == spell_data["name"]
        assert spell["school"] == spell_data["school"]
        assert spell["desc"] == spell_data["desc"]
        assert spell["variations"] == spell_data["higher_level"]

    def test_dnditem_build(self, item):
        item_data = item
        item = open5eapi.Open5eItem._build(item_data)

        assert item["name"] == item_data["name"]
        assert item["type"] == item_data["type"]
        assert item["image"] == {
            "asset_id": 0,
            "raw": None,
            "url": "https://i.imgur.com/abcdefg.png",
        }
        assert item["rarity"] == "Rare"
        assert item["cost"] == "2000 gp"
        assert item["category"] == "Martial Weapons"
        assert item["attunement"]
        assert item["damage_dice"] == "2d6"
        assert item["damage_type"] == "Slashing"
        assert item["weight"] == "6 lb."
        assert item["ac_string"] is None
        assert item["strength_requirement"] == 15
        assert item["stealth_disadvantage"]
        assert item["properties"] == ["Finesse", "Versatile (1d8)"]
        assert (
            item["desc"]
            == "This magical sword has a keen edge that seems to glide effortlessly through even the toughest armor."
        )

    def test_api_all(self):
        # Test that all() returns a list of monsters
        monsters = open5eapi.Open5eMonster.all()
        assert len(monsters) > 0
        spells = open5eapi.Open5eSpell.all()
        assert len(spells) > 0
        items = open5eapi.Open5eItem.all()
        assert len(items) > 0

    def test_api_search(self):
        # Test that all() returns a list of monsters
        monsters = open5eapi.Open5eMonster.search("goblin")
        assert len(monsters) > 0
        spells = open5eapi.Open5eSpell.search("magic missile")
        assert len(spells) > 0
        items = open5eapi.Open5eItem.search("leather")
        assert len(items) > 0

    def test_api_get(self):
        spell_url = "https://api.open5e.com/spells/magic-missile/"
        spell = open5eapi.Open5eSpell.get(spell_url)
        assert spell["name"] == "Magic Missile"
        assert spell["school"] == "Evocation"
        assert (
            spell["desc"]
            == "You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several."
        )

        assert (
            spell["variations"]
            == "When you cast this spell using a spell slot of 2nd level or higher, the spell creates one more dart for each slot level above 1st."
        )

        monster_url = "https://api.open5e.com/monsters/aboleth/"
        monster = open5eapi.Open5eMonster.get(monster_url)
        assert monster["name"] == "Aboleth"
        assert monster["size"] == "Large"
        assert monster["type"] == "aberration"
        assert monster["alignment"] == "lawful evil"
        assert monster["armor_class"] == 17
        assert monster["hit_points"] == 135
        assert monster["challenge_rating"] == 10
        assert monster["special_abilities"][0]["name"] == "Amphibious"

        item_url = "https://api.open5e.com/magicitems/glamoured-studded-leather/"
        item = open5eapi.Open5eItem.get(item_url)
        assert item["name"] == "Glamoured Studded Leather"
        assert item["type"] == "Armor (studded leather)"
        assert item["rarity"] == "rare"
