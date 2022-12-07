'''
给你一个整数组nums，你可以对它进行一些操作
每次操作中，选择任意一个nums[i],删除它病获得nums[i]的点数
之后你必须删除所有等于nums[i] -1 和nums[i]+1的元素

开始你拥有0个点数,返回你能通过这些操作获得的最大点数
'''
"""
打家劫舍进化版
0、创建一个列表，长度为数组中最大的值List
1、相同i数值求和，并填入列表中对应数值的位置List[i]
2、打家劫舍
"""
def deletAndEarn(nums):
    if len(nums)<2:
        return max(nums)
    dp = [0 for _ in range(max(nums)+1)]
    for i in nums:
        dp[i] += i
    n = len(dp)
    first = dp[0]
    second = max(dp[0],dp[1])
    total = 0
    for i in range(2,n):
        total = max(first + dp[i],second)
        first = second
        second = total
    return total
nums = [2,2,3,3,3,4]
print(deletAndEarn(nums))
