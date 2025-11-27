f = open('26_27779.txt')
N = int(f.readline())
s = [int(x) for x in f]

s = sorted(s, key=lambda x: -x)

accepted = [s.pop(0)]

for i in range(N - 1):
    if accepted[-1] - s[i] >= 8:
        accepted.append(s[i])

print(len(accepted))
print(accepted[-1])
