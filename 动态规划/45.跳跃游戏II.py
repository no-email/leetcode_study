'''
给你一个非负整数组nums，你最初位于数组的第一个位置
数组中的每个元素代表你在该位置可以跳跃的最大长度
你的目标是使用最少的跳跃次数到达数组的最后一个位置
假设你总是可以达到数组的最后一个位置
'''
"""
示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
    从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
记录每一跳时当前的位置sit以及最大位置max_length,遍历当前位置至最大位置的每个点,可以跳跃的最远距离
"""
def jump(nums):
    i = 0
    max_length = 0
    n = len(nums)
    times = 1
    while max_length < n-1:
        for j in range(i+1,i+nums[i]):
            max_length = max(j+nums[j],max_length)
        i = max_length
        times = times +1
    return times
nums = [2,3,1,1,4]
print(jump(nums))


def jump1(nums):
    n = len(nums)
    maxpod,end,step =0,0,0
    for i in range(n):
        if maxpod >=i:
            maxpod = max(maxpod,i+nums[i])
        if i == end:
            end = maxpod
            step +=1
    return step

