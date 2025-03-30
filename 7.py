i = 11
I = 6580*3240*i
I = I/8
for k in range(1,1000):
    if I*k/3_964_685 <= 510:
        print(k)
