import json

from models.customers import Customer
from models.properties import Properties


# Defining list of objects  

list_customers = []
list_properties = []

def load_customers():
    """Loading function for customers"""
    with open('./data/generated-customers.json') as f: 
        data = json.load(f)

        for item in data:
            list_customers.append(Customer(**item))

        return list_customers

def load_properties():
    """Loading function for properties"""
    with open('./data/generated-property.json') as f: 
        data = json.load(f)

        for item in data:
            list_properties.append(Properties(**item))
        
        return list_properties