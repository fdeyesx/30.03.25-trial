def main(n):
    if n%3 == 0: n//=3
    else: n-=1

    if n%5 == 0: n//=5
    else: n-=1

    if n%11 == 0: n//=11
    else: n-=1
    return n

k = 0
for i in range(1,100000):
    if main(i) == 8:
        k+=1
print(k)
