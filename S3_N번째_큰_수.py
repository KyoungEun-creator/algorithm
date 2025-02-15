# 2075: S3_N번째 큰 수

'''
N×N의 표에 수 N2개 채워져 있다. 
채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다.
이러한 표가 주어졌을 때, N번째 큰 수를 찾는 프로그램을 작성하시오. 표에 채워진 수는 모두 다르다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,500)이 주어진다. 
다음 N개의 줄에는 각 줄마다 N개의 수가 주어진다. 
표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수이다.

출력
첫째 줄에 N번째 큰 수를 출력한다.
'''

import sys
import heapq

N = int(sys.stdin.readline())
min_heap = []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for num in row:
        if (len(min_heap) < N):
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

print(min_heap[0])