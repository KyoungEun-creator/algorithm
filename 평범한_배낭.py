# 12865: 평범한 배낭

'''
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 
해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
입력으로 주어지는 모든 수는 정수이다.

한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

thing = [[0, 0]]
d = [[0] * (K+1) for _ in range(N+1)]
# 2차원 리스트 d가 (n+1) x (k+1) 크기로 0으로 초기화된 형태

for i in range(N):
    thing.append(list(map(int, input().split())))
# print(thing): [[0, 0], [6, 13], [4, 8], [3, 6], [5, 12]]

for i in range(1, N+1): # 물건 하나씩
    for j in range(1, K+1): # 1 ~ K까지 무게 
        W = thing[i][0]
        V = thing[i][1]

        if j < W: 
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-W]+V)

print(d[N][K])