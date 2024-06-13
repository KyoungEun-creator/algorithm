# 10872: 팩토리얼

'''
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
첫째 줄에 N!을 출력한다.
'''

N = int(input())
res = 1

for i in range(1, N+1):
    res *= i
print(res)

# 재귀함수
'''
n = int(input())

def factorial(i):
    res = 1
    if i > 0:
        res = i * factorial(i - 1)
    return res

print(factorial(n))
'''