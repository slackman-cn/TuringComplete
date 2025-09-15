import pygame
import enum

# 4 elements ABCD
N = 4
NLEFT = 2
NTOP = N - NLEFT
names = 'ABCDEFGH'

# pygame setup
pygame.init()
screen = pygame.display.set_mode((200*NTOP, 200*NLEFT))
fpsClock = pygame.time.Clock()
running = True
font = pygame.font.SysFont('arial', 20)

# Gray Code
def num_to_glist(num, length):
    blist = [0] * length
    for i in range(length):
        if num & (2**i) > 0:
            blist[length-1-i] = 1
    blist_rightshift = [0] + blist[:-1]
    # XOR
    glist = [ blist[i] ^ blist_rightshift[i] for i in range(length)]
    return ''.join(map(str, glist))


head0 = pygame.Rect(0,0, 100, 100)
head_top = [pygame.Rect(100+50*i,0,50,100) for i in range(2**NTOP)]
head_left = [pygame.Rect(0,100+50*i,100,50) for i in range(2**NLEFT)]
head_left_name = names[0:NLEFT]
head_top_name = names[NLEFT:N]
head_left_tags = [ num_to_glist(i, NLEFT)  for i in range(2**NLEFT)]
head_top_tags = [ num_to_glist(i, NTOP)  for i in range(2**NTOP)]
print(head_left_name, head_left_tags)

def render_head():
    GRAY = (200, 200, 200)
    BLACK = (0,0,0)
    for i,row in enumerate(head_top):
        pygame.draw.rect(screen, GRAY, row, 1) # border
        text_surface = font.render(head_top_name, True, BLACK)
        screen.blit(text_surface, (row.left+10, row.top+10))
        text_surface = font.render(head_top_tags[i], True, BLACK)
        screen.blit(text_surface, (row.left+12, row.top+40))
    for i,col in enumerate(head_left):
        pygame.draw.rect(screen, GRAY, col, 1)  # border
        text_surface = font.render(head_left_name + "=" + head_left_tags[i], True, BLACK)
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
        self.code = head_left_tags[row] + head_top_tags[col]
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


state_init = [ [State(i,j) for j in range(2**NTOP)] for i in range(2**NLEFT) ]
state_list = [element for row in state_init for element in row]
for ele in state_init[0]:
    print(ele.pos, ele.code, ele.rect)


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
                    s.state_next()
                    print(s.code, s.state)

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