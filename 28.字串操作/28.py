def main():
    s1, s2, w1, w2 = [input() for _ in range(4)]
    rew2 = ''
    for i in range(len(w2)-1, -1, -1):
        rew2 += w2[i]
    csentence = s1 + ' ' + s2
    c = list(map(str, (csentence).split()))
    d = list()
    f = list()
    print(' '.join(map(str, c)))
    for i in range(len(c)):
        if c[i].lower() == w1.lower():
            d.append(w2)
            f.append(rew2)
        else:
            d.append(c[i])
            f.append(c[i])
    print(' '.join(map(str, d)))
    clength = sum(len(i) for i in c)
    dlength = sum(len(i) for i in d)
    print(clength, dlength, sep = ' ')
    print(' '.join(map(str, f)))
    n = abs(len(w1)-len(w2))
    for i in range(0, len(csentence), n):
        print(csentence[i], end = '')

main()