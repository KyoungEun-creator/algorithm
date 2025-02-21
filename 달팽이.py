# 1913: 달팽이

'''
홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.
입력
첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다. 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.

출력
N개의 줄에 걸쳐 표를 출력한다. 
각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며, 자릿수를 맞출 필요가 없다. 
N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.

'''

N = int(input())
question = int(input()) # 좌표를 구하고자 하는 숫자
route = [["?"] * N for _ in range(N)]

# 위치 백터 (하, 우, 상, 좌)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

direction = 0
x, y = 0, 0
calc = 1

# 시작점
route[0][0] = N ** 2
route[N // 2][N // 2] = 1

cnt = 1 # 방문한 칸 개수 (시작점 제외)

while cnt < N ** 2:
    nx, ny = x + dx[direction], y + dy[direction]

    # 방향 꺾는 경우 (범위를 넘어가거나 "?"가 아니면)
    if not (0 <= nx < N and 0 <= ny < N) or route[nx][ny] != "?":
        direction = (direction + 1) % 4
        nx, ny = x + dx[direction], y + dy[direction]
    
    route[nx][ny] = N ** 2 - calc
    calc += 1 # 하나씩 작아진다
    x, y = nx, ny
    cnt += 1

# 표 출력
for row in route:
    print(" ".join(map(str, row)))

# 좌표 출력
for i in range(N):
    for j in range(N):
        if route[i][j] == question:
            print(i+1, j+1)
            break