'''
给定一个整数数组prices,其中prices[i]表示第i天的股票价格;整数fee代表了交易
股票的手续费用.你可以无限次地完成交易,但是你每笔交易都要付手续费.如果你已经购
买了一支股票,在卖出它之前你就不能再继续购买股票了
返回获得利润的最大值
注意:这里的一笔交易值买入持有并卖出股票的整个过程,每笔交易你只需要为支付一次手
续费
'''

"""
示例 1：

输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
输出：8
解释：能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润:((8 - 1) - 2) + ((9 - 4) - 2) = 8
示例 2：

输入：prices = [1,3,7,5,10,3], fee = 3
输出：6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def maxprofit(prices,fee):
    buy = [x+fee for x in prices]
    n = len(prices)
    minprice = buy[0]
    total_profit = 0
    for i in range(1,n):
        minprice = min(buy[i],minprice)
        if prices[i] > minprice:
            total_profit = total_profit + prices[i] - minprice
            minprice = prices[i]
    return total_profit
prices = [1, 3, 2, 8, 4, 9]
print(maxprofit(prices,2))


