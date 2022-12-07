"""
泰波那契序列Tn 定义如下:
T0= 0, T1= 1, T2= 1 且在n>=0 的条件下 Tn+3= Tn + Tn+1 + Tn+2
给你整数n,请返回第n个泰波那契数Tn的值
"""
def tribonacci(n):
    if n ==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    a=0
    b=1
    c=1
    d=0
    for i in range(3,n+1):
        d = a+b+c
        a = b
        b = c
        c = d
    return d
print(tribonacci(25))