import random

from autonomous import log

from dmtoolkit.models import Region
from dmtoolkit.models.ttrpgobject import TTRPGObject


class World(TTRPGObject):
    genres = ["fantasy", "sci-fi", "hardboiled", "horror", "post-apocalyptic"]

    attributes = TTRPGObject.attributes | {
        "regions": [],
        "system": None,
        "genre": "",
        "user": None,
        "doc_apis": [],
    }

    @property
    def history(self):
        return self.backstory

    @history.setter
    def history(self, value):
        self.backstory = value

    def get_image_prompt(self):
        description = f"A full color, high resolution illustrated map a fictional {self.genre} world called {self.name} and described as {self.desc or 'filled with points of interest to explore, antagonistic factions, and a rich, mysterious history.'}"
        return description

    def generate(self, region=1, location=1, city=1, faction=1):
        for _ in range(region):
            self.add_region(location, city, faction)

    def add_region(self, l_num=3, c_num=2, f_num=2):
        region = Region.generate(world=self, description=self.desc)
        self.regions.append(region)
        factions = region.create_factions(f_num)
        (f.add_member(leader=True) for f in factions)
        locations = region.create_locations(l_num)
        (f.add_inhabitant(owner=True) for f in locations)
        cities = region.create_cities(c_num)
        (f.add_locations(owner=True) for f in cities)
        region.cities = self.add_cities(cities)
        self.save()
        return region

    def config(self):
        self.config = {
            "name": self.name,
            "genre": self.genre,
            "system": self.system.name,
            "backstory": self.backstory,
            "regions": [r.name for r in self.regions.serialize()],
        }
        return self.config

    def canonize(self):
        for doc in self.doc_apis:
            doc.canonize(self.config())
