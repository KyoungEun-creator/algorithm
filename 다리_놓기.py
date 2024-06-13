# 1010: 다리 놓기

'''
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)이 주어진다.
각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력한다.
'''

import sys
input = sys.stdin.readline

T = int(input())

def factorial(i):
    res = 1
    if i > 0:
        res = i * factorial(i - 1)
    return res

for _ in range(T):
    N, M = map(int, input().split())
    res = factorial(M) // (factorial(M-N) * factorial(N))
    print(res)

# m개의 지역에 n개의 다리를 놓을 수 있는 경우의 수 mCn
# mCn = m! // (m-n)!n! 