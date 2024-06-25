# 9095: 1, 2, 3 더하기

'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
'''

import sys
input = sys.stdin.readline

T = int(input())

'''
arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, 11):
    arr[i] = arr[i-3] + arr[i-2] + arr[i-1]

for _ in range(T):
    n = int(input())
    print(arr[n])
'''

# 방법2
def count(n):
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):
        if i >= 1:
            dp[i] += dp[i-1]
        if i>= 2:
            dp[i] += dp[i-2]
        if i >= 3:
            dp[i] += dp[i-3]
    return dp[n]

for _ in range(T):
    n = int(input())
    print(count(n))