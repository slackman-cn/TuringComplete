import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 300))
fpsClock = pygame.time.Clock()
running = True

# 默认字体
# font = pygame.font.SysFont(None, 20)
font = pygame.font.SysFont('arial', 20)
start_time = pygame.time.get_ticks()

available_fonts = pygame.font.get_fonts()
print(available_fonts)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    screen.fill((255,255,255))

    # RENDER YOUR GAME HERE
    current_time = pygame.time.get_ticks()
    total_time = (current_time - start_time) // 1000
    # print(f"Total time {total_time} seconds")
    total_text = font.render(f"Total time {total_time} seconds", True, (0,0,0))
    screen.blit(total_text, (50,50))

    # flip() the display to put your work on screen
    pygame.display.flip()
    fpsClock.tick(10)  # limits FPS to 30

pygame.quit()