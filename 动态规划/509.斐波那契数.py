"""
斐波那契数（通常用F(n)表示） 形成的序列称为斐波那契数。该数列由0和1 开始，
后面的每一项数字都是前面两项数字的和
也就是
F(0) = 0, F(1)= 1
F(n)= F(n-1) + F(n-2) 其中n>1
给定n,请计算F(n)
"""
def fib(n):
    # df = [[0]*n for _ in range(n)]
    if n ==0:
        return 0
    if n == 1:
        return 1
    befor = 0
    after = 1
    end = 0
    for i in range(2,n+1):
        end = befor + after
        befor = after
        after = end
    return end
print(fib(4))
