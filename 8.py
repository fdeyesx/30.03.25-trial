from itertools import *
k=0
for i in product('0123456789abcdef',repeat=3):
    s = ''.join(i)
    if s[0] != '0':
        if s[0] > s[1] > s[2]:
            k+=1
            print(s)

for x in product('0123456789abcdef', repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if s[0] > s[1] > s[2] > s[3] > s[4]:
            k+=1
            print(s)

print(f'!!{k}')
