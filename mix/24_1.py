s = open('24_21.txt').readline()

k = 1
m_k = float('-inf')

for i in range(len(s) - 1):
    l, r = s[i], s[i + 1],
    if l != r:
        k += 1
    else:
        m_k = max(m_k, k)
        k = 1
print(m_k)
