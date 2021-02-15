import numpy as np
import random
total_cycle = 5
no_of_days = 5
starting_ = 3
order = 8

total_limit = 11


def demand(num):
    if num >= 1 and num <= 10:
        return 0
    elif num >= 11 and num <= 35:
        return 1
    elif num >= 36 and num <= 70:
        return 2
    elif num >= 71 and num <= 91:
        return 3
    else:
        return 4


def lead_time(num):
    if num >= 1 and num <= 6:
        return 1
    elif num >= 7 and num <= 9:
        return 2
    elif num == 0:
        return 3


cycles = np.array([[[-1]*8]*no_of_days]*total_cycle)

cycles[0][0][0] = starting_
cycles[0][0][7] = 1
cycles[0][0][1] = random.randint(0, 92)
cycles[0][0][2] = demand(cycles[0][0][1])
cycles[0][0][3] = cycles[0][0][0] - cycles[0][0][2]

for i in range(total_cycle):
    for j in range(no_of_days):
        if i != 0 or j != 0:
            if i > 0 and j == 0:
                if cycles[i-1][4][7] == 0:
                    cycles[i][j][0] = order + cycles[i-1][4][3]
                elif cycles[i-1][4][7] >= 1:
                    cycles[i][j][7] = cycles[i-1][4][7] - 1
                    cycles[i][j][0] = cycles[i-1][4][3]
                else:
                    cycles[i][j][0] = cycles[i-1][4][3]
            else:
                if cycles[i][j-1][7] == 0:
                    cycles[i][j][0] = order + cycles[i][j-1][3]
                elif cycles[i][j-1][7] >= 1:
                    cycles[i][j][7] = cycles[i][j-1][7] - 1
                    cycles[i][j][0] = cycles[i][j-1][3]
                else:
                    cycles[i][j][0] = cycles[i][j-1][3]

            cycles[i][j][1] = random.randint(0, 92)
            cycles[i][j][2] = demand(cycles[i][j][1])

            if cycles[i][j][0] < cycles[i][j][2]:
                cycles[i][j][4] = cycles[i][j][2] - cycles[i][j][0]
                cycles[i][j][3] = 0
            else:
                cycles[i][j][3] = cycles[i][j][0] - cycles[i][j][2]

            if j == 4:
                cycles[i][j][5] = total_limit - cycles[i][j][3]
                order = cycles[i][j][5]
                cycles[i][j][6] = random.randint(0, 9)
                cycles[i][j][7] = lead_time(cycles[i][j][6])-1
sum = 0
count = 0
for i in range(total_cycle):
    for j in range(no_of_days):
        sum += cycles[i][j][3]
        if cycles[i][j][4] > -1:
            count += 1

print(cycles)
print(f"avg ending inventory {sum/(total_cycle*no_of_days)} days")
print(f"no. of days shortage {count}")
