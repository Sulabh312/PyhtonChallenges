import numpy as np, time, math
tau = 0.5
t_value = np.arange(0, 3.01, 0.01)
ls = []

for t in t_value:
    y = 1 - math.e**(-t / tau)
    ls.append((t, y))
target = 0.63
for t, y in ls:
    if y >= target:
        print(f"{target} is reached at t = {t:.2f} seconds")
        break