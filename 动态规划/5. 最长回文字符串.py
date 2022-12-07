"""
给你一个字符串s，找到s中最长的回文字串
输入： s="babad"
输出： "bab"
解释："aba"同样是符合题意的答案

输入：s = "cbbd"
输出："bb"
"""

"""
解题思路
动态规划
设置dp矩阵
dp[i][j] 记录s[i]至s[j]是否位回文字符串
0、 如果dp[i][j]为回文字符串则s[i] = s[j]
1、如果j- i < 3 则s[i] = s[j]时即为回文字符串
2、如果dp[i][j] 为回文字符串 则dp[i+1][j-1]同样位回文字符串
"""
def longestPalindrome(s):
    n = len(s)
    dp =[[False]*n for _ in range(n)]  #建立dp矩阵   默认所有都为假
    for i in range(n):
        dp[i][i] = True  #dp[i][i] 为真
    if n < 2:
        return s #当s的长度小于2时  返回s即可
    max_len = 1 #默认回文字符串最小为1
    begin = 0
    for L in range(2,n+1): #回文长度L
        for i in range(n):
            j = L + i - 1
            if j >= n:
                break # 当j的位置大于n时跳出
            if s[i] !=s[j]:
                dp[i][j] =False
            else:
                if j - i <3:
                    dp[i][j] =True
                else:
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j] and j-i+1 >max_len:
                max_len = j-i+1
                begin = i
    return s[begin:begin+max_len]

s = "babad"
q = longestPalindrome(s)
print(q)
