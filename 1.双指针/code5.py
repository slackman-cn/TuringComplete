# 5. 最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/description/
s = "babad"

# code here
if len(s) <=1:
    print(s)
#
def check_valid(i=0, j=len(s)-1):
    while i < j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

# 复杂度n^2
ret = ''
ret_len=0
for i in range(0, len(s)):
    j = len(s) - 1
    while j > i:
        if s[j] == s[i] and (j-i) > ret_len and check_valid(i,j):
            ret = s[i:j+1]
            ret_len = (j-i)
        j-=1

if ret_len == 0:
    print(s[0])
else:
    print(ret)
print(ret, ret_len)
