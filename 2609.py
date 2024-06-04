# title: 최대공약수와 최소공배수

# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

a, b = map(int, input().split())

# 최대 공약수 x
x = 0
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        x = i
print(x)

# Greatest Common Divisor
# import math
# print(math.gcd(a, b))

# 최소 공배수 y
# 최소공배수는 두 수 a와 b의 곱을 최대공약수로 나눈 값과 같다.
y = int((a * b) / x)
print(y)


