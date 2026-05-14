f = open('26_1_23545.txt')
n, k, = map(int, f.readline().split())
p = []
m = []
while n > 0:
    p.append(int(f.readline()))
    n -= 1
while k > 0:
    m.append(list(map(int, f.readline().split())))
    k -= 1

m = sorted(m, key=lambda x: (x[1], -x[0]))
tp = list()
tc = 0
for rp in p:
    for model in m:
        if model[0] >= rp:
            tp.append(model[0])
            tc += model[1]
            break
print(max(tp), tc)
