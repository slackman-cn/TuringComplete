import pygame
import sys
import time

GRAY = (200,200,200)
R = (255,0,0)
G = (0,255,0)
B = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((800,600))
font = pygame.font.SysFont('arial', 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # components
    screen.fill((240,240,240))

    # render
    pygame.display.flip()
    pygame.time.Clock().tick(10)