from sys import setrecursionlimit

setrecursionlimit(1000000)
def f(n):
    if n == 1: return 1
    return n*f(n-1)

k = f(2024)//4
j = k + f(2023)
print(j//f(2022))
