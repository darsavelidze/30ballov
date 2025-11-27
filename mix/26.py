pairs = []

for x in range(1, 100000):
    y = 78125 - 4 * x
    if y < 0:
        break
    pair = [y, x]
    pairs.append(pair)

print(max(pairs))