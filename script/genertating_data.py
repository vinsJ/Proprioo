# This file must be run one time.


import json

from random import randint

from models.properties import Properties


def generate_data():
    """ Method to generate data property 

    Generate data and save it into JSON file
    """

    list_properties = []

    for i in range(0, 100):

        surface = randint(70, 120)
        price = randint(450000, 800000)

        p = Properties(i, 'house', 5, surface, price, True, 0)
        list_properties.append(p.__dict__)

    with open('./data/generated-property.json', 'w', encoding='utf-8') as f:
        json.dump(list_properties, f)


generate_data()
