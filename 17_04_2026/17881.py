f = open('26_17881.txt')

N = int(f.readline())
good = []
bad = []
for line in f:
    ID, *rates = [int(x) for x in line.split()]
    if rates.count(2) == 0:
        good.append([ID, sum(rates) / 4])
    else:
        bad.append([ID, rates.count(2)])

good = sorted(good, key=lambda x: (-x[1], x[0]))
bad = sorted(bad, key=lambda x: (x[1], x[0]))

# print((len(good) + len(bad)) * 0.25)
print(good[2490][0])
for x in bad:
    if x[1] == 3:
        print(x[0])
        break
