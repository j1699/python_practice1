import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x) #maximum함수는 둘 중 큰 값을 출력하는 함수

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 5.1)
plt.show()