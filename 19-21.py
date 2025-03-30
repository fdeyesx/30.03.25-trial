def f(s,e):
    if s <= 19: return e%2 == 0
    if e == 0: return 0
    k = [f(s-4,e+1),f(s-6,e+1),f(s//2,e+1)]
    return any(k) if e%2 != 0 else all(k)

print('19:', [s for s in range(100,200) if not f(s,1) and f(s,2)])
print('20:', [s for s in range(100,200) if not f(s,1) and f(s,3)])
print('21:', [s for s in range(20,200) if not f(s,2) and f(s,4)])
