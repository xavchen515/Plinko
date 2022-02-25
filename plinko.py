import random
import matplotlib.pyplot as plt
import numpy as np
import pygame

# We'll be using pygame for this game/simulation!
pygame.init()
res = (720, 720)
pygame.display.set_caption("Plinko Game")
screen = pygame.display.set_mode(res)
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
ball_color = (0, 0, 0)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('quit', True, color)
ball_radius = 5
screen.fill((222, 222, 222))
bin_color = (30, 69, 142)

# Creating a dict to store all outcomes
# bin = {"left4": 0, "left3": 0, "left2": 0, "left1": 0, "mid": 0,
#        "right1": 0, "right2": 0, "right3": 0, "right4": 0}

# # Here are the odds
# multiplier = [11.5, 3.15, 1.30, 0.70, 0.35, 0.70, 1.30, 3.15, 11.5]

# num_trials = 50000

# # User will set starting amount and bet amount
# dollars = int(input("Enter your starting amount: $"))
# bet = int(input("Enter your bet amount: $"))
print(height)

# Create the plinko ball object


def draw_ball():
    pygame.draw.circle(screen, ball_color, (width/2, 50), ball_radius)

# Create the bin objects


def draw_rect():
    pygame.draw.rect(screen, bin_color, (40, height-80, 40, 70))
    pygame.draw.rect(screen, bin_color, (115, height-80, 40, 70))
    pygame.draw.rect(screen, bin_color, (190, height-80, 40, 70))
    pygame.draw.rect(screen, bin_color, (265, height-80, 40, 70))
    pygame.draw.rect(screen, bin_color, (340, height-80, 40, 70))
    pygame.draw.rect(screen, bin_color, (415, height-80, 40, 70))
    pygame.draw.rect(screen, bin_color, (490, height-80, 40, 70))
    pygame.draw.rect(screen, bin_color, (565, height-80, 40, 70))
    pygame.draw.rect(screen, bin_color, (640, height-80, 40, 70))


while True:
    for ev in pygame.event.get():
        # When user clicks the "Quit" button
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width-200 <= mouse[0] <= width-60 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()

    mouse = pygame.mouse.get_pos()

    if width-200 <= mouse[0] <= width-60 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen, color_light, [width-200, height/2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width-200, height/2, 140, 40])

    draw_ball()
    draw_rect()

    screen.blit(text, (width-150, height/2))
    pygame.display.update()

    # for i in range(num_trials):
    #     dollars -= bet
    #     decider = random.randint(0, 1)
    #     index = 4

    #     for i in range(8):
    #         random_number = random.randint(0, 1)
    #         if random_number == 0:
    #             index += 0.5
    #         elif random_number == 1:
    #             index -= 0.5

    #     if index % 1 == 0.5:
    #         if decider == 0:
    #             index += 0.5
    #         else:
    #             index -= 0.5

    #     # Falling in one of the bins will change value of bin & total
    #     if index == 0:
    #         bin["left4"] += 1
    #         dollars += bet*multiplier[0]
    #     elif index == 1:
    #         bin["left3"] += 1
    #         dollars += bet*multiplier[1]
    #     elif index == 2:
    #         bin["left2"] += 1
    #         dollars += bet*multiplier[2]
    #     elif index == 3:
    #         bin["left1"] += 1
    #         dollars += bet*multiplier[3]
    #     elif index == 4:
    #         bin["mid"] += 1
    #         dollars += bet*multiplier[4]
    #     elif index == 5:
    #         bin["right1"] += 1
    #         dollars += bet*multiplier[5]
    #     elif index == 6:
    #         bin["right2"] += 1
    #         dollars += bet*multiplier[6]
    #     elif index == 7:
    #         bin["right3"] += 1
    #         dollars += bet*multiplier[7]
    #     elif index == 8:
    #         bin["right4"] += 1
    #         dollars += bet*multiplier[8]

    # location = list(bin.keys())
    # value = list(bin.values())
    # percent_norm = []

    # # Let's calculate the odds of balls falling into each bin!
    # for i in value:
    #     percent_norm.append(i/num_trials * 100)

    # percent = [round(num, 2) for num in percent_norm]

    # # Let's also check what the house edge for the current simulation is
    # house_edge = 100

    # for i in range(len(multiplier)):
    #     house_edge -= percent[i] * multiplier[i]

    # print()
    # print("***** DISTRIBUTION *****")
    # print("Occurrences - ", value)
    # print("Percent - ", percent)
    # print()
    # print("***** BALANCE *****")
    # print(round(dollars, 2))
    # print("***** RECORDED HOUSE EDGE *****")
    # print(round(house_edge, 2), "%")


# *** TESTERS ***
# x_axis = np.array(value)

# plt.plot(x_axis)
# plt.xlabel("Bins")
# plt.ylabel("Number of Occurrences")
# plt.title("Plinko Chart")
# plt.show()
