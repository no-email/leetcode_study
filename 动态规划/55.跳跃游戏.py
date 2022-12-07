'''
给定一个非负整数数组 nums,你最初位于数组的第一个下标.数组中的每个元素代表你在该位置可以跳跃的最大长度
判断你是否能够达到最后一个下标
示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
""":param
深度优先搜索
每一步都持续按最大步跨越 如果可以达到最后一个下标则返回true
如果不行,则退回上一步按最大步减一跨越,直至走完全部路线
"""
'''
贪心算法
每一步按最大步跨越，其所能到达的最远位置为可达的，亦可以说是在其最远位置以内的 均可达。
我们用max_length记录最远可达，每到一个点都计算最远可达的点，并与max_length最对比 更新manx_length
当manx_length大于n时则可达,否则不可达
'''
def canJump(nums):
    n = len(nums)
    max_length = 0
    i =0
    while i<max_length:
        max_length = max(i+nums[i],max_length)
        if max_length>=n-1:
            return True
        i = i +1
    return False
nums = [2,3,1,1,4]
print(canJump(nums))

nums = [3,2,1,0,4]
print(canJump(nums))