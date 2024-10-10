# 10872: 팩토리얼

'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

출력
첫째 줄에 N!을 출력한다.
'''

# 241009
N = int(input())
res = 1

for i in range(N, 1, -1):
    res *= i
    
print(res)

# old
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