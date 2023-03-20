import numpy as np

def softmax(a):
    c = np.max(a)
    y = np.exp(a - c) / np.sum(np.exp(a - c))
    
    return y

a = np.array([1010, 1000, 990])
print(softmax(a))