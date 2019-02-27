import numpy as np

# AND gate
# 단층 퍼셉트론. 선형.
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    temp = np.sum(w * x) + b
    if temp <= 0:
        return 0
    else:
        return 1
print("AND gate")
print("x1\tx2\ty")
print("0\t0\t%d" % AND(0, 0))
print("0\t1\t%d" % AND(0, 1))
print("1\t0\t%d" % AND(1, 0))
print("1\t1\t%d\n" % AND(1, 1))

# NAND gate
# 단층 퍼셉트론. 선형.
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    temp = np.sum(x * w) + b
    if temp <= 0:
        return 0
    else:
        return 1
print("NAND gate")
print("x1\tx2\ty")
print("0\t0\t%d" % NAND(0, 0))
print("0\t1\t%d" % NAND(0, 1))
print("1\t0\t%d" % NAND(1, 0))
print("1\t1\t%d\n" % NAND(1, 1))

# OR gate
# 단층 퍼셉트론. 선형.
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    temp = np.sum(x * w) + b
    if temp <= 0:
        return 0
    else:
        return 1
print("OR gate")
print("x1\tx2\ty")
print("0\t0\t%d" % OR(0, 0))
print("0\t1\t%d" % OR(0, 1))
print("1\t0\t%d" % OR(1, 0))
print("1\t1\t%d\n" % OR(1, 1))

# XOR gate
# 다층 퍼셉트론. 비선형.
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
print("XOR gate")
print("x1\tx2\ty")
print("0\t0\t%d" % XOR(0, 0))
print("0\t1\t%d" % XOR(0, 1))
print("1\t0\t%d" % XOR(1, 0))
print("1\t1\t%d\n" % XOR(1, 1))