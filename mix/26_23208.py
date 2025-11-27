from Tools.scripts.fixcid import Reverse

f = open('26_23208.txt')
N = 970
end = []
start = []
details = []
for i, l in enumerate(f,1):
    a, b = [int(x) for x in l.split()]
    d = [[a, 's', i], [b, 'o', i]]
    if a < b:
        start.append([a,i])
    else:
        end.append([b,i])

start.sort()
end.sort(reverse=True)
r = start + end
print(r)
print(len(start))
print(r[len(start) + 1])