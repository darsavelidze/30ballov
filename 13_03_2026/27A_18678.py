from math import dist


def get(data, r):
    clusters = []
    while data:
        clusters.append(cluster := [data.pop(0)])
        [cluster.append(p) or data.remove(p) for core in cluster for p in data if dist(core, p) < r]
    return clusters


points = [list(map(float, line.replace(',', '.').split())) for line in open('27A_18678.txt')]
clusters = [x for x in get(points, 0.3) if len(x) > 10]
c1, c2 = clusters


def find_mid(cluster):
    dists = []
    for p1 in cluster:
        su = 0
        for p2 in cluster:
            su += dist(p1, p2)
        dists.append([su, p1])

    m = min(dists)
    return m[1]


for x in clusters:
    print(find_mid(x))