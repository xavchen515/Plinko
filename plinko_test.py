import random
import matplotlib.pyplot as plt
import numpy as np


bin = {"left4": 0, "left3": 0, "left2": 0, "left1": 0, "mid": 0,
       "right1": 0, "right2": 0, "right3": 0, "right4": 0}

multiplier = [11.5, 3.15, 1.30, 0.70, 0.35, 0.70, 1.30, 3.15, 11.5]

num_trials = 50000
dollars = int(input("Enter your starting amount: $"))
bet = int(input("Enter your bet amount: $"))

for i in range(num_trials):
    dollars -= bet
    decider = random.randint(0, 1)
    index = 4

    for i in range(8):
        random_number = random.randint(0, 1)
        if random_number == 0:
            index += 0.5
        elif random_number == 1:
            index -= 0.5

    if index % 1 == 0.5:
        if decider == 0:
            index += 0.5
        else:
            index -= 0.5

    if index == 0:
        bin["left4"] += 1
        dollars += bet*multiplier[0]
    elif index == 1:
        bin["left3"] += 1
        dollars += bet*multiplier[1]
    elif index == 2:
        bin["left2"] += 1
        dollars += bet*multiplier[2]
    elif index == 3:
        bin["left1"] += 1
        dollars += bet*multiplier[3]
    elif index == 4:
        bin["mid"] += 1
        dollars += bet*multiplier[4]
    elif index == 5:
        bin["right1"] += 1
        dollars += bet*multiplier[5]
    elif index == 6:
        bin["right2"] += 1
        dollars += bet*multiplier[6]
    elif index == 7:
        bin["right3"] += 1
        dollars += bet*multiplier[7]
    elif index == 8:
        bin["right4"] += 1
        dollars += bet*multiplier[8]

location = list(bin.keys())
value = list(bin.values())
percent_norm = []

for i in value:
    percent_norm.append(i/num_trials * 100)

percent = [round(num, 2) for num in percent_norm]
house_edge = 100

for i in range(len(multiplier)):
    house_edge -= percent[i] * multiplier[i]

print()
print("***** DISTRIBUTION *****")
print("Occurrences - ", value)
print("Percent - ", percent)
print()
print("***** BALANCE *****")
print(round(dollars, 2))
print("***** RECORDED HOUSE EDGE *****")
print(round(house_edge, 2), "%")

x_axis = np.array(value)

plt.plot(x_axis)
plt.xlabel("Bins")
plt.ylabel("Number of Occurrences")
plt.title("Plinko Chart")
plt.show()
