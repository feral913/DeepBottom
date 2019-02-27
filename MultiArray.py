import sys
import numpy as np

# 1차원 배열
print("1차원 배열 A")
A = np.array([1, 2, 3, 4])
print("A = %s" % A)
print("배열의 차원 수 : %d" % np.ndim(A))
sys.stdout.write("배열의 형상 : ")
print(A.shape)
print("A.sape[0] : %d" % A.shape[0])
print()

# 2차원 배열
print("2차원 배열 B")
B = np.array([[1, 2], [3, 4], [5, 6]])
print("B = %s" % B)
print("배열의 차원 수 : %d" % np.ndim(B))
sys.stdout.write("배열의 형상 : ")
print(np.shape(B))
print()

# 행렬의 곱
# 행렬의 곱은 numpy의 dot() 함수로 계산한다.
# 2x2 행렬 간의 곱
A = np.array([[1, 2], [3, 4]])
print("A = %s" % A)
B = np.array([[5, 6], [7, 8]])
print("B = %s" % B)
sys.stdout.write("A의 형상 : ")
print(np.shape(A))
sys.stdout.write("B의 형상 : ")
print(np.shape(B))
print("A * B = %s" % np.dot(A, B))
print()
# 2x3 행렬과 3x2 행렬의 곱
A = np.array([[1, 2, 3], [4, 5, 6]])
print("A = %s" % A)
B = np.array([[1, 2], [3, 4], [5, 6]])
print("B = %s" % B)
sys.stdout.write("A의 형상 : ")
print(np.shape(A))
sys.stdout.write("B의 형상 : ")
print(np.shape(B))
print("A * B = %s" % np.dot(A, B))
print()
# 3x2 행렬과 2x1 행렬의 곱
A = np.array([[1, 2], [3, 4], [5, 6]])
print("A = %s" % A)
B = np.array([7, 8])
print("B = %s" % B)
sys.stdout.write("A의 형상 : ")
print(np.shape(A))
sys.stdout.write("B의 형상 : ")
print(np.shape(B))
print("A * B = %s" % np.dot(A, B))

