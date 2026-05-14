f = open('26_15_23259.txt')
n, m = map(int, f.readline().split())
w = sorted([int(f.readline()) for i in range(n)])
c = sorted([int(f.readline()) for j in range(m)])
max_possible = max([x for x in w if x <= c[-1]])
k = 0
while w and c:
    if w[0] <= c[0]:
        w.pop(0)
        c.pop(0)
        k += 1
    else:
        w.pop(0)
print(k, max_possible)
