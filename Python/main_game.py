import pygame
import sys
import random
import time

GRAY = (200,200,200)
R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
# login page
N_ROW = 3
N_COL = 3
game_start_time = time.time()
game_mines_count = 1
game_over = False
matrix_rev = [[False for _ in range(N_COL)] for _ in range(N_ROW)]
matrix_mine = [[False for _ in range(N_COL)] for _ in range(N_ROW)]


# 扫雷: 右键标记雷
# 选择难度 { 简单3x3 雷1; 普通12x12 雷20 }
pygame.init()
screen = pygame.display.set_mode((800,600))
font = pygame.font.SysFont('arial', 20)

def render_message():
    n_time = int(time.time() - game_start_time)
    text_time = font.render(f'Time: {n_time} seconds', True, (255,0,0))
    n_mines = game_mines_count - sum([sum(row) for row in matrix_mine])
    text_mines = font.render(f'Left Mines: {n_mines}', True, (255,0,0))
    screen.blit(text_time, (10,10))
    screen.blit(text_mines, (800-200,10))

# 0 空板
# -1 雷
# 1,2,3 周围8个格子有N个雷
board = []
for i in range(N_ROW):
    row = []
    for j in range(N_COL):
        row.append(0)
    board.append(row)
# 随机
positions = []
for i in range(N_ROW):
    for j in range(N_COL):
        positions.append((i,j))
mime_position = random.sample(positions, game_mines_count)
# 提示周围雷个数
for (i,j) in mime_position:
    board[i][j] = -1
    for x in [i-1, i, i+1]:
        for y in [j-1, j, j+1]:
            if 0 <= x < N_ROW and 0 <= y < N_COL:
                if board[x][y] != -1:
                    board[x][y] += 1
print(board)
print(mime_position)

size = min(800 // N_ROW, (600 - 50) // N_COL)
def render_board():
    for i in range(N_ROW):
        for j in range(N_COL):
            rect = pygame.Rect(j*size, i*size+50, size, size)
            if matrix_rev[i][j]:
                # 反转
                if board[i][j] == -1:
                    pygame.draw.rect(screen, R, rect)
                else:
                    pygame.draw.rect(screen, (255,255,255), rect)
                    if board[i][j] > 0:
                        text = font.render(str(board[i][j]), True, (0,0,0))
                        text_dest = text.get_rect(center = rect.center)
                        screen.blit(text, text_dest)
            else:
                pygame.draw.rect(screen,GRAY, rect)
                if matrix_mine[i][j]:
                    pygame.draw.circle(screen,B,rect.center, size//3)
            # 黑色边框
            pygame.draw.rect(screen, (0,0,0),rect,1)

def click_board(i,j):
    if 0 <= i < N_ROW and 0 <= j < N_COL:
        if matrix_rev[i][j]:
            return
        matrix_rev[i][j] = True
        if board[i][j] == 0:
            for x in [i-1,i,i+1]:
                for y in [j-1,j,j+1]:
                    click_board(x,y)
# 所有雷被标记
def game_win():
    con1 = all([
        matrix_rev[i][j] or matrix_mine[i][j]
        for i in range(N_ROW)
        for j in range(N_COL)
        if board[i][j] == -1
    ])
    con2 = all([
        matrix_rev[i][j]
        for i in range(N_ROW)
        for j in range(N_COL)
        if board[i][j] != -1
    ])
    if con1 and con2:
        print('win')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[1] > 50:
                i = (pos[1]-50) // size
                j = pos[0]//size
                print(i,j)
                # left click
                if event.button == 1 and not matrix_mine[i][j]:
                    if board[i][j] == -1:
                        game_over = True
                else:
                    click_board(i,j)
                # right click
                if event.button == 3:
                    matrix_mine[i][j] = not matrix_mine[i][j]

    # components
    screen.fill((240,240,240))
    render_message()
    render_board()

    # render
    pygame.display.flip()
    pygame.time.Clock().tick(10)