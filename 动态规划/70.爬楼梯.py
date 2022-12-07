"""
假设你正在爬楼梯。需要n阶你才能到达楼顶
每次你可以爬1或2个台阶。 你有多少种不同的方法可以爬到楼梯
"""

"""
因为一次登梯要么上一阶要么上两阶 所有n阶只能有n-1阶或者n-2阶即登上n阶的方法由n-1阶加上n-2阶
所有F(n) = F(n-1)+F(n-2)
"""
def climstairs(n):
    if n ==1:
        return 1
    if n ==2:
        return 2
    before = 1
    after = 2
    end = 0
    for i in range(3,n+1):
        end = before + after
        before = after
        after = end
    return end
print(climstairs(3))