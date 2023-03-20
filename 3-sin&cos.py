import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 6, 0.1)
y1 = np.sin(x) / 2 + 0.5
y2 = np.cos(x)
plt.plot(x, y1, label="normalized")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(0,8,1)
plt.legend()
plt.show()