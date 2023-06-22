import pytest
import json
from apis import OpenAI
from autonomous import log


# @pytest.mark.skip(reason="costs money")
class TestOpenAI:
    def test_init(self):
        oai = OpenAI()
        assert oai

    def test_generate_image(self):
        oai = OpenAI()
        prompt = "The prettiest girl in the world named Natasha"
        img = oai.generate_image(prompt, size="256x256", n=1)
        assert isinstance(img, bytes)
        test_file = "tests/assets/testimg.png"
        test_file.write(img)

    def test_generate_text(self):
        primer = """
        You are a random NPC generator
        """
        prompt = "Generate an NPC with a physical description, a backstory that contains an unexpected twist, and a desperate secret."
        funcobj = {
            "name": "generate_npc",
            "description": "Generate an NPC",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The character's name",
                    },
                    "gender": {
                        "type": "string",
                        "description": "The character's gender",
                    },
                    "backstory": {
                        "type": "string",
                        "description": "The character's backstory",
                    },
                    "str": {
                        "type": "integer",
                        "description": "The amount of Strength the character has from 1-20",
                    },
                    "dex": {
                        "type": "integer",
                        "description": "The amount of Dexterity the character has from 1-20",
                    },
                    "con": {
                        "type": "integer",
                        "description": "The amount of Constitution the character has from 1-20",
                    },
                    "int": {
                        "type": "integer",
                        "description": "The amount of Intelligence the character has from 1-20",
                    },
                    "wis": {
                        "type": "integer",
                        "description": "The amount of Wisdom the character has from 1-20",
                    },
                    "cha": {
                        "type": "integer",
                        "description": "The amount of Charisma the character has from 1-20",
                    },
                },
            },
        }
        funcobj["parameters"]["required"] = (
            list(funcobj["parameters"]["properties"].keys()),
        )
        response = OpenAI().generate_text(prompt, primer, functions=[funcobj])
        npc_data = json.loads(response)
        log(npc_data)
        assert npc_data["name"] is not None
        assert npc_data["gender"] is not None
        assert npc_data["backstory"] is not None
        assert npc_data["str"] is not None
        assert npc_data["dex"] is not None
        assert npc_data["con"] is not None
        assert npc_data["int"] is not None
        assert npc_data["wis"] is not None
        assert npc_data["cha"] is not None
        assert npc_data["str"] >= 1
        assert npc_data["str"] <= 20
