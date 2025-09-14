import pygame
import sys
import random
import time

GRAY = (200,200,200)
R = (255,0,0)
G = (0,255,0)
B = (0,0,255)

# 扫雷: 右键标记雷
# 选择难度 { 简单3x3 雷1; 普通12x12 雷20 }
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