import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 400))
font = pygame.font.SysFont('arial', 20)
fpsClock = pygame.time.Clock()
running = True

# button
def render_text():
    text = "Hello, World!"
    color = (255, 0, 0)  # 文字颜色
    background_color = (255, 255, 255)  # 背景颜色（可选）
    text_surface = font.render(text, True, color, background_color)
    screen.blit(text_surface, (100, 100))


i = 0
button = pygame.Rect(300, 150+80*i, 200, 50)
def render_button():
    GRAY = (200, 200, 200)
    BLACK = (0,0,0)
    pygame.draw.rect(screen, GRAY, button)
    text_surface = font.render("Click", True, BLACK)
    text_rect = text_surface.get_rect(center = (button.x + button.width/2, button.y + button.height/2))
    screen.blit(text_surface, text_rect)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                print('click')

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    screen.fill((60,25,60))

    # RENDER YOUR GAME HERE
    render_text()
    render_button()

    # flip() the display to put your work on screen
    pygame.display.flip()
    fpsClock.tick(30)  # limits FPS to 30

pygame.quit()