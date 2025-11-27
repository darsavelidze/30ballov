cache = [-1] * 200000


def f(n):
    if cache[n] != -1:
        return cache[n]
    if n <= 10:
        return n
    else:
        return n - 7 + f(n - 21)


for i in range(1, 200000):
    cache[i] = f(i)

print((f(185734) - f(185650)) // f(40))
