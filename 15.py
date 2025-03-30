for a in range(0,500):
    d = set()
    for x in range(0,1000):
        for y in range(0,1000):
            f = ((x+2*y) < a) or (y > x) or (x > 60)
            d.add(f)
    if False not in d:
        print(a)
        break
