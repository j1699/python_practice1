import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 6, 0.1) # np.arange(a, b, c)에서 a는 시작값, b는 끝값, c는 간격을 의미한다.
y = np.sin(x)
plt.plot(x, y)
plt.show()