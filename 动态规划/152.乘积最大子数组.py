'''
给你一个整数数组nums,请你找出数组中乘积最大的非空连续子数组(该子数组中至少包含一个数字)
并返回该子数组所对应的乘积

示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# def maxproduct(nums):
#     pre,maxs,mins = nums[0],0
#     for i in range(1,len(nums)):
#         pre = max(pre*nums[i],nums[i])
#         maxs = max(pre,maxs)
#     return maxs
#
# nums = [2,3,-2,4]
# print(maxproduct(nums))
def maxProduct( nums):
    if not nums:
        return
    res = nums[0]
    pre_max = nums[0]
    pre_min = nums[0]
    for num in nums[1:]:
        cur_max = max(pre_max * num, pre_min * num, num)
        cur_min = min(pre_max * num, pre_min * num, num)
        res = max(res, cur_max)
        pre_max = cur_max
        pre_min = cur_min
    return res


