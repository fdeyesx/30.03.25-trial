def main(n):
    r = 0
    if n%3 == 0: r = n%3
    else: r = n-1

    if r%5 == 0: r%=5
    else: r-=1

    if r%11 == 0: r%=11
    else: r-=1

    return r

k = 0
for i in range(1,10000000):
    if main(i) == 8:
        k+=1
print(k)
