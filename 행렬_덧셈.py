# 2738: 행렬 덧셈

# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 
# 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. (M * N)
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. (M * N)
# N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

N, M = map(int, input().split())

A = [
    list(map(int, input().split()))
    for _ in range(N)
]

B = [
    list(map(int, input().split()))
    for _ in range(N)
]

# 정답을 담을 행렬 0으로 초기화
answer = [
    [0 for _ in range(M)]
    for _ in range(N)
]

for i in range (N):
    for j in range (M):
        answer[i][j] = A[i][j] + B[i][j]

for row in answer:
    for elem in row:
        print(elem, end= " ")
    print()