"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

"""

def max_pool(List):
    n = len(List)
    if n==2:
        return min(List)
    dp = [[0]*n for _ in range(n)]
    maxpool = 0
    for i in range(n):
        dp[i][i] =0
    for i in range(n):
        for j in range(i,n):
            dp[i][j] = (j - i)*min(List[i],List[j])
        maxpool = max(max(dp[i]),maxpool)
    return maxpool

print(max_pool([1,8,6,2,5,4,8,3,7]))

def max_pool1(List):
    n = len(List)
    if n == 2:
        return min(List)
    pre = 0
    maxpool =0
    for i in range(n):
        for j in range(i,n):
            pre = (j - i)*min(List[i],List[j])
            maxpool = max(pre,maxpool)
    return maxpool
print(max_pool1([1,8,6,2,5,4,8,3,7]))


def max_pool2(height):
    n = len(height)
    if n == 2:
        return min(height)
    i,j,res = 0,n-1,0
    while i<j:
        if height[i]<height[j]:
            res = max(res,height[i]*(j-i))
            i = i+1
        else:
            res = max(res,height[j]*(j-i))
            j = j-1
    return res
print(max_pool2([1,8,6,2,5,4,8,3,7]))