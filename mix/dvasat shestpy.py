f = open('26_25363.txt')
N = int(f.readline())
s = [list(map(int, x.split())) for x in f]

gen = []
k = 1
left = []
right = []
for pause, active, in s:
    if pause < active:
        gen.append([pause, k, 1])
    else:
        gen.append([active, k, 2])
    k += 1
gen = sorted(gen)
last = -1
for x in gen:
    time, num, typ = x
    if typ == 1:
        left.append(num)
    if typ == 2:
        right.append(num)
    last = num

res = left + right[::-1]
print(last)
print(N - res.index(last) - 1)