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


time_arrival = np.array([[5, .20, 0, 0, 0],
                         [6, .70, 0, 0, 0],
                         [7, .10, 0, 0, 0]])

call_duration = np.array([[2, .15, 0, 0, 0],
                          [3, .6, 0, 0, 0],
                          [4, .15, 0, 0, 0],
                          [5, .1, 0, 0, 0]])

time_arrival = get_random(time_arrival)
call_duration = get_random(call_duration)

wait = 0
arraival, duration = 0, 0
for i in range(100):
    arraival = find_data(time_arrival, random.randint(0, 100))
    duration = find_data(call_duration, random.randint(0, 100))

    if arraival-duration < 0:
        wait += duration - arraival
        duration -= arraival
    else:
        duration = 0
print(f"AVG waiting time is {wait/100}")
