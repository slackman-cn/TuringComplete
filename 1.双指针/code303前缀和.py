# 303. 区域和检索 - 数组不可变
# https://leetcode.cn/problems/range-sum-query-immutable/description/

class NumArray:
    sums = []
    def __init__(self, nums: List[int]):
        if len(nums) <= 0:
            return
        self.sums = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        sum_left = 0
        sum_right = 0
        if 0 < left < len(self.sums):
            sum_left = self.sums[left - 1]
        if right >= len(self.sums):
            sum_right = self.sums[-1]
        elif right >= left:
            sum_right = self.sums[right]
        return sum_right - sum_left
