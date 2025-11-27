from math import dist


def get_clusters(data, epsilon):
    clusters = []
    while data:
        clusters.append(cluster := [data.pop(0)])
        [cluster.append(p) or data.remove(p) for core in cluster for p in data if dist(core, p) < epsilon]
    return clusters


def find_mid(cluster):
    min_count = 1000000
    middle = []
    for point in cluster:
        count = 0
        array = cluster.copy()
        array.remove(point)
        for dif_points in array:
            count += ((point[0] - dif_points[0]) ** 2 + (point[1] - dif_points[1]) ** 2) ** 0.5
        if count < min_count:
            min_count = count
            middle = point
    return middle


points = [list(map(float, line.replace(',', '.').split())) for line in open('27B_18678.txt')]
clusters = [x for x in get_clusters(points, 1.3) if len(x) > 50]

first_cluster = find_mid(clusters[0])
second_cluster = find_mid(clusters[1])
third_cluster = find_mid(clusters[2])

print((first_cluster[0] + second_cluster[0] + third_cluster[0]) / 3 * 100000,
      (first_cluster[1] + second_cluster[1] + third_cluster[1]) / 3 * 100000)