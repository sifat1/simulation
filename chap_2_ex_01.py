import numpy as np
import random

demand_table = np.array([[10, .25, 0, 0, 0],
                         [11, .35, 0, 0, 0],
                         [12, .30, 0, 0, 0],
                         [13, .10, 0, 0, 0]])

# find cumilicative probability
p_sum = 0
r_sum = 0
for i in range(len(demand_table)):
    p_sum += demand_table[i][1]
    demand_table[i][2] = p_sum
    demand_table[i][3] = r_sum
    r_sum = demand_table[i][2]*100
    demand_table[i][4] = r_sum
    r_sum += 1

days = []
days_rand_d = []
for i in range(10):
    rand_d = random.randint(0, 100)
    for j in range(len(demand_table)):
        if rand_d >= demand_table[j][3] and demand_table[j][4] <= rand_d:
            days.append(demand_table[j][0])
            days_rand_d.append(rand_d)
            break
sum_days = 0
for d in days:
    sum_days += d
print(f"Demand for next 10 days {sum_days}")
