f = open('26_23570.txt')
N, K = map(int, f.readline().split())

min_powers = dict()
models = []

for i in range(N):
    model_power = int(f.readline())
    if model_power in min_powers:
        min_powers[model_power] += 1
    else:
        min_powers[model_power] = 1

for i in range(K):
    model = [int(x) for x in f.readline().split()]
    models.append(model)

models = sorted(models, key=lambda x: (x[1], -x[0]))

res_price = 0
m = -10 ** 10
for area_power, count_models in min_powers.items():
    for model_power, price in models:
        if model_power >= area_power:
            res_price += count_models * price
            m = max(model_power, m)
            break

print(res_price, m)
