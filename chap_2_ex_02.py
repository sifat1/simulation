import numpy as np
import random


def get_random(d_data):
    p_sum = 0
    r_sum = 0
    for i in range(len(d_data)):
        p_sum += d_data[i][1]
        d_data[i][2] = p_sum
        d_data[i][3] = r_sum
        r_sum = d_data[i][2]*100
        d_data[i][4] = r_sum
        r_sum += 1
    return d_data


no_customers_perday = np.array([[8, .35, 0, 0, 0],
                                [10, .30, 0, 0, 0],
                                [12, .25, 0, 0, 0],
                                [14, .10, 0, 0, 0]])

no_dozen_percustomers = np.array([[1, .4, 0, 0, 0],
                                  [2, .3, 0, 0, 0],
                                  [3, .2, 0, 0, 0],
                                  [4, .1, 0, 0, 0]])

no_customers_perday = get_random(no_customers_perday)
no_dozen_percustomers = get_random(no_dozen_percustomers)
dozen = 0


def find_data(data, rand_it):
    customers = 0
    for j in range(len(data)):
        if rand_it >= data[j][3] and data[j][4] <= rand_it:
            customers = data[j][0]
            break
    return customers


for i in range(5):
    rand_it = random.randint(0, 100)
    customers = find_data(no_customers_perday, rand_it)

    for k in range(int(customers)):
        dozen += find_data(no_dozen_percustomers, rand_it)

print(dozen/5)
