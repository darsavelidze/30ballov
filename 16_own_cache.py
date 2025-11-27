cache = [-1] * 10000


def f(n):
    if cache[n] != -1:
        return cache[n]
    if n < 10:
        return n
    else:
        return 3 * n + f(n - 3)


for i in range(1, 10000):
    cache[i] = f(i)

print((f(6250) + 2 * f(6244)) / f(6238))
