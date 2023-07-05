from autonomous.model.automodel import AutoModel
from autonomous import log
from apis import DnDBeyondAPI
from slugify import slugify
from autonomous.storage.cloudinarystorage import CloudinaryStorage


class Character(AutoModel):
    attributes = {
        "dnd_id": None,
        "npc": True,
        # character traits
        "name": "",
        "gender": "",
        "image": {"url": "", "asset_id": 0, "raw": None},
        "ac": 0,
        "description": "",
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

    def updateinfo(self, **kwargs):
        if not self.dnd_id:
            log("Player must have a dnd_id")
            return None
        else:
            data = DnDBeyondAPI.getcharacter(self.dnd_id)

            if results := self.table().find(dnd_id=self.dnd_id):
                self.pk = results["pk"]

            if data["image"]["url"] and data["image"]["url"] != self.image.get("url"):
                self.image = CloudinaryStorage().save(
                    data["image"]["url"], folder=f"dnd/players/{slugify(self.name)}"
                )
            del data["image"]

            self.__dict__.update(data)
            # log(self)
            self.save()
        return data
