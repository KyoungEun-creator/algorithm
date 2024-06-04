# 11050: 이항 계수 

# 자연수 (N\)과 정수 (K\)가 주어졌을 때 이항 계수 (\binom{N}{K}\)를 구하는 프로그램을 작성하시오.
# nCk = factorial(n) // factorial(n-k) * factorial(k)

import sys
N, K = map(int, sys.stdin.readline().split())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
       return n * factorial(n - 1)   

print(factorial(N) // (factorial(N-K) * factorial(K)))