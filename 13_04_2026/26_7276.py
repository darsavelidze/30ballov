f = open('26_7276.txt').readlines()
l,n = [int(x) for x in f.pop(0).split()]
planes = []
for line in f:
    if [int(x) for x in line.split()]:
        planes.append([int(x) for x in line.split()])
planes_sorted = sorted(planes, key = lambda x: (x[1], x[0]))
c = [planes_sorted[0]]
for i in range(n-1):
    if c[-1][1] <= planes_sorted[i+1][0]:
        c.append(planes_sorted[i+1])
    else:
        continue
print(len(c), c[-1][0])