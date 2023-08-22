from dmtoolkit.models.dndobject import DnDObject
from autonomous import log
from dmtoolkit.apis import DnDBeyondAPI
from slugify import slugify
from autonomous.storage.cloudinarystorage import CloudinaryStorage
import random


class Character(DnDObject):
    attributes = {
        # character traits
        "npc": True,
        "canon": False,
        "name": "",
        "gender": "",
        "image": {"url": "", "asset_id": 0, "raw": None},
        "ac": 0,
        "desc": "",
        "backstory": "",
        "gender": "",
        "personality": "",
        "occupation": "",
        "race": "",
        "speed": {},
        "class_name": "",
        "age": 0,
        "hp": 0,
        "wealth": [],
        "inventory": [],
        "str": 0,
        "dex": 0,
        "con": 0,
        "wis": 0,
        "int": 0,
        "cha": 0,
        "features": {},
        "spells": {},
        "resistances": [],
    }

    def get_image_prompt(self):
        style = ["Italian Renaissance", "John Singer Sargent", "James Tissot"]
        return f"A full color portrait in the style of {random.choice(style)} of a {self.race} character from Dungeons and Dragons aged {self.age} and described as {self.desc}"


class Player(Character):
    attributes = Character.attributes | {"dnd_id": None, "npc": False}

    def updateinfo(self, **kwargs):
        if not self.dnd_id:
            log("Player must have a dnd_id")
            return None
        else:
            data = DnDBeyondAPI.getcharacter(self.dnd_id)

            if results := self.table().find(dnd_id=self.dnd_id):
                self.pk = results["pk"]

            if data["image"]["url"] and data["image"]["url"] != self.image.get("url"):
                self.image = CloudinaryStorage().save(data["image"]["url"], folder=f"dnd/players/{slugify(self.name)}")

            del data["image"]

            self.__dict__.update(data)
            # log(self)
            self.save()
        return data
