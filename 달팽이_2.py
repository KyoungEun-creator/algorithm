# 1952: 달팽이2

'''
입력
첫째 줄에 M과 N이 빈 칸을 사이에 두고 주어진다. (2 ≤ M, N ≤ 100)

출력
첫째 줄에 표의 모든 칸이 채워질 때까지 선이 꺾어지는 횟수를 출력한다.
'''

M, N = list(map(int, input().split()))

route = [["?"] * N for _ in range(M)]

# snail 배열을 ?로 초기화하고, (0, 0)에서 시작
# 방향을 유지하면서 한 칸씩 이동
# 이동 불가능한 칸(벽, 이미 방문한 곳)을 만나면 방향을 바꾸고 num을 증가
# 모든 칸을 방문하면 num 출력: cnt가 M * N와 같게 되면? 칸 전부를 훑었을 때 '?'가 더이상 없으면?

# "오른쪽 → 아래 → 왼쪽 → 위쪽" 순서로 이동하는 로직이 필요함
# 이동하려는 위치가 벽을 만나거나, 이미 방문한 칸이면 방향을 변경

# 위치 백터
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
direction = 0
num = 0 # 대각선의 개수
cnt = 1 # 방문한 칸 개수 (시작점 제외)
route[x][y] = "ㅇ"  # 시작점 방문 표시

while cnt < M * N:
    nx, ny = x + dx[direction], y + dy[direction]

    # 방향 꺾는 경우
    if not (0 <= nx < M and 0 <= ny < N) or route[nx][ny] != "?":
        direction = (direction + 1) % 4
        num += 1
        nx, ny = x + dx[direction], y + dy[direction]

    route[nx][ny] = "-"
    x, y = nx, ny
    cnt += 1

print(num)