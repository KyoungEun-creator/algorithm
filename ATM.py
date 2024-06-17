# 11399: ATM

'''
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.
'''

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

# 오름차순 정렬
P.sort()

ans = 0

for i in range(1, N+1):
    ans += sum(P[0:i])

print(ans)


# 방법2
'''
current = 0
sum_val = 0
for time in P:
    current += time
    sum_val += current

print(sum_val)
'''