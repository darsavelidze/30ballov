s = open('24_17563.txt').readline()
n = len(s)

r = ['**', '--', '.-', '.*', '*.', '-.', '*-', '-*', '..']

while any([x in s for x in r]):
    for x in r:
        s = s.replace(x, '.')

m = s.split('.')
m = [x for x in m if '-0' not in x and '*0' not in x]
m = sorted(m, key=len)
print(len(m[-1]))