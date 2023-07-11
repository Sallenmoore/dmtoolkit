import pytest
from apis import dndbeyondapi


@pytest.mark.skip(reason="Takes too long to run")
class TestDnDBeyondAPI:
    def test_player_build(self):
        for dnd_id in [77709222, 68398459, 101495221, 70279502]:
            player = dndbeyondapi.DnDBeyondAPI.getcharacter(dnd_id)

            assert player["name"] is not None
            assert player["dnd_id"] is not None
            assert player["image"] is not None
            assert player["ac"] is not None
            assert player["desc"] is not None
            assert player["race"] is not None
            assert player["speed"] is not None
            assert player["class_name"] is not None
            assert player["hp"] is not None
            assert player["age"] is not None
            assert player["wealth"] is not None
            assert player["str"] is not None
            assert player["dex"] is not None
            assert player["con"] is not None
            assert player["int"] is not None
            assert player["wis"] is not None
            assert player["cha"] is not None
            assert player["inventory"] is not None
            assert player["features"] is not None
            assert player["spells"] is not None
            assert player["resistances"] is not None

        player = dndbeyondapi.DnDBeyondAPI.getcharacter(-1)

        assert not player
