f = open('26_8432.txt')
N = 888
t = []
light_auto = [-1] * 70
mini_bus = [-1] * 30


for l in f:
    arrived, required_time, type = [x for x in l.split()]
    t.append([int(arrived), int(arrived)+int(required_time), type])

t = sorted(t)

c_1 = 0
c_2 = 0
for auto in t:
    if auto[2] == 'B':
        parked = False
        for i in range(len(mini_bus)):
            if mini_bus[i] <= auto[0]:
                mini_bus[i] = auto[1]
                parked = True
                c_1 +=1
                break
        if not parked:
            c_2 += 1
    if auto[2] == 'A':
        parked = False
        for i in range(len(light_auto)):
            if light_auto[i] <= auto[0]:
                light_auto[i] = auto[1]
                parked = True
                break
        if not parked:
            for i in range(len(mini_bus)):
                if mini_bus[i] <= auto[0]:
                    mini_bus[i] = auto[1]
                    parked = True
                    break
        if not parked:
            c_2+=1
print(c_1, c_2)