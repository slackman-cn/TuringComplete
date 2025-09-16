## 扫雷
## https://www.nowcoder.com/practice/d5f277427d9a4cd3ae60ea6c276dddfd

import random
N_ROW = 4
N_COL = 4

# 地图 N x N
# 错误写法 mines_grid = [ ['.'] * N_COL ] * N_ROW
mines_grid = [ ['.' for _ in range(N_ROW)] for _ in range(N_COL) ]
mines_count_grid = [ [0 for _ in range(N_ROW)] for _ in range(N_COL) ]
def mines_grid_print():
    print('-------')
    for row in mines_grid:
        print(' '.join(row))
    for row in mines_count_grid:
        print('\t'.join(map(str, row)))

# 随机 2 个地雷
point_list = [(r,c) for r in range(N_ROW) for c in range(N_COL)]
mines_list = random.sample(point_list, 2)
for (r,c) in mines_list:
    mines_grid[r][c] = '*'
    mines_count_grid[r][c] = -1
    for x in [r-1, r, r+1]:
        for y in [c-1,c,c+1]:
            if 0 <= x < N_ROW and 0 <= y < N_COL:
                if mines_count_grid[x][y] != -1:
                   mines_count_grid[x][y] += 1
mines_grid_print()