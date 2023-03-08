"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。


输入：nums = [0,0,0], target = 1
输出：0
"""

def colsesum(nums,target):
    nums.sort()
    n = len(nums)
    if n ==3:
        return sum(nums)
    colse = 10e7

    for i in range(n):
        z,j = i+1,n-1
        while z<j:
            temp = nums[i] + nums[j] + nums[z]
            if temp == target:
                return temp
            if abs(temp - target)<abs(colse-target):
                colse = temp
            if temp>target:
                j = j-1
            if temp<target:
                z = z+1
    return colse

    # while i<j:
    #     for z in range(i+1,j):
    #         temp = nums[i]+nums[j]+nums[z] - target
    #         if abs(colse)>=abs(temp):
    #             colse = temp
    #     if colse==0:
    #         return target
    #     elif colse<0:
    #         i = i + 1
    #     else:
    #         j = j - 1
    # return colse+target
print(colsesum([4,0,5,-5,3,3,0,-4,-5],-2))
print(colsesum([-1,2,1,-4],1))







