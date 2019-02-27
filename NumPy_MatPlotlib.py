# 표준 python에 포함되지 않는 외부 라이브러리 호출 및 활용
import sys
import numpy as np

# numpy 배열
print("#numpy 배열#")
x = np.array([1.0, 2.0, 3.0])
print("numpy 배열 x : %s" % x)
print("Type of x : %s" % type(x))
print()

# numpy 산술 연산
print("#numpy 산술 연산#")
# 원소 수가 같을 때
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print("x : %s" % x)
print("y : %s" % y)
print("x + y : %s" % (x + y))
print("x - y : %s" % (x - y))
print("x * y : %s" % (x * y))
print("x / y : %s" % (x / y))
# 원소 수가 다를 때 - 브로드캐스트
print("x / 2.0 : %s" % (x / 2.0))
print()

# numpy의 N 차원 배열
print("#numpy의 N 차원 배열#")
A = np.array([[1, 2], [3, 4]])
print("A = %s" % A)
sys.stdout.write("Shape of A : ")
print(A.shape)
print("Type of A : %s" % A.dtype)
B = np.array([[3, 0], [0, 6]])
print("B = %s" % B)
print("A + B : %s" % (A + B))
print("A * B : %s" % (A * B))
# 브로드캐스트
print("A * 10 : %s" % (A * 10))
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print("A = %s" % A)
print("B = %s" % B)
print("A * B = %s" % (A * B))
# 원소 접근
X = np.array([[51, 55],[14, 19], [0, 4]])
print("X = %s" % X)
print("X[0] : %s" % X[0])
print("X[0][1] : %s" % X[0][1])
print("X : ")
for row in X:
    print(row)
# 다차원 배열을 1차원 배열로 변환(평탄화)
X = X.flatten()
print("X.flatten : %s" % X)
print("X[np.array([0, 2, 4])] : %s" % X[np.array([0, 2, 4])])
print("X > 15 : %s" % (X > 15))
print("X[X > 15] : %s" % (X[X > 15]))
print()

# 그래프 그리기
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 생성
y1 = np.sin(x)

plt.plot(x, y1)
#plt.show()

plt.figure() # create new figure
y2 = np.cos(x)
plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle = "--", label = "cos") # 점선
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title('sin & cos') # 제목
plt.legend() # 범례
#plt.show()

# 이미지 표시하기
from matplotlib.image import imread

img = imread('Lenna.png')

plt.figure()
plt.imshow(img)
plt.show()