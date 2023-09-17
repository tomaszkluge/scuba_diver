import pygame
import os
import random

pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))


def write(text, x, y, size, color):
    font = pygame.font.SysFont('serif', size)
    text = font.render(text, 1, color)
    screen.blit(text, (x, y))


view = 'menu'


class Rock():

    def __init__(self, x, width):
        self.x = x
        self.width = width
        self.y_up = 0
        self.height_up = random.randint(150, 250)
        self.between = 200
        self.y_down = self.height_up + self.between
        self.height_down = height - self.y_down
        self.color = (192, 192, 192)

    def move(self, speed):
        self.x -= speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y_up, self.width, self.height_up), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y_down, self.width, self.height_down))

class Diver():

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.height = 20
            self.width = 20
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphic = pygame.image.load(os.path.join('cave_diver.png'))


Rocks = []
for i in range(21):
    Rocks.append(Rock(i * width / 20, width / 20))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and view == 'menu':
                view = 'game'

    screen.fill((0, 0, 0))

    if view == 'menu':
        write('Press space to start', 80, 150, 20, color=(0, 0, 255))
        graphic = pygame.image.load(os.path.join('cave_diver.png'))
        screen.blit(graphic, (80, 30))
    elif view == 'game':
        for p in Rocks:
            p.move(1)
            p.draw()
        for p in Rocks:
            if p.x <= -p.width:
                Rocks.remove(p)
                Rocks.append(Rock(width, width / 20))

    pygame.display.update()

pygame.quit()
quit()
