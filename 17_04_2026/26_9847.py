f = open('26_9847.txt')
N = int(f.readline())

minutes = [0] * (24 * 60 + 1)
for line in f:
    start, end = map(int, line.split())
    minutes[start] += 1
    minutes[end] -= 1

for i in range(1, len(minutes)):
    minutes[i] += minutes[i - 1]


print('643 643' in ' '.join(map(str, minutes)))
print(' '.join(map(str, minutes)).count('643 643'))
