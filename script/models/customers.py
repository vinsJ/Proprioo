import json

class Customer():
    """ Customer model """
    def __init__(self, id:str, lastName:str, firstName:str, phone:str, email:str, search: dict()):
        self.id = id
        self.lastName = lastName
        self.firstName = firstName
        self.phone = phone
        self.email = email
        self.search = Search(**search)
        
class Search():
    """ Search model """
    def __init__(self, surface:int, budget:int, rooms:int):
        self.surface=surface
        self.budget=budget
        self.rooms=rooms