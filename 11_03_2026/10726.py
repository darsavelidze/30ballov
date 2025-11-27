f = open('26_10107.txt')
N = int(f.readline())

events = [list(map(int, x.split())) for x in f]

events = sorted(events, key=lambda x: x[1])

current = 0
viewed = []
for i in range(1, N):
    if events[i][0] >= events[current][1]:
        viewed.append(events[i])
        current = i

print(len(viewed) + 1)
