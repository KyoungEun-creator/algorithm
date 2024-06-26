# 1003: 피보나치 함수

'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. 
N은 40보다 작거나 같은 자연수 또는 0이다.

각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
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