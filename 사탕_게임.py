# 3085: 사탕 게임

'''
입력
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

출력
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
'''

N = int(input())

arr = []
candy = 0
for _ in range(N):
    # array.append(list(map(str, input().split()))) # [['CCP'], ['CCP'], ['PPC']]
    arr.append(list(input().strip())) # [['C', 'C', 'P'], ['C', 'C', 'P'], ['P', 'P', 'C']]
    # arr = [list(input().strip()) for _ in range(N)]


# 가장 긴 '연속된' 사탕 개수를 찾는 함수
def count_candy():
    max_cnt = 1

    for i in range(N):
        row_cnt, col_cnt = 1, 1 # 행, 열 안에서 연속되는 것의 개수
        for j in range(1, N): 
            if arr[i][j] == arr[i][j-1]:
                row_cnt += 1
            else:
                max_cnt = max(max_cnt, row_cnt)
                row_cnt = 1  # 초기화
            if arr[j][i] == arr[j-1][i]:
                col_cnt += 1
            else:
                max_cnt = max(max_cnt, col_cnt)
                col_cnt = 1  # 초기화
        max_cnt = max(max_cnt, row_cnt, col_cnt)
    return max_cnt

# 인접한 사탕을 교환하면서 최대 개수 찾기
max_candy = count_candy()  # 초기 상태에서 최댓값 확인

for i in range(N):
    for j in range(N - 1):
        # 오른쪽과 교환 (가로)
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        # 최댓값 갱신
        max_candy = max(max_candy, count_candy())
        # 원래대로 
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        # 아래쪽과 교환 (세로)
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
        # 최댓값 갱신
        max_candy = max(max_candy, count_candy())
        # 원래대로 
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
        
print(max_candy) 