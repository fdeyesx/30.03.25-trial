def k(n):
    s = str(n).replace(',','.')
    p = s.find('.')
    s1 = int(s[:p])
    s2 = int(s[p + 1:]) / (10 ** len(s[p + 1:]))
    sum1 = s1+s2
    return sum1

def f(x1,y1,x2,y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def main(k,x1,x2,y1,y2):
    mn = 10**10
    cx = 0
    cy = 0
    for i in range(len(k)):
        s = 0
        tx,ty = k[i][0], k[i][1]
        if x1 <= tx <= x2:
            if y1 <= ty <= y2:
                for j in range(len(k)):
                    dx, dy = k[j][0], k[j][1]
                    if x1 <= dx <= x2:
                        if y1 <= dy <= y2:
                            s += f(tx, ty, dx, dy)
                        if s < mn:
                            mn = s
                            cx = tx
                            cy = ty
        return [cx, cy, mn]


s = open('27_B.txt').readlines()
s.remove(s[0])
s = list(s)
stlist = []
for m in range(0,len(s)):
    o = s[m].split()
    stlist.append([k(o[0]),k(o[1])])

k1 = main(stlist, -4, 3, 2, 8)
k2 = main(stlist, 0, 8, 2, -4)
k3 = main(stlist, 4, 12, 2, 9)

print(k1,k2,k3)