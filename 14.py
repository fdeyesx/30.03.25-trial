def f(n):
    s = ''
    while n!=0:
        s = str(n%7) + s
        n //= 7
    return s

for x in range(0,1000):
    s = 3*7**(x+1) + 13*7**(x+2) + 31*7**(3*x) + 7**(2*x)
    s1 = f(s)
    sum1 = 0
    for i in s1:
        sum1 += int(i)
    if sum1 == 18:
        print(x)
        break
