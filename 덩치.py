# 7568: 덩치

'''
첫 줄에는 전체 사람의 수 N이 주어진다. 
그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.
입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 
단, 각 덩치 등수는 공백문자로 분리되어야 한다.
'''

N = int(input())

# [몸무게, 키]에 대한 2차원 배열
people = []
for _ in range(N):
    arr = list(map(int, input().split()))
    people.append(arr)

# 등수 리스트
ranks = [1] * N

for i in range(N):
    for j in range(N):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                ranks[i] += 1

for elem in ranks:
    print(elem, end=" ")