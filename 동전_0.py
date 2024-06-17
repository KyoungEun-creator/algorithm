# 11047: 동전 0

'''
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 동전의 가치 Ai 리스트
coins = []

for i in range(0, N):
    coins.append(int(input()))

# K원을 만드는데 필요한 동전 개수
num = 0

for coin in reversed(coins):
    if K >= coin:
        num += (K // coin)
        K %= coin

print(num)