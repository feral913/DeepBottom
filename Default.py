# 산술 연산
print("#산술 연산#")
print("1 - 2 = %d" % (1 - 2))
print("4 * 5 = %d" % (4 * 5))
# python2에서 정수끼리의 계산 결과는 정수
# python3에서 정수끼리의 계산 결과에서도 부동소수점 출력
print("7 / 5 = %.2f" % (7 / 5))
# ** : 거듭 제곱
print("3 ** 2 = %d" % (3 ** 2))
print()

# 자료형
# python에서는 type() 함수로 특정 데이터의 자료형을 알아볼 수 있다.
print("#자료형#")
print("Type of 10 : %s" % type(10))
print("Type of 2.718 : %s" % type(2.718))
print("Type of hello : %s" % type("hello"))
print()

# 변수
# python은 동적 언어이다. 변수의 자료형을 상황에 맞게 자동으로 결정한다.
print("#변수#")
x = 10
print("x = %d" % x)
x = 100
print("x = %d" % x)
y = 3.14
print("y = %.2f" % y)
print("x * y = %d" % (x * y))
print("Type of (x * y) : %s" % type(x * y))
print()

# 리스트
print("#리스트#")
a = [1, 2, 3, 4, 5]
print("리스트 a : %s" % a)
print("리스트 a의 길이 : %d" % len(a))
print("리스트 a의 첫 원소 : %d" % a[0])
print("리스트 a의 다섯 번째 원소 : %d" % a[4])
a[4] = 99
print("리스트 a의 다섯 번째 원소에 다른 값 대입 : %s" % a)
# python에서는 슬라이싱을 이용하여 범위를 지정해 원하는 부분 리스트를 얻을 수 있다.
# 첫 원소(인덱스 0)부터 두개
print("a[0:2] : %s" % a[0:2])
# 두 번째 원소(인덱스 1)부터 끝까지
print("a[1:] : %s" % a[1:])
# 처음부터 세개
print("a[:3] : %s" % a[:3])
# 처음부터 마지막 원소의 1개 앞까지 (뒤에서 한 개 빼기)
print("a[:-1] : %s" % a[:-1])
# 처음부터 마지막 원소의 2개 앞까지 (뒤에서 두 개 빼기)
print("a[:-2] : %s" % a[:-2])
print()

# 딕셔너리
# key와 value를 한 쌍으로 저장한다.
print("#딕셔너리#")
me = {'height' : 180}
print("me[height] : %d" % me['height'])
# 새 원소 추가
me['weight'] = 70
print(me)
print()

# bool
print("#bool#")
hungry = True
sleepy = False
print("Type of 'hungry' : %s" % hungry)
print("Type of 'not hungry' : %s" % (not hungry))
print("Type of 'hungry and sleepy' : %s" % (hungry and sleepy))
print("Type of 'hungry or sleepy' : %s" % (hungry or sleepy))
print()

# if
print("#if#")
hungry = True
if hungry:
    print("I'm hungry")

hungry = False
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")
    print("I'm sleepy")
print()

# for
print("#for#")
for i in [1, 2, 3]:
    print(i)
print()

# 함수
print("#함수#")
def hello():
    print("Hello World!")
hello()

def hello2(object):
    print("Hello " + object + "!")
hello2("cat")
print()

# class
print("#class#")
class Man:
    # 클래스 초기화 메서드(생성자, constructor).
    # 클래스의 인스턴스가 만들어질 때 한 번만 불린다.
    # python에서는 메서드의 첫 번째 인수로 자신(자신의 인스턴스)를 나타내는 self를 명시적으로 쓰는 것이 특징이다.
    # 인스턴스 변수(self.~)는 인스턴스별로 저장되는 변수이다.
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()
