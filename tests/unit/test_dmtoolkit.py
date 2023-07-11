import pytest
import random

from autonomous import log

from dmtoolkit import DMToolkit
from models import Character, Shop, Monster, Item, Spell


@pytest.mark.skip(reason="takes too long")
class TestDMToolkit:
    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_search_items(self, pop_db):
        objs = DMToolkit.items(name="glamoured")
        for obj in objs:
            assert isinstance(obj, Item)
            assert "glamoured" in obj.name.lower()

    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_search_spells(self, pop_db):
        objs = DMToolkit.spells(name="fire")
        for obj in objs:
            assert isinstance(obj, Spell)
            assert "fire" in obj.name.lower()

    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_search_monsters(self, pop_db):
        objs = DMToolkit.monsters(name="goblin")
        for obj in objs:
            assert isinstance(obj, Monster)
            assert "goblin" in obj.name.lower()

    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_search_characters(self, pop_db):
        objs = DMToolkit.characters(name="test")
        for obj in objs:
            assert isinstance(obj, Character)
            assert "test" in obj.name

    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_search_shops(self, pop_db):
        objs = DMToolkit.shops(name="test")
        for obj in objs:
            assert isinstance(obj, Shop)
            assert "test" in obj.name.lower()

    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_get_items(self, pop_db):
        objs = DMToolkit.items()
        objs = random.sample(objs, 5)
        for obj in objs:
            assert isinstance(obj, Item)
            alt_obj = DMToolkit.items(pk=obj.pk)[0]
            assert obj.name == alt_obj.name
            assert obj.pk == alt_obj.pk

    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_get_spells(self, pop_db):
        objs = DMToolkit.spells()
        objs = random.sample(objs, 5)
        for obj in objs:
            assert isinstance(obj, Spell)
            alt_obj = DMToolkit.spells(pk=obj.pk)[0]
            assert obj.name == alt_obj.name
            assert obj.pk == alt_obj.pk

    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_get_monsters(self, pop_db):
        objs = DMToolkit.monsters()
        objs = random.sample(objs, 5)
        for obj in objs:
            assert isinstance(obj, Monster)
            alt_obj = DMToolkit.monsters(pk=obj.pk)[0]
            assert obj.name == alt_obj.name
            assert obj.pk == alt_obj.pk
            assert obj.image == alt_obj.image

    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_get_players(self, pop_db):
        objs = DMToolkit.pcs(pk=pop_db["character"].pk)
        for obj in objs:
            assert isinstance(obj, Character)
            assert "test" in obj.name

    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_get_shops(self, pop_db):
        objs = DMToolkit.shops(pk=pop_db["shop"].pk)
        for obj in objs:
            assert isinstance(obj, Shop)
            assert "test" in obj.name.lower()

    @pytest.mark.skip(reason="takes too long")
    def test_DMToolkit_all(self, pop_db):
        objs = DMToolkit.items()
        assert len(objs) > 0

        objs = DMToolkit.spells()
        assert len(objs) > 0

        objs = DMToolkit.monsters()
        assert len(objs) > 0

        objs = DMToolkit.characters()
        assert len(objs) > 0

        objs = DMToolkit.shops()
        assert len(objs) > 0

    @pytest.mark.skip(reason="costs money")
    def test_DMToolkit_randomnpc(self):
        npc = DMToolkit.generatenpc()
        assert npc.name

    @pytest.mark.skip(reason="costs money")
    def test_DMToolkit_randomencounter(self):
        encounter = DMToolkit.generateencounter()
        assert encounter["difficulty"]

    @pytest.mark.skip(reason="costs money")
    def test_DMToolkit_randomshop(self):
        shop = DMToolkit.generateshop()
        assert shop.name

    @pytest.mark.skip(reason="costs money")
    def test_DMToolkit_npc_image_generate(self):
        npc = DMToolkit.generatenpc()
        npc.generate_image()
        assert npc.image["asset_id"]
        assert npc.image["url"]
        assert not npc.image["raw"]

    @pytest.mark.skip(reason="costs money")
    def test_DMToolkit_shop_image_generate(self):
        shop = DMToolkit.generateshop()
        shop.generate_image()
        assert shop.image["asset_id"]
        assert shop.image["url"]

    @pytest.mark.skip(reason="costs money")
    def test_DMToolkit_item_image_generate(self):
        # Item.update_db()
        item = DMToolkit.items()[0]
        item.generate_image()
        assert item.image["asset_id"]
        assert item.image["url"]
        assert not item.image["raw"]

    @pytest.mark.skip(reason="costs money")
    def test_DMToolkit_monster_image_generate(self):
        # Monster.update_db()
        monster = DMToolkit.monsters()[0]
        monster.generate_image()
        assert monster.image["asset_id"]
        assert monster.image["url"]
        assert not monster.image["raw"]

    @pytest.mark.skip(reason="costs money")
    def test_DMToolkit_spell_image_generate(self):
        Spell.update_db()
        spell = DMToolkit.spells()[0]
        spell.generate_image()
        assert spell.image["asset_id"]
        assert spell.image["url"]
        assert not spell.image["raw"]
