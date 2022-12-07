'''
给定一个长度为n的环形整数数组nums,返回nums的非空子数组的最大可能和
环形数组意味着数组的末端将会与开头相连呈环状,形式上,nums[i]的下一个元素是nums[(i+1)%n],
nums[i]的前一个元素是nums[(i-1+n)%n]
子数组最多只能包含固定缓冲区nums中的每个元素一次,形式上对于子数组nums[i],nums[i+1],...nums[j],不存在
i<=k1,k2<=j  其中k1%n == k2%n
示例 1：

输入：nums = [1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3
示例 2：

输入：nums = [5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
示例 3：

输入：nums = [3,-2,2,-3]
输出：3
解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-sum-circular-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

""":param
两种情况
一、不成环状即——————最大子数组和
二、成环状，首一部分，尾一部分 max(前缀+后缀)


解释二、
max(前缀+后缀) 
= total_sum - center_array
= total_sum + max(-center_array)
= total_sum - mn(center_array)
"""
def maxSubarraySumCircular(df):
    total,maxsum,curmax,minsum,curmin = 0,df[0],0,df[0],0
    for a in df:
        curmax = max(curmax+a,a)
        maxsum = max(maxsum,curmax)
        curmin = min(curmin+a,a)
        minsum = min(curmin,minsum)
        total +=a
    return max(maxsum,total-minsum) if maxsum>0 else maxsum