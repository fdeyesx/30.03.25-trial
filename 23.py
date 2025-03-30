def f(s,e):
    if s == e: return 1
    if s > e: return 0
    return f(s+1,e) + f(s+3,e) + f(s*3,e)

print(f(3,9) * f(9,27) * f(27,31))
