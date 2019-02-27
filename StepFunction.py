# a = b + w1x1 + w2x2
# y = h(a) = 0 (a <= 0), 1 (a > 0)

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype = np.int)

x = np.arange(-5, 5, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.show()