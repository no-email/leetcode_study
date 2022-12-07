"""
给定一个数组price,其中price[i]表示股票第i天的价格
在每一天,你可能会决定购买或出售股票,你在任何时候最多
只能持有一只股票你可以购买它然后再同一天出售
返回你能获得的最大利润

示例 1:

输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:
输入: prices = [1,2,3,4,5]
输出: 4
解释: 在第1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
       注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def maxprofit(prices):
    n = len(prices)
    minprice = prices[0]
    total_profit = 0
    for i in range(1,n):
        if prices[i] < minprice:
            minprice = prices[i]
        else:
            total_profit = total_profit + prices[i] - minprice
            minprice = prices[i]
    return total_profit
prices = [7,1,5,7,3,6,4]
print(maxprofit(prices))

"""
解题思路:
本题即找数据的的拐点,即局部最小值和局部最大值,
当后一个数大于前一个数时,即计算两者的差值并入利润中
且后一个数记为最小值,继续遍历
当后一个数小于前一个数时把后一个数记为最小值,继续遍历

即记录两个值,minprice,和total_profit
分两中情况：
一、后一个数小于前一个数
二、后一个数大于前一个数
第一种情况时:
更换minprice
第二种情况时:
total_profit = total_profit + price[i] - minprice
minprice = price[i]

"""