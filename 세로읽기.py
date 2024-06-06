# 10798: 세로읽기

# 총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다. 
# 주어지는 글자는 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’ 중 하나이다. 각 줄의 시작과 마지막에 빈칸은 없다.
# 영석이가 세로로 읽은 순서대로 글자들을 출력한다. 이때, 글자들을 공백 없이 연속해서 출력한다. 
# 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다. 

lines = []
length = [] 
answer = ''

# 단어를 5개 입력받아 리스트에 저장할 것
for _ in range(5):
    word = input()
    lines.append(word)
    length.append(len(word))

for j in range(max(length)):    # 열의 개수 (최대는 단어의 최대 길이와 동일)
    for i in range(5):          # 행
        if j < length[i]:       # j가 length[i], 즉 index 범위를 벗어난다면 글자를 추가하지 않음 
            answer += lines[i][j]

print(answer)