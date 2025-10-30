# 304. 二维区域和检索 - 矩阵不可变
# https://leetcode.cn/problems/range-sum-query-2d-immutable/description/

def sumRange(sums: List[int], left: int, right: int) -> int:
    sum_left = 0
    sum_right = 0
    if 0 < left < len(sums):
        sum_left = sums[left - 1]
    if right >= len(sums):
        sum_right = sums[-1]
    elif right >= left:
        sum_right = sums[right]
    return sum_right - sum_left


class NumMatrix:
    sums_matrix = []
    def __init__(self, matrix: List[List[int]]):
        self.sums_matrix = []  # 必须重置，不然测试用例报错
        for row in matrix:
            sums = [row[0]] * len(row)
            for i in range(1, len(row)):
                sums[i] = sums[i-1] + row[i]
            self.sums_matrix.append(sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row2 < row1:
            return 0
        sums = 0
        for n in range(row1, row2+1):
            print(self.sums_matrix[n])
            sums += sumRange(self.sums_matrix[n], col1, col2)
        return sums
