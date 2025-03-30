i = 9
I = 70*1024*8
for k in range(1,1000):
    if i*k*345 >= I:
        print(k)
        break
