import pygame
import sys

GRAY = (200,200,200)
R = (255,0,0)
G = (0,255,0)
B = (0,0,255)

# 扫雷: 右键标记
# 选择难度 { 简单3x3 雷1; 普通12x12 雷20; 困难24x24 雷99 }
pygame.init()
screen = pygame.display.set_mode((800,600))
font = pygame.font.SysFont('arial', 20)

class Button:
    total = 0
    def __init__(self, text, size, limit):
        self.rect = pygame.Rect(300, 150+80*Button.total,200,50)
        Button.total += 1
        self.text = text
        self.size = size
        self.limit = limit
    def render(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        text_surface = font.render(self.text, True, (255,0,0))
        # screen.blit(text_surface, (self.rect.centerx - 50, self.rect.centery-10))
        # 居中显示
        text_dest = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_dest)

button_list = [
    Button('Easy', 3, 1),
    Button('Normal', 12, 20),
    Button('Hard', 24, 99),
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in button_list:
                if button.rect.collidepoint(mouse_pos):
                    print(button.text)

    # page components
    screen.fill((240,240,240))
    for button in button_list:
        button.render()

    # page render
    pygame.display.flip()
    pygame.time.Clock().tick(10)