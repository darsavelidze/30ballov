a = True
b = True
c = False


f = a or b <= c
f1 = (a or b) <= c
f2 = a or (b <= c)
print(f)
print(f1, f2)