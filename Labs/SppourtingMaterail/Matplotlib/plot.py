import numpy as np
import matplotlib.pyplot as plt

x = list(range(10))
for i in range(10):
    plt.plot(x, np.random.rand(10), linewidth=1, label=f'Line {i+1}')

plt.title("Too Much Data Can Be Confusing!")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.tight_layout()
plt.show()
