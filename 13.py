from ipaddress import *
n = ip_network('211.46.0.0/255.255.128.0')
k = 0
j = 0
for i in n:
    f = f'{i:b}'
    k+=1
    if f.count('1')%4 == 0:
        if f[-2:] == '11':
            print(f)
            j += 1
print(k,j)
