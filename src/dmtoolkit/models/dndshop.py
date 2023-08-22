from autonomous.model.automodel import AutoModel
from autonomous import log
import random
from autonomous.apis import OpenAI
from autonomous.storage.cloudinarystorage import CloudinaryStorage


class Shop(AutoModel):
    attributes = {
        "name": "",
        "image": {"url": "", "asset_id": 0, "raw": None},
        "shoptype": "",
        "owner": None,
        "inventory": {},
        "location": "",
        "desc": "",
    }

    def generate_image(self):
        resp = OpenAI().generate_image(
            self.get_image_prompt(),
            n=1,
        )
        folder = f"dnd/{self.__class__.__name__.lower()}s"
        self.image = CloudinaryStorage().save(resp[0], folder=folder)
        self.save()

    def get_image_prompt(self):
        description = self.desc or "A simple general goods shop with wooden counters and shelves."

        return f"A full color interior image of a medieval fantasy merchant shop called {self.name} with the following description: {description}"
