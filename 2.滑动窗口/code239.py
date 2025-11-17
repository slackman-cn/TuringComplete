# https://leetcode.cn/problems/sliding-window-maximum/description/
# 239. 滑动窗口最大值

import collections

nums = [1,3,-1,-3,5,3,6,7]
k = 3
# nums = [7,2,4]
# k = 2
Num = collections.namedtuple('Num', ['index', 'value'])

wstat = [Num(0, nums[0])]
ret = []
for i in range(1, k):
    while len(wstat) and nums[i] > wstat[-1].value:
        wstat.pop()
    wstat.append(Num(i, nums[i]))

# 最大值 wstat[0]  [3,2,1]
ret = wstat[0].value
print(ret, wstat)

for i in range(k, len(nums)):
    if len(wstat) and i - wstat[0].index >= k:
        wstat.pop(0)

    while len(wstat) and nums[i] > wstat[-1].value:
        wstat.pop()
    wstat.append(Num(i, nums[i]))

    ret = wstat[0].value
    print(ret, wstat)