f = open('24_17563.txt').readline()
mode = 'znak'
max_k = float('-inf')
k = 0
i = 0
while i < (len(f) - 1):
    if mode == 'znak':
        while f[i] not in '789' and i in range(len(f) - 1):
            i += 1
        mode = 'num'
    else:
        while i < len(f) - 1 and f[i] not in '-*':
            k += 1
            i += 1
        if i < len(f) - 1  and f[i + 1] in '-*0':
            max_k = max(k, max_k)
            k = 0
            mode = 'znak'
        else:
            k += 1
            i += 1
print(k)
