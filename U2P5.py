import numpy as np, matplotlib.pyplot as plt

a3 = -2
a2 = 1 - a3
a1, a0 = 0, 0 

t_val = np.round(np.arange(0, 1.1, 0.1),2)
for t in t_val:
    print(f"{t}\t{np.polyval([a3, a2, a1, a0], t)}")

plt.plot(t_val, [x(t) for t in t_val])
plt.xlabel("Time (t)")
plt.ylabel("Position x(t)")
plt.title("Cubic Trajectory")
plt.grid(True)
plt.show()