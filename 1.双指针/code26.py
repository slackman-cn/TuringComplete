# 26. 删除有序数组中的重复项
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
nums = [0,0,1,1,1,2,2,3,3,4]

# code here
if len(nums) <=1:
    print('Return')

it=nums[0]
k=1
for i in range(1, len(nums)):
    if nums[i] == it:
        continue
    else:
        it = nums[i]
        nums[k] = it
        k+=1
        print(it, nums[0:k])



print(nums, k)