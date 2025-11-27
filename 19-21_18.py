def f(s1, s2, m):
    if s1 + s2 >= 77:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1 + 1, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 * 2, m - 1)]
    if m % 2 != 0:
        return any(h)
    else:
        return all(h)


print([x for x in range(1, 78) if f(7, x, 2)])
print([x for x in range(1, 78) if not f(7, x, 1) and f(7, x, 3)])
print([x for x in range(1, 78) if not f(7, x, 2) and f(7, x, 4)])
