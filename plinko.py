import random
import matplotlib.pyplot as plt
import numpy as np
import pygame

# We'll be using pygame for this game/simulation!
pygame.init()

# Setting the screen size (Don't change)
res = (720, 720)
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()

# Set background colour
screen.fill((222, 222, 222))

# Set caption
pygame.display.set_caption("Plinko Game")

# Create colour shortcuts
white = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
black = (0, 0, 0)
red = (255, 0, 0)
red2 = (255, 60, 0)
orange = (255, 120, 0)
orange2 = (255, 180, 0)
yellow = (255, 240, 0)

quit_font = pygame.font.SysFont('Corbel', 35)
quit_text = quit_font.render('quit', True, white)
bin_font = pygame.font.SysFont('Ariel', 25)


# Plinko ball
ball_radius = 8
ball_x = width/2
ball_y = 50


# Creating a dict to store all outcomes
# bin = {"left4": 0, "left3": 0, "left2": 0, "left1": 0, "mid": 0,
#        "right1": 0, "right2": 0, "right3": 0, "right4": 0}

# # Here are the odds
# multiplier = [11.5, 3.15, 1.30, 0.70, 0.35, 0.70, 1.30, 3.15, 11.5]

# num_trials = 50000

# # User will set starting amount and bet amount
# dollars = int(input("Enter your starting amount: $"))
# bet = int(input("Enter your bet amount: $"))


# Create the plinko ball object
def draw_ball():
    pygame.draw.circle(screen, black, (ball_x, ball_y), ball_radius)


# Create the bin objects
def draw_rect():
    pygame.draw.rect(screen, red, (25, height-60, 70, 40))
    pygame.draw.rect(screen, red2, (100, height-60, 70, 40))
    pygame.draw.rect(screen, orange, (175, height-60, 70, 40))
    pygame.draw.rect(screen, orange2, (250, height-60, 70, 40))
    pygame.draw.rect(screen, yellow, (325, height-60, 70, 40))
    pygame.draw.rect(screen, orange2, (400, height-60, 70, 40))
    pygame.draw.rect(screen, orange, (475, height-60, 70, 40))
    pygame.draw.rect(screen, red2, (550, height-60, 70, 40))
    pygame.draw.rect(screen, red, (625, height-60, 70, 40))


def bin_text():
    bin_text = bin_font.render('11.5x', True, black)
    screen.blit(bin_text, (35, height-45))
    screen.blit(bin_text, (635, height-45))
    bin_text = bin_font.render('3.15x', True, black)
    screen.blit(bin_text, (110, height-45))
    screen.blit(bin_text, (560, height-45))
    bin_text = bin_font.render('1.30x', True, black)
    screen.blit(bin_text, (185, height-45))
    screen.blit(bin_text, (485, height-45))
    bin_text = bin_font.render('0.70x', True, black)
    screen.blit(bin_text, (260, height-45))
    screen.blit(bin_text, (410, height-45))
    bin_text = bin_font.render('0.35x', True, black)
    screen.blit(bin_text, (335, height-45))


clock = pygame.time.Clock()

while True:

    screen.fill((222, 222, 222))

    for ev in pygame.event.get():
        # When user clicks the "Quit" button
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width-155 <= mouse[0] <= width-15 and 15 <= mouse[1] <= 55:
                pygame.quit()
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_SPACE:
                pygame.draw.circle(screen, black, (ball_x, 50), ball_radius)

    draw_ball()
    ball_y += 0.06

    mouse = pygame.mouse.get_pos()

    if width-155 <= mouse[0] <= width-15 and 15 <= mouse[1] <= 55:
        pygame.draw.rect(screen, color_light, [width-155, 15, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width-155, 15, 140, 40])

    draw_rect()
    bin_text()

    screen.blit(quit_text, (width-105, 20))
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
