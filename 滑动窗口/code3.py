# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 3. 无重复字符的最长子串
s = "abcabcbb"
s = "bbbbb"
s = 'pwwkew'

# code here
wstat={}
def check_valid():
    for v in wstat.values():
        if v > 1:
            return False
    return True

i=0
j=0
ret = ''
ret_len = 0
while j < len(s):
    wj = s[j]
    j+=1
    wstat[wj] = wstat.get(wj,0)+1

    # 右指针遇到重复，就移动左指针
    while i < j:
        if check_valid():
            if (j - i) > ret_len:
                print(i, j, s[i:j])
                ret_len = (j - i)
                ret = s[i:j]
            break
        else:
            wi = s[i]
            i += 1
            wstat[wi] -= 1

print('Ret', ret, ret_len)