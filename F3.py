# 3층 신경망

import numpy as np

X = np.array([1, 0.5])

# 1층
# Input : X, Weight : W1, Bias : B1, Activation Function : Sigmoid
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# np.dot : 행렬 곱셈.
A1 = B1 + np.dot(X, W1)
Z1 = sigmoid(A1)

print(A1)
print(Z1)

# 2층
# Input : Z1, Weight : W2, Bias : B2, AF : Sigmoid
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

A2 = B2 + np.dot(Z1, W2)
Z2 = sigmoid(A2)

print(A2)
print(Z2)
