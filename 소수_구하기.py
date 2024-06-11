# 1929: 소수 구하기

'''
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. 
(1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''

# 시간복잡도 똥망..
'''
M, N = list(map(int, input().split()))
li = []

for i in range(M, N+1):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        li.append(i)

for elem in li:
    print(elem)
'''

import math

M, N = list(map(int, input().split()))

def is_prime(i):
    if i == 1: 
        return False
    # 2부터 제곱근까지 확인
    for j in range(2, int(math.sqrt(i)+1)): 
        if i % j == 0: 
            return False
    else: 
        print(i)

for i in range(M, N+1):
    is_prime(i)