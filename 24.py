from re import *

s = open('24.23.txt').readline()
r = '(?:[02468][13579])*'
k = [len(x) for x in findall(r,s)]
a = '(?:[13579][02468])*'
j = [len(x) for x in findall(a,s)]
print(max(k),max(j))
