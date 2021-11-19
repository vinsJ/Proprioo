import json

class Properties():
    """ Properties model """
    def __init__(self, id:str, type:str, rooms:int, surface:int, price:int, cave:bool, 
    garden:int):
        self.id = id
        self.type = type
        self.rooms = rooms
        self.surface = surface
        self.price = price
        self.cave = cave
        self.garden = garden

    def toJSON(self):
        return json.dump(self, default=lambda o: o.__dict__)