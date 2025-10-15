import pygame
import random
import time
N_MINES_COUNT = 2
N_ROW = 4
N_COL = 4
N_SIZE = min(800 // N_ROW, (600 - 50) // N_COL)
GAME_MODE = {'Easy': 1, 'Normal': 2, 'Hard': 3}
GAME_STATE = {'victory': False, 'defeat': False, 'start': time.time()}

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont('arial', 20)
running = True

# 地图 N x N
mines_count_grid = [ [0 for _ in range(N_ROW)] for _ in range(N_COL) ]
mines_grid = [ ['.' for _ in range(N_ROW)] for _ in range(N_COL) ]

# 随机 2 个地雷
point_list = [(r,c) for r in range(N_ROW) for c in range(N_COL)]
mines_list = random.sample(point_list, N_MINES_COUNT)
for (r,c) in mines_list:
    mines_count_grid[r][c] = -1
    for x in [r-1, r, r+1]:
        for y in [c-1,c,c+1]:
            if 0 <= x < N_ROW and 0 <= y < N_COL:
                if mines_count_grid[x][y] != -1:
                   mines_count_grid[x][y] += 1

for row in mines_count_grid:
    print('\t'.join(map(str, row)))

def render_game_state():
    mines_text = font.render(f'Total Mines: {N_MINES_COUNT}', True, (255, 0, 0))
    screen.blit(mines_text, (10, 10))
    duration = int(time.time() - GAME_STATE['start'])
    duration_text = font.render(f'Time: {duration} seconds', True, (255, 0, 0))
    screen.blit(duration_text, (200, 10))

    if GAME_STATE['victory']:
        game_text = font.render('Game Success!', True, (255, 0, 0))
        screen.blit(game_text, (800 - 200, 10))
    if GAME_STATE['defeat']:
        game_text = font.render('Game Fail!', True, (255, 0, 0))
        screen.blit(game_text, (800 - 200, 10))

def render_grid():
    color_unclick = (192,192,192)
    color_click = (255,255,255)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    for (r,c) in point_list:
        rect = pygame.Rect(c*N_SIZE, r*N_SIZE+50, N_SIZE, N_SIZE)
        ## 左键棋盘
        if mines_grid[r][c] == '.':
            pygame.draw.rect(screen, color_unclick, rect)
        elif mines_grid[r][c] == '*':
            pygame.draw.rect(screen, red, rect)
        elif mines_grid[r][c] == '?':
            pygame.draw.rect(screen, blue, rect)
        elif mines_grid[r][c] == '0':
            pygame.draw.rect(screen, color_click, rect)
        else:
            pygame.draw.rect(screen, color_click, rect)
            text = font.render(str(mines_grid[r][c]), True, (0, 0, 0))
            text_dest = text.get_rect(center=rect.center)
            screen.blit(text, text_dest)
        # 黑色边框
        pygame.draw.rect(screen, (0,0,0),rect,1)

def click_left(x,y):
    if not (0 <= x < N_ROW and 0 <= y < N_COL):
        print('Invalid Input')
        return
    if mines_grid[x][y] == '?':
        mines_grid[x][y] = '.'
        return
    if mines_count_grid[x][y] == -1:
        print('Game Over')
        GAME_STATE['defeat'] = True
        mines_grid[x][y] = '*'
        return
    if mines_count_grid[x][y] == 0:
        click_left_0(x,y)
    else:
        mines_grid[x][y] = str(mines_count_grid[x][y])
    mines_grid_flat = [item for _row in mines_grid for item in _row]
    left_mines = sum(1 for x in mines_grid_flat if x == '.')
    if left_mines == N_MINES_COUNT:
        GAME_STATE['victory'] = True

def click_left_0(x,y):
    if not (0 <= x < N_ROW and 0 <= y < N_COL):
        return
    if mines_count_grid[x][y] != 0:
        return
    if mines_grid[x][y] == '0':
        return
    mines_grid[x][y] = '0'
    for xr in [x - 1, x, x + 1]:
        for yc in [y - 1, y, y + 1]:
            click_left_0(xr, yc)

def click_right(x,y):
    if not (0 <= x < N_ROW and 0 <= y < N_COL):
        print('Invalid Input')
        return
    if mines_grid[x][y] == '?':
        mines_grid[x][y] = '.'
    elif mines_grid[x][y] == '.':
        mines_grid[x][y] = '?'


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if GAME_STATE['defeat'] or GAME_STATE['victory']:
                print('Finish...')
                break
            pos = pygame.mouse.get_pos()
            x = (pos[1]-50) // N_SIZE
            y = pos[0] // N_SIZE
            # left click
            if event.button == 1:
                click_left(x,y)
            # right click
            if event.button == 3:
                click_right(x,y)

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    screen.fill((60,25,60))

    # RENDER YOUR GAME HERE
    render_grid()
    render_game_state()

    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.time.Clock().tick(15)  # limits FPS to 15

pygame.quit()
