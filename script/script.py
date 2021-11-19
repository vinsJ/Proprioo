import math

from data_loader import load_customers, load_properties

list_customers = load_customers()
list_proprerties = load_properties()

def compute_score(customer, property):
    """ compute score of a property based on customer's needs """
    penalties_surface = 1
    penalties_price = 1

    diff_surface = math.sqrt((customer.search.surface - property.surface)**2)
    diff_price = math.sqrt((customer.search.budget - property.price)**2)

    if(diff_surface >= 10):
        penalties_surface = diff_surface

    if(diff_price >= 10000):
        penalties_price = round(diff_price/1000)

    score = math.sqrt(((customer.search.surface - property.surface)**2)*penalties_surface + (((customer.search.budget - property.price)**2)/customer.search.budget)*penalties_price)

    return score

def sort_list_dict_score(list_dict):
    return sorted(list_dict, key=lambda d: d['score'])

def recommend():

    score_customers_properies = []

    for c in list_customers:
        list_c_score_p = []
        for p in list_proprerties:
            score = compute_score(c, p)
            list_c_score_p.append({'property': p, 'score': score})

        list_c_score_p = sort_list_dict_score(list_c_score_p)
        score_customers_properies.append(list_c_score_p)
    

recommend()

