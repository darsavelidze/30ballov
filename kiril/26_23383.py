f = open('26_23383.txt')
n = f.readline()
d = dict()
for line in f:
    s, c = map(int, line.split())
    if c not in d.keys():
        d[c] = [s]
    else:
        d[c] = sorted(set(d[c] + [s]))
res = []
for i in d.items():
    c, l, = i
    m = float('-inf')
    k = 1
    for j in range(len(l) - 1):
        if l[j + 1] - l[j] == 1:
            k += 1
            m = max(m, k)
        else:
            k = 1
    res.append((i[0], m))
res = sorted(res, key=lambda x: (-x[1], x[0]))
print(res[0])
