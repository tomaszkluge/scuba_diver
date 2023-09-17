import pygame

pygame.init()

width = 700
height = 700
screen = pygame.display.set_mode((width, height))


def write(text, x, y, size, color):
    font = pygame.font.SysFont('serif', size)
    text = font.render(text, 1, (0, 0, 255))
    x = (width - text.get_width()) / 2
    y = (height - text.get_height()) / 2
    screen.blit(text, (x, y))


write('Press space to start', 80, 150, 20)

pygame.display.update()
