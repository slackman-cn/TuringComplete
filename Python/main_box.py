import pygame
import enum

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 400))
fpsClock = pygame.time.Clock()
running = True
font = pygame.font.SysFont('arial', 20)

box = [ [pygame.Rect(20+i*50,20+j*50,50,50) for j in range(4)] for i in range(4) ]
box_flat = [element for row in box for element in row]

head0 = pygame.Rect(0,0, 80, 80)
head_rows = [pygame.Rect(80+50*i,0,50,80) for i in range(4)]
head_cols = [pygame.Rect(0,80+50*i,80,50) for i in range(4)]
head_tags = ['00', '01', '11', '10']

def render_head():
    GRAY = (200, 200, 200)
    BLACK = (0,0,0)
    for i,row in enumerate(head_rows):
        pygame.draw.rect(screen, GRAY, row, 1) # border
        text_surface = font.render("CD", True, BLACK)
        screen.blit(text_surface, (row.left+10, row.top+10))
        text_surface = font.render(head_tags[i], True, BLACK)
        screen.blit(text_surface, (row.left+12, row.top+40))
    for i,col in enumerate(head_cols):
        pygame.draw.rect(screen, GRAY, col, 1)  # border
        text_surface = font.render("AB=" + head_tags[i], True, BLACK)
        screen.blit(text_surface, (col.left+10, col.centery-10))


class StateEnum(enum.Enum):
    H = '1'
    L = '0'
    DISMISS = 'x'

class State:
    def __init__(self, row, col):
        # row=0, top=0
        self.rect = pygame.Rect(head0.bottomright[0]+50*col,head0.bottomright[1]+50*row, 50,50)
        self.pos = (row,col)
        self.state = StateEnum.L
        self.name = 'ABCD'
        self.value = head_tags[row] + head_tags[col]
    def state_next(self):
        if self.state == StateEnum.L:
            self.state = StateEnum.H
        elif self.state == StateEnum.H:
            self.state = StateEnum.DISMISS
        elif self.state == StateEnum.DISMISS:
            self.state = StateEnum.L
    def render(self):
        text_surface = font.render(self.state.value, True, (0,0,0))
        pygame.draw.rect(screen, (200,200,200), self.rect, 1) # border
        screen.blit(text_surface, (self.rect.centerx-10, self.rect.centery-10))


state_init = [ [State(i,j) for j in range(4)] for i in range(4) ]
state_list = [element for row in state_init for element in row]
for ele in state_init[0]:
    print(ele.pos, ele.value, ele.rect)

def render_box():
    GRAY = (200, 200, 200)
    BLACK = (0,0,0)
    text_surface = font.render("X", True, BLACK)
    for button in box_flat:
        # pygame.draw.rect(screen, GRAY, button)
        pygame.draw.rect(screen, GRAY, button, 1) # border
        screen.blit(text_surface, (button.centerx-10, button.centery-10))
        # pygame.draw.line(screen, BLACK, button.topleft, button.topright)
    # pygame.draw.line(screen, BLACK, (70,70), (70, 70+200))
    # pygame.draw.line(screen, BLACK, (70,70), (70+200, 70))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for s in state_list:
                if s.rect.collidepoint(mouse_pos):
                    print(s.state)
                    s.state_next()

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    screen.fill((60,25,60))

    # RENDER YOUR GAME HERE
    # render_box()
    render_head()
    for s in state_list: s.render()

    # flip() the display to put your work on screen
    pygame.display.flip()
    fpsClock.tick(5)  # limits FPS to 5

pygame.quit()