'''
给你一个整数组nums,请你找出一个具有最大和的连续子数组(子数组最少包含一个元素),返回其最大和
子数组是数组中的一个连续部分
示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组[4,-1,2,1] 的和最大，为6 。
示例 2：

输入：nums = [1]
输出：1

示例 3：

输入：nums = [5,4,-1,7,8]
输出：23


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
动态规划 只要求每个i的最大子数组f{i}
即在判断f{i}时 考虑 nums[i]  和 f{i-1} + nums[i] 的大小即可
'''
def maxSubArray(nums):
    pre = 0
    maxsum = nums[0]
    n = len(nums)
    for i in range(n):
        pre = max(pre + nums[i], nums[i])
        maxsum = max(pre, maxsum)
    return maxsum
nums = [23,452,-1,5,-3]
print(maxSubArray(nums))