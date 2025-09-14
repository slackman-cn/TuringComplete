import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 400))
running = True

# 加载logo图
img = pygame.image.load("linux.ico")
pos_x = 100
pos_y = 100
move_x = 0
move_y = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_y = -5
            if event.key == pygame.K_DOWN:
                move_y = 5
            if event.key == pygame.K_LEFT:
                move_x = -5
            if event.key == pygame.K_RIGHT:
                move_x = 5
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                move_x = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                move_y = 0
    pos_x += move_x
    pos_y += move_y
    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    screen.fill((255,255,255))

    # RENDER YOUR GAME HERE
    screen.blit(img, [pos_x, pos_y])

    # flip() the display to put your work on screen
    pygame.display.flip()
    # 控制帧率
    pygame.time.Clock().tick(60)

pygame.quit()