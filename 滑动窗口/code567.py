# https://leetcode.cn/problems/permutation-in-string/
# 567. 字符串的排列
s1 = "ab"
s2 = "eidbaooo"
# s2 = "eidboaoo"

# code here
tstat={}
wstat={}
for c in s1:
    tstat[c] = tstat.get(c,0) + 1

i=0
j=0
valid=0
while j < len(s2):
    wj = s2[j]
    j+=1
    if wj in tstat:
        wstat[wj] = wstat.get(wj, 0) + 1
        if wstat[wj] == tstat[wj]:
            valid += 1

    while (j-i) >= len(s1):
        if valid == len(tstat):
            print("True")
            break

        wi = s2[i]
        i+=1
        if wi in tstat:
            if wstat[wi] == tstat[wi]:
                valid -= 1
            wstat[wi] -= 1
