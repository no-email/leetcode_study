"""
给你一个整数组cost,其中cost[i] 是从楼梯i个台阶向上爬所需要支付的费用.
一旦你支付此费用即可向上爬一个或两个台阶.你可以选择从下标为0或者下标为1的台阶开始爬楼梯
请返回所到达楼梯顶部的最低花费

输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。总花费为 15 。


输入：cost = [1,100,1,1,1,100,1,1,100,1]
输出：6
解释：你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6 。
"""
def mincostclimbstairs(cost):
    n = len(cost)
    last = 0
    befor = 0
    total_cost = 0
    # times = 1
    while n>=2:
        last = cost[n-1]
        befor = cost[n-2]
        if last<befor:
            total_cost +=last
            n=n-1
            last = cost[n-1]
            befor = cost[n-2]
        else:
            total_cost += befor
            n = n-2
            last = cost[n-1]
            befor = cost[n-2]
        # times = times + 1
    return total_cost

def minCostClimbingStairs1(self, cost: List[int]) -> int:
    n = len(cost)
    dp=[0] * (n+1)
    for i in range(2,n+1):
        dp[i]= min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    return dp[n]



cost = [1,100,1,1,1,100,1,1,100,1]
print(mincostclimbstairs(cost))
cost1 = [10,15,20]
print(mincostclimbstairs(cost1))