## https://www.nowcoder.com/practice/d5f277427d9a4cd3ae60ea6c276dddfd
N_ROW = 4
N_COL = 4
N_MINES_COUNT = 2

# 地图 N x N
# 错误写法 mines_grid = [ ['.'] * N_COL ] * N_ROW
mines_count_grid = [ [0 for _ in range(N_ROW)] for _ in range(N_COL) ]
mines_grid = [ ['.' for _ in range(N_ROW)] for _ in range(N_COL) ]
flags_grid = [ ['.' for _ in range(N_ROW)] for _ in range(N_COL) ]

def mimes_count_print():
    for row in mines_count_grid:
        print('\t'.join(map(str, row)))
def mines_grid_print():
    print('-------')
    for row in mines_grid:
        print(' '.join(row))

# 随机 2 个地雷
point_list = [(r,c) for r in range(N_ROW) for c in range(N_COL)]
# mines_list = random.sample(point_list, N_MINES_COUNT)
mines_list = [(0,0)]
for (r,c) in mines_list:
    mines_count_grid[r][c] = -1
    mines_grid[r][c] = '*'
    for x in [r-1, r, r+1]:
        for y in [c-1,c,c+1]:
            if 0 <= x < N_ROW and 0 <= y < N_COL:
                if mines_count_grid[x][y] != -1:
                   mines_count_grid[x][y] += 1


def click_left(x,y):
    if not (0 <= x < N_ROW and 0 <= y < N_COL):
        print('Invalid Input')
        return
    if mines_count_grid[x][y] == -1:
        print('Game Over')
        return
    elif mines_count_grid[x][y] == 0:
        click_left_0(x,y)
    else:
        mines_grid[x][y] = str(mines_count_grid[x][y])

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
        return
    if flags_grid[x][y] == '*':
        flags_grid[x][y] = '.'
    else:
        flags_list = [item for row in flags_grid for item in row]
        if flags_list.count('*') >= N_MINES_COUNT:
            return
        flags_grid[x][y] = '*'


mimes_count_print()
mines_grid_print()
click_left(0,2)
mines_grid_print()
