# import random

# import pytest
# from autonomous import log

# from dmtoolkit import DMTools
# from dmtoolkit.models import Character, Item, Monster, Shop, Spell


# # @pytest.mark.skip(reason="takes too long")
# class TestDMToolkitSearch:
#     def test_DMToolkit_search_items(self, pop_db):
#         objs = DMTools.items(name="glamoured")
#         for obj in objs:
#             assert isinstance(obj, Item)
#             assert "glamoured" in obj.name.lower()

#     def test_DMToolkit_search_spells(self, pop_db):
#         objs = DMTools.spells(name="fire")
#         for obj in objs:
#             assert isinstance(obj, Spell)
#             assert "fire" in obj.name.lower()

#     def test_DMToolkit_search_monsters(self, pop_db):
#         objs = DMTools.monsters(name="goblin")
#         for obj in objs:
#             assert isinstance(obj, Monster)
#             assert "goblin" in obj.name.lower()

#     def test_DMToolkit_search_characters(self, pop_db):
#         objs = DMTools.characters(name="test")
#         for obj in objs:
#             assert isinstance(obj, Character)
#             assert "test" in obj.name

#     def test_DMToolkit_search_shops(self, pop_db):
#         objs = DMTools.shops(name="test")
#         for obj in objs:
#             assert isinstance(obj, Shop)
#             assert "test" in obj.name.lower()


# # @pytest.mark.skip(reason="takes too long")
# class TestDMToolkitGet:
#     def test_DMToolkit_get_items(self, pop_db):
#         objs = DMTools.items()
#         for obj in objs:
#             assert isinstance(obj, Item)
#             alt_obj = DMTools.items(pk=obj.pk)[0]
#             assert obj.name == alt_obj.name
#             assert obj.pk == alt_obj.pk

#     def test_DMToolkit_get_spells(self, pop_db):
#         objs = DMTools.spells()
#         for obj in objs:
#             assert isinstance(obj, Spell)
#             alt_obj = DMTools.spells(pk=obj.pk)[0]
#             assert obj.name == alt_obj.name
#             assert obj.pk == alt_obj.pk

#     def test_DMToolkit_get_monsters(self, pop_db):
#         objs = DMTools.monsters()
#         for obj in objs:
#             assert isinstance(obj, Monster)
#             alt_obj = DMTools.monsters(pk=obj.pk)[0]
#             assert obj.name == alt_obj.name
#             assert obj.pk == alt_obj.pk
#             assert obj.image == alt_obj.image

#     def test_DMToolkit_get_players(self, pop_db):
#         objs = DMTools.pcs(pk=pop_db["character"].pk)
#         for obj in objs:
#             assert isinstance(obj, Character)
#             assert "test" in obj.name

#     def test_DMToolkit_get_shops(self, pop_db):
#         objs = DMTools.shops(pk=pop_db["shop"].pk)
#         for obj in objs:
#             assert isinstance(obj, Shop)
#             assert "test" in obj.name.lower()


# # @pytest.mark.skip(reason="takes too long")
# class TestDMToolkitAll:
#     def test_DMToolkit_allitems(self, pop_db):
#         objs = DMTools.items()
#         assert len(objs) > 0

#     def test_DMToolkit_allspells(self, pop_db):
#         objs = DMTools.spells()
#         assert len(objs) > 0

#     def test_DMToolkit_allmonsters(self, pop_db):
#         objs = DMTools.monsters()
#         assert len(objs) > 0

#     def test_DMToolkit_allcharacters(self, pop_db):
#         objs = DMTools.characters()
#         assert len(objs) > 0

#     def test_DMToolkit_allshops(self, pop_db):
#         objs = DMTools.shops()
#         assert len(objs) > 0


# # @pytest.mark.skip(reason="takes too long")
# class TestDMToolkitGenerate:
#     def test_DMToolkit_randomnpc(self):
#         npc = DMTools.generatenpc()
#         assert npc.name

#     def test_DMToolkit_randomencounter(self):
#         encounter = DMTools.generateencounter()
#         assert encounter["difficulty"]

#     def test_DMToolkit_randomshop(self):
#         shop = DMTools.generateshop()
#         assert shop.name


# # @pytest.mark.skip(reason="takes too long")
# class TestDMToolkitGenerateImage:
#     def test_DMToolkit_npc_image_generate(self):
#         npc = DMTools.generatenpc()
#         npc.generate_image()
#         assert npc.image["asset_id"]
#         assert npc.image["url"]
#         assert not npc.image["raw"]

#     def test_DMToolkit_shop_image_generate(self):
#         shop = DMTools.generateshop()
#         shop.generate_image()
#         assert shop.image["asset_id"]
#         assert shop.image["url"]

#     def test_DMToolkit_item_image_generate(self, pop_db):
#         item = DMTools.items()[0]
#         item.generate_image()
#         assert item.image["asset_id"]
#         assert item.image["url"]
#         assert not item.image["raw"]

#     def test_DMToolkit_monster_image_generate(self, pop_db):
#         monster = DMTools.monsters()[0]
#         monster.generate_image()
#         assert monster.image["asset_id"]
#         assert monster.image["url"]
#         assert not monster.image["raw"]

#     def test_DMToolkit_spell_image_generate(self, pop_db):
#         spell = DMTools.spells()[0]
#         spell.generate_image()
#         assert spell.image["asset_id"]
#         assert spell.image["url"]
#         assert not spell.image["raw"]
