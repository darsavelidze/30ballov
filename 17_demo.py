f = open('17_23757.txt')
s = [int(x) for x in f]

m_2 = min([x for x in s if 10 <= x < 100])

sums = []

for i in range(0, len(s) - 1):
    a, b = s[i], s[i + 1],
    cond_1 = (10 <= a < 100) + (10 <= b < 100)
    if cond_1 == 1 and (a + b) % m_2 == 0:
        sums.append(a + b)

print(len(sums), max(sums))