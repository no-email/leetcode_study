'''
给你一个整数组nums，请你求出乘积为正数的最长子数组的长度
一个数组的子数组是有原数组中零个或者更多个连续数字组成的数组
请你返回乘积为正数的最长数组长度

示例1：

输入：nums = [1,-2,-3,4]
输出：4
解释：数组本身乘积就是正数，值为 24 。
示例 2：

输入：nums = [0,1,-2,-3,-4]
输出：3
解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
示例 3：

输入：nums = [-1,-2,-3,0,1]
输出：2
解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def getMaxLen(nums):
    n = len(nums)
    total_len = 0
    max_len = 0
    under = 0
    pre = 1
    for i in nums:
        pre = pre * i
        if pre > 0:
            max_len = max_len + 1 + under
            under = 0
        elif pre < 0:
            under += 1
        else:
            total_len = max(total_len, max_len)
            max_len = 0
            under = 0
            pre = 1
    return max(total_len,max_len)
nums = [1,-2,-3,4]
nums = [-1,-2,-3,0,1]
nums = [0,1,-2,-3,-4]
print(getMaxLen(nums))
##nums[-1,2]报错

def getMaxLen(nums):
    length = len(nums)
    positive, negative = [0] * length, [0] * length
    if nums[0] > 0:
        positive[0] = 1
    elif nums[0] < 0:
        negative[0] = 1
    maxlength = positive[0]

    for i in range(1, length):
        if nums[i] > 0:
            positive[i] = positive[i - 1] + 1
            negative[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
        elif nums[i] < 0:
            positive[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
            negative[i] = positive[i - 1] + 1
        else:
            positive[i] = negative[i] = 0
        maxlength = max(maxlength,positive[i])
    return maxlength