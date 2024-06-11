# 10814: 나이순 정렬

'''
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 
이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 
입력은 가입한 순서로 주어진다.

첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 
나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.
'''

N = int(input())
members = []

# N번만큼 입력받기
for i in range(N):
    age, name = input().split()
    age = int(age)
    members.append((age, name, i))

# age: member[0]
# name: member[1]
# 입력순서: member[2]

# age, 입력순서에 따라 오름차순 정렬
members.sort(key=lambda member: (member[0], member[2]))
# members == [(20, 'Sunyoung', 2), (21, 'Junkyu', 0), (21, 'Dohyun', 1)]

for member in members:
    print(member[0], member[1])