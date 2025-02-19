# 2840: 행운의 바퀴

'''
입력
첫째 줄에 바퀴의 칸의 수 N과 상덕이가 바퀴를 돌리는 횟수 K가 주어진다. (2 ≤ N ≤ 25, 1 ≤ K ≤ 100)

다음 줄부터 K줄에는 바퀴를 회전시켰을 때 화살표가 가리키는 글자가 몇 번 바뀌었는지를 나타내는 S와 회전을 멈추었을 때 가리키던 글자가 주어진다. (1 ≤ S ≤ 100)

출력
첫째 줄에 '마지막 회전에서 화살표가 가리키는 문자부터' 시계방향으로 바퀴에 적어놓은 알파벳을 출력한다. 
이때, 어떤 글자인지 결정하지 못하는 칸은 '?'를 출력한다. 
만약, 상덕이가 적어놓은 종이에 해당하는 행운의 바퀴가 없다면 "!"를 출력한다. 
'''

N, K = list(map(int, input().split()))
chances = []

for _ in range(K):
    num, char = input().split()
    num = int(num)
    chances.append([num, char])
# print(chances) # [[1, 'A'], [2, 'B'], [3, 'C']]

wheel = ["?"] * N
cur_position = 0 # 처음 시작하는 화살표 위치
used_chars = set()  # 이미 사용된 문자들을 저장할 집합

for r, char in chances:
    cur_position = (cur_position - r) % N # 바퀴의 인덱스

    # 이미 해당 위치에 다른 문자가 들어가 있을 경우
    if wheel[cur_position] != "?" and wheel[cur_position] != char:
        print("!")
        exit()

    # 만약 다른 곳에서 사용된 문자가 이 위치에 들어가 있을 경우
    if char in used_chars and wheel[cur_position] != char:
        print("!")
        exit()

    # 문제 없으면 값 저장
    wheel[cur_position] = char
    used_chars.add(char)  # 사용된 문자 기록

print("".join(wheel[cur_position:] + wheel[:cur_position]))