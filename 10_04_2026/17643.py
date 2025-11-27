f = open('26_17643.txt').readlines()
N = int(f.pop(0))

items = dict()

for line in f:
    id, price, is_sold = [int(x) for x in line.split()]
    if id not in items:
        items[id] = [price, 0, 0]

    if is_sold:
        items[id][2] += 1
    else:
        items[id][1] += 1

summary = []

for item in items.values():
    summary.append(item[0])

avg = sum(summary) / len(summary)
expensive_items = dict()

for key, value in items.items():
    if value[0] > avg:
        expensive_items[key] = value

res = sorted(expensive_items.values(), key=lambda x: (-x[1], -x[0], x[2],))
print(res[0][0] * res[0][1], res[0][2])
