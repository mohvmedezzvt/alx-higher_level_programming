#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weighted_score, total_weights_only = 0, 0
    for score, weight in my_list:
        total_weighted_score += score * weight
        total_weights_only += weight

    weighted_average = total_weighted_score / total_weights_only
    return weighted_average
