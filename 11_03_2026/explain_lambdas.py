def sorting(x, action):
    for i in range(len(x)):
        for j in range(0, len(x) - 1):
            if action(x[j]) > action(x[j + 1]):
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


print(sorting(["11", 'kdfkdfj', 'sadfk', '222'], lambda x: x[1]))
