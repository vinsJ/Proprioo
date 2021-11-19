import math
import json

from data_loader import load_customers, load_properties

list_customers = load_customers()
list_proprerties = load_properties()


def compute_score(customer, property):
    """ compute score of a property based on customer's needs 

    :return: score of a property for a given customer (float) """
    penalties_surface = 1
    penalties_price = 1

    diff_surface = math.sqrt((customer.search.surface - property.surface)**2)
    diff_price = math.sqrt((customer.search.budget - property.price)**2)

    # add penalties in case the difference is too high

    if(diff_surface >= 10):
        penalties_surface = diff_surface

    if(diff_price >= 10000):
        penalties_price = round(diff_price/1000)

    score = math.sqrt(((customer.search.surface - property.surface)**2)*penalties_surface
                      + (((customer.search.budget - property.price)**2)/customer.search.budget)*penalties_price)

    return score


def sort_list_dict_score(list_dict):
    """ sort list of dictionnary based on the attribute 'score' 

    :return: sorted list by score (ascending)
    """
    return sorted(list_dict, key=lambda d: d['score'])


def recommend():
    """ Function that gives the top 5 properties for a given customer

    :return: list of dictionnary """

    score_customers_properies = []

    for c in list_customers:
        list_c_score_p = []
        for p in list_proprerties:
            score = compute_score(c, p)
            list_c_score_p.append({'property': p.__dict__, 'score': score})

        list_c_score_p = sort_list_dict_score(list_c_score_p)
        score_customers_properies.append(
            {'customer': c.id, 'needs': c.search.__dict__,
             'recommendations': list_c_score_p[:5]})

    return score_customers_properies


def save_results(list_results):
    """ save the result in JSON file located in data folder """
    with open('./data/results.json', 'w', encoding='utf-8') as f:
        json.dump(list_results, f)


save_results(recommend())
