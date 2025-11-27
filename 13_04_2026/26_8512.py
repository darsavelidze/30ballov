f = open('26_8512.txt').readlines()
k = int(f.pop(0))
n = int(f.pop(0))
plans = [[int(x) for x in l.split()] for l in f if [int(x) for x in l.split()]]
plans_sorted = sorted(plans, key=lambda x:(x[0],x[1]))
y = []
for i in range(k):
    y.append(-1)
c = 0
last = None
for j in range(n):
    for i in range(k):
        if plans_sorted[j][0]>y[i]:
            y[i]=plans_sorted[j][1]
            c+=1
            last = i+1
            break
print(c, last)
