# 2578: 빙고

'''
입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 
여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 
빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.
'''

'''
1. 사회자가 부르는 숫자를 하나씩 찾아 해당 좌표를 체크(0으로 표시)
2. 매 호출마다 빙고 개수 체크(0이 가로,세로,대각선으로 놓인 것)
3. 3개 이상이 되면 종료
'''

# 빙고판에 쓰여진 수
board = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 수
speaker = sum([list(map(int, input().split())) for _ in range(5)], [])

cnt = 0 # 호출 횟수
bingo = 0 # 빙고 개수 

# 숫자의 위치를 빠르게 찾기 위한 딕셔너리 생성
pos = {board[i][j]: (i, j) for i in range(5) for j in range(5)}

# 2. 빙고 개수 체크 로직 구현
def checkBingo():
    bingoCnt = 0
    for i in range(5):
        # 가로 체크
        if all(board[i][j] == 0 for j in range(5)):
            bingoCnt += 1
        # 세로 체크
        if all(board[j][i] == 0 for j in range(5)):
            bingoCnt += 1
    # 대각선 체크
    if all(board[i][i] == 0 for i in range(5)): 
        bingoCnt += 1
    if all(board[i][4 - i] == 0 for i in range(5)):
        bingoCnt += 1
    return bingoCnt
    
# 1. 사회자가 부르는 숫자를 하나씩 처리
for num in speaker:
    cnt += 1
    x, y = pos[num]  # 숫자의 위치 찾기
    board[x][y] = 0  # 숫자를 0으로 변경
    bingo = checkBingo()  # 빙고 개수 확인
    
    # 3. 3개 이상 되면 종료 & 호출 횟수 출력
    if bingo >= 3:
        print(cnt)
        break