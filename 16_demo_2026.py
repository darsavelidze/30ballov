cache_g = [-1] * 20000

def g(n):
    if cache_g[n] != -1:
        return cache_g[n]
    if n < 10:
        return 2 * n
    else:
        return g(n - 2) + 1


def f(n):
    return 2 * (g(n - 3) + 8)


for i in range(1, 20000):
    cache_g[i] = g(i)

print(f(15548))
