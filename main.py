import pygame
import os
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
background_color = (100, 149, 237)


# Function for drawing text on the screen
def write(text, x, y, size, color):
    font = pygame.font.SysFont('serif', size)
    text_surface = font.render(text, 1, color)
    screen.blit(text_surface, (x, y))


# Game states
VIEW_MENU = 'menu'
VIEW_GAME = 'game'
VIEW_END = 'end'


# Class for representing rocks
class Rock:
    def __init__(self, x, width):
        self.x = x
        self.width = width
        self.height_up = random.randint(150, 250)
        self.between = 200
        self.height_down = height - self.height_up - self.between
        self.color = (192, 192, 192)

    def move(self, speed):
        self.x -= speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.height_up))
        pygame.draw.rect(screen, self.color, (self.x, self.height_up + self.between, self.width, self.height_down))

    def collision(self, player):
        return self.x < player.x + player.width and self.x + self.width > player.x and (
                player.y < self.height_up or player.y + player.height > self.height_up + self.between)


# Class for the player's character (diver)
class Diver:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.graphic = pygame.image.load(os.path.join('cave_diver.png'))

    def draw(self):
        screen.blit(self.graphic, (self.x, self.y))

    def move(self, dy):
        self.y += dy


# Create a list of rocks
rocks = [Rock(i * width / 20, width / 20) for i in range(21)]

# Create the player character
player = Diver(250, 275)

# Vertical movement speed
dy = 0

# Game loop
view = VIEW_MENU
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (view == VIEW_MENU or view == VIEW_END):
                view = VIEW_GAME
                player = Diver(250, 275)
                rocks = [Rock(i * width / 20, width / 20) for i in range(21)]
            if event.key == pygame.K_UP:
                dy = -1
            if event.key == pygame.K_DOWN:
                dy = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0

    screen.fill(background_color)

    if view == VIEW_MENU:
        write('Press space to start', 80, 150, 20, color=(0, 0, 255))
        screen.blit(player.graphic, (80, 30))
    elif view == VIEW_GAME:
        for rock in rocks:
            rock.move(1)
            rock.draw()
            if rock.collision(player):
                view = VIEW_END
        for rock in rocks:
            if rock.x <= -rock.width:
                rocks.remove(rock)
                rocks.append(Rock(width, width / 20))
        player.draw()
        player.move(dy)
    elif view == VIEW_END:
        screen.blit(player.graphic, (80, 30))
        write("You lose", 50, 290, 20, color=(255, 0, 0))
        write('Press space to restart', 80, 150, 20, color=(0, 0, 255))

    pygame.display.update()

pygame.quit()
quit()
