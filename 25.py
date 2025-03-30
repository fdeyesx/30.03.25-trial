for n in range(178965,178982+1):
    d = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            d.append(i)
            d.append(n//i)
    if len(d) == 4:
        d = sorted(d)
        d = d[::-1]
        print(d[0], d[1], d[2], d[3])
