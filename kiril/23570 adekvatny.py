from collections import Counter
f = open('26_23570.txt')
n, k, = map(int, f.readline().split())
p = []
while n > 0:
    p.append(int(f.readline()))
    n -= 1
m = Counter(p)

models = dict()

while k > 0:
    power, price = map(int, f.readline().split())
    if power in models:
        models[power] = min(models[power], price)
    else:
        models[power] = price
    k -= 1

d = sorted(models.items(), key=lambda x: x[1])

tc = 0
pl = []
for rp, c in m.items():
    for model in d:
        if model[0] >= rp:
            tc += model[1] * c
            pl.append(model[0])
            break
print(tc, max(pl))
