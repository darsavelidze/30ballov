points = [list(map(float, line.replace(',', '.').split())) for line in open('27B_18678.txt')]
from math import dist
def get(data, r):
    clusters = []
    while data:
        clusters.append(cluster := [data.pop(0)])
        [cluster.append(p) or data.remove(p) for core in cluster for p in data if dist(core,p) < r]
    return clusters
c1,c2,c3 = [x for x in get(points, 0.5) if len(x) > 100]

anton = []
for p1 in c1:
    nikitos = 0
    for p2 in c1:
        nikitos+=dist(p1,p2)
    anton.append([nikitos,p1])
center1 = min(anton)[1]
print(anton)
print(center1)
