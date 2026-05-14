f = open('26_23383.txt')
n = f.readline()
f_2 = sorted([list(map(int, line.split())) for line in f], key=lambda x: x[0])
d = dict()
for s, c in f_2:
    if c not in d.keys():
        d[c] = [1, s, 1]
    elif s - d[c][1] == 1:
        m = max(d[c][0] + 1, d[c][2])
        d[c] = [d[c][0] + 1, s, m]
    elif s - d[c][1] == 0:
        pass
    else:
        d[c] = [1, s, d[c][2]]
res = sorted([[a[0], a[1][2]] for a in d.items()], key=lambda x: (-x[1], x[0]))
print(res[0])
