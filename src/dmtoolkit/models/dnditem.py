from .dndobject import DnDObject
from autonomous import logger
import random
import markdown


class Item(DnDObject):
    attributes = {
        "name": "",
        "image": {"url": "", "asset_id": 0, "raw": None},
        "desc": "",
        "rarity": "",
        "cost": 0,
        "attunement": False,
        "duration": "",
        "damage_dice": "",
        "damage_type": "",
        "weight": 0,
        "ac_string": "",
        "strength_requirement": None,
        "properties": [],
        "tables": [],
    }

    def __init__(self, **kwargs):
        self.desc = markdown.markdown(self.desc)

    @classmethod
    def update_db(cls):
        cls._update_db(cls._api.Open5eItem)

    @classmethod
    def get_image_prompt(self):
        description = self.desc or "displayed on a table"
        style = random.choice(
            [
                "Rusted Pixel style digital art",
                "Albrecht Dürer style photorealistic colored pencil sketch",
                "William Blake style watercolor",
            ]
        )
        return f"A full color {style} of a {self.name} from Dungeons and Dragons 5e - {description}"
