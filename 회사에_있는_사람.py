# 7785: 회사에 있는 사람

'''
첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 106) 
다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. 
"enter"인 경우는 출근, "leave"인 경우는 퇴근이다.

회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다. 
사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열이다.

현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.
'''

# 시간초과 오류
'''
import sys
input = sys.stdin.readline

n = int(input())
people = []

for _ in range(n):
    log = input().split()

    if log[1] == "enter":
        people.append(log[0])
    elif log[1] == "leave":
        people.remove(log[0])


for elem in sorted(people, reverse=True):
    print(elem)
'''

# 리스트 말고 딕셔너리 set() 사용할 것
import sys
input = sys.stdin.readline

n = int(input())
company = set()

for _ in range(n):
    log = input().split()

    if log[1] == "enter":
        company.add(log[0])
    elif log[1] == "leave":
        company.remove(log[0])

answer = list(company)

for elem in sorted(answer, reverse=True):
    print(elem)