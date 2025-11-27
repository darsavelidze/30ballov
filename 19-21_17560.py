def f(s, m):
    if s >= 58: # Условие победы
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 1, m - 1), f(s + 4, m - 1), f(s * 2, m - 1)] # Вариации ходов
    if m % 2 != 0:
        return any(h)
    else:
        return all(h) # Если после неудачного хода Пети то any

print([x for x in range(1, 58) if f(x, 2)]) # Меняем только исходное кол камней
print([x for x in range(1, 58) if not f(x, 1) and f(x, 3)])
print([x for x in range(1, 58) if not f(x, 2) and f(x, 4)])
