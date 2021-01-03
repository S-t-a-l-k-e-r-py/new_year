import pygame
import random
import sys
import time

pygame.init()
display_x = 1920
display_y = 1080
snow_quantity = 1000
snow_size = 20

display = pygame.display.set_mode((display_x, display_y), pygame.FULLSCREEN)
background_img = pygame.image.load("background.png")
snow = list(map(lambda s: pygame.image.load(s).convert_alpha(), ["1.png", "2.png", "3.png", "4.png"]))
snowfall = []


class Snowflake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.image = pygame.transform.scale(random.choice(snow), (snow_size, snow_size))
        self.init_pos_min = x - random.randint(0, 3)
        self.init_pos_max = x + random.randint(0, 3)
        self.move_right = True

    def move_snowflake(self):
        self.y = self.y + self.speed
        if self.y > display_y:
            self.y = (0 - snow_size)
            self.x = random.randint(0, display_x)
        self.shake()

    def shake(self):
        if self.move_right:
            self.x += 0.1
            if self.x >= self.init_pos_max:
                self.move_right = False
        else:
            self.x -= 0.1
            if self.x <= self.init_pos_min:
                self.move_right = True

    def draw_snow(self):
        self.move_snowflake()
        display.blit(self.image, (self.x, self.y))


def create_snow(max_snow):
    global snowfall
    for s in range(0, max_snow):
        x = random.randint(0, display_x)
        y = random.randint(0, display_y)
        snowfall.append(Snowflake(x, y))


create_snow(snow_quantity)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()
    display.blit(background_img, (0, 0))
    for i in snowfall:
        i.draw_snow()
    time.sleep(0.0040)
    pygame.display.flip()
