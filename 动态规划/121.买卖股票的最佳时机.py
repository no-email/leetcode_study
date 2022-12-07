'''
给定一个数组price， 它的第i个元素prices[i] 表示一支给定股票第i天
的价格.你只能选择某一天买入这支股票,并选择在未来的某一个不同的日志卖出该
股票.设定一个算法来计算你能所获取的最大利润
返回你可以从这笔交易中获取的最大利润.如果你不能获取任何利润,返回0

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def maxprofit(price):
    n = len(price)
    minprice = price[0]
    maxpro = 0
    for i in range(1,n):
        if price[i] < minprice:
            minprice = price[i]
        else:
            maxpro = max(price[i] - minprice, maxpro)
    return maxpro
nums = [7,1,5,3,6,4]
nums = [7,6,4,3,1]
print(maxprofit(nums))

"""
解题方法:
本题即求出数列中最大的极差,切要求较小的值在前面,较大的值在后面
可以用动态规划的方法来求解
首先便利数列,确认局部最小的值,即每次都和当前最小值作比较,以期取得最小值.
其次当取得值比当前最小值大时计算差值,取最大
"""