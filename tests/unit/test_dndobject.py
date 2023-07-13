import random
import pytest

from models import Character, Shop, Monster, Item, Spell


# @pytest.mark.skip(reason="takes too long")
class TestDnDObject:
    # @pytest.mark.skip(reason="takes too long")
    def test_dndobject_all(self, pop_db):
        objs = Item.all()
        for obj in objs:
            assert isinstance(obj, Item)
            assert obj.name is not None

        objs = Spell.all()
        for obj in objs:
            assert isinstance(obj, Spell)
            assert obj.name is not None

        objs = Monster.all()
        for obj in objs:
            assert isinstance(obj, Monster)
            assert obj.name is not None

    # @pytest.mark.skip(reason="costs money")
    def test_dnditemobject_get(self, pop_db):
        obj = random.choice(Item.all())
        obj.generate_image()
        assert obj.image["url"]
        assert obj.image["asset_id"]
        assert obj.image["raw"] is None
        result = Item.get(obj.pk)
        assert isinstance(obj, Item)
        assert result.name is not None

    # @pytest.mark.skip(reason="costs money")
    def test_dndspellobject_get(self, pop_db):
        obj = random.choice(Spell.all())
        obj.generate_image()
        assert obj.image["url"]
        assert obj.image["asset_id"]
        assert obj.image["raw"] is None
        result = Spell.get(obj.pk)
        assert isinstance(obj, Spell)
        assert result.name is not None

    # @pytest.mark.skip(reason="costs money")
    def test_dndmonsterobject_get(self, pop_db):
        obj = random.choice(Monster.all())
        obj.generate_image()
        assert obj.image["url"]
        assert obj.image["asset_id"]
        assert obj.image["raw"] is None
        result = Monster.get(obj.pk)
        assert isinstance(obj, Monster)
        assert result.name is not None

    # @pytest.mark.skip(reason="takes too long")
    def test_dnditemobject_search(self, pop_db):
        objs = Item.search(name="resistance")
        for obj in objs:
            assert isinstance(obj, Item)
            assert "resistance" in obj.name.lower()

    # @pytest.mark.skip(reason="takes too long")
    def test_dndspellobject_search(self, pop_db):
        objs = Spell.search(name="fire")
        for obj in objs:
            assert isinstance(obj, Spell)
            assert "fire" in obj.name.lower()

    # @pytest.mark.skip(reason="takes too long")
    def test_dndmonsterobject_search(self, pop_db):
        objs = Monster.search(name="goblin")
        for obj in objs:
            assert isinstance(obj, Monster)
            assert "goblin" in obj.name.lower()

    # @pytest.mark.skip(reason="takes too long")
    def test_dndplayer(self):
        player = Character(dnd_id="77709222")
        player.updateinfo()
        player.save()

        assert player.dnd_id == "77709222"
        assert player.name
        assert player.image
        assert player.ac
        assert player.desc
        assert player.race
        assert player.speed
        assert player.class_name
        assert player.hp
        assert player.age
        assert player.wealth
        assert player.str
        assert player.dex
        assert player.con
        assert player.int
        assert player.wis
        assert player.cha
        assert player.inventory
        assert player.features
        assert player.spells
        assert player.resistances

        player = Character.find(dnd_id="-1")
        assert not player

    # @pytest.mark.skip(reason="costs money")
    def test_dndnpc(self, pop_db):
        npc = pop_db["character"]
        for npc in Character.all():
            if npc.name == "test":
                npc.generate_image()
                assert npc.image["url"]
                assert npc.image["asset_id"]
                assert npc.image["raw"] is None
                assert npc.inventory[0]["definition"]["name"] == "item a"

    # @pytest.mark.skip(reason="costs money")
    def test_dndshop(self, pop_db):
        shop = pop_db["shop"]
        for shop in Shop.all():
            if shop.name == "test":
                shop.generate_image()
                assert shop.image["url"]
                assert shop.image["asset_id"]
                assert shop.image["raw"] is None
                assert shop.location == "TEST"
                assert len(shop.inventory) == 2
                assert shop.inventory[0]["name"] == "test item A"
