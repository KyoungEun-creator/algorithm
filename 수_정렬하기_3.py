# 10989: 수 정렬하기 3

'''
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 10001

for _ in range(N):
    num = int(input())
    arr[num] += 1
    # arr 안 elem의 값은 중요하지 않음 (그저 중복 횟수일 뿐)
    # 중요한 건 elem의 위치 index값
    # index값이 우리가 진짜로 원하는 입력받은 숫자와 같다!

for i in range(10001):
    # 그자리에 숫자가 있다면 == 인덱스가 존재한다면 == 입력받은 숫자라면
    if arr[i] != 0:
        # 인덱스에 해당하는 수를 출력한다
        for j in range(arr[i]):
            print(i)