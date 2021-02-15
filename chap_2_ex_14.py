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


def find_data(data, rand_it):
    customers = 0
    for j in range(len(data)):
        if rand_it >= data[j][3] and data[j][4] <= rand_it:
            customers = data[j][0]
            break
    return customers


time_arrival = np.array([[5, .1, 0, 0, 0],
                         [6, .4, 0, 0, 0],
                         [7, .3, 0, 0, 0],
                         [8, .2, 0, 0, 0]])

trans_duration = np.array([[2, .15, 0, 0, 0],
                           [3, .5, 0, 0, 0],
                           [4, .2, 0, 0, 0],
                           [5, .15, 0, 0, 0]])

time_arrival = get_random(time_arrival)
trans_duration = get_random(trans_duration)

Q = 0
balking = 0
arraival, duration = 0, 0
for i in range(100):
    arraival = find_data(time_arrival, random.randint(0, 100))
    duration += find_data(trans_duration, random.randint(0, 100))
    if Q == 2:
        balking += 1
    else:
        if (arraival-duration) < 0 and Q < 2 and Q >= 0:
            Q += 1
            duration -= arraival
        else:
            Q -= 1
            duration = 0


print(balking)
