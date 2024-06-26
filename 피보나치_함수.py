# 1003: 피보나치 함수

'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. 
N은 40보다 작거나 같은 자연수 또는 0이다.

각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
'''

# 패턴
'''
zero = [1, 0, 1, 1, 2, 3, 5, 8, 13, 21, ...] => 피보나치
one = [0, 1, 1, 2, 3, 5, 8, 13, 21, 24, ...] => 피보나치

# 각자 피보나치 수열을 따름을 확인할 수 있음!
'''

# 방법1
'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = 1, 0
    N = int(input())
    for _ in range(N):
        a, b = b, a + b 
    print(a, b)
'''

# 방법2
import sys
input = sys.stdin.readline

T = int(input())

zero = [0] * 41
one = [0] * 41

# f(0)
zero[0], one[0] = 1, 0 
# f(1)
zero[1], one[1] = 0, 1

def fibo(n):
    for i in range(2, n+1):
        zero[i] = zero[i-2] + zero[i-1]
        one[i] = one[i-2] + one[i-1]
    return zero[n], one[n]

for _ in range(T):
    N = int(input())
    z, o = fibo(N)
    print(z, o)