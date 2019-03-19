import numpy as np
import matplotlib.pylab as plt

# 계단 함수. Step function.
# a = b + w1x1 + w2x2
# y = h(a) = 0 (a <= 0), 1 (a > 0)
def step_function(x):
    return np.array(x > 0, dtype = np.int)

x = np.arange(-5, 5, 0.1)
y1 = step_function(x)
plt.plot(x, y1)
#plt.show()

# Sigmoid Function.
# h(x) = 1 / 1 + exp(-x)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

y2 = sigmoid(x)
plt.figure()
plt.plot(x, y2)
#plt.show()

# ReLU(Rectified Linear Unit) Function.
# h(x) = x (x > 0), 0 (x <= 0)
def relu(x):
    return np.maximum(0, x)

y3 = relu(x)
plt.figure()
plt.plot(x, y3)
plt.show()

# Identity Function
# h(x) = x
def identity_function(x):
    return x

# Softmax Function
# y_{k} = exp(a_{k}) / sum_{i=1}^{n} exp(a_{i})
# y_{k} = exp(a_{k} - c) / sum_{i=1}^{n} exp(a_{i} - c)
# c는 입력값 중 최대값. exp(a)로 인한 오버플로우를 막기 위해
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
