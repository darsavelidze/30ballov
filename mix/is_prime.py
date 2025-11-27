x = int(input())
flag = True

for i in range(2, x // 2):
    if x % i == 0:
        flag = False

if flag:
    print("YES")
else:
    print("NO")