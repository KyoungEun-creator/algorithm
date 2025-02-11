# 1213: 팰린드롬 만들기

'''
입력
첫째 줄에 임한수의 영어 이름이 있다. 
알파벳 대문자로만 된 최대 50글자이다.

출력
첫째 줄에 문제의 정답을 출력한다. 
만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다. 
정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.
'''

import sys
from collections import Counter
# ABACABA
word = list(map(str, sys.stdin.readline().strip())) # ['A', 'B', 'A', 'C', 'A', 'B', 'A']
word.sort() # ['A', 'A', 'A', 'A', 'B', 'B', 'C',]

check = Counter(word) # Counter({'A': 4, 'B': 2, 'C': 1})
cnt = 0 # 홀수의 개수
center = "" # 홀수의 문자
half = ""

for char, count in check.items():  # check.items()에서 char는 문자, count는 해당 문자의 개수
    if count % 2 != 0:
        cnt += 1
        center = char
    # 팰린드롬의 절반을 만드는 과정
    half += char * (count // 2)
   
    # 홀수의 개수가 1보다 크면 팰린드롬이 불가함!!
    if cnt > 1:
        print("I'm Sorry Hansoo")
        exit()

# 팰린드롬 생성
print(half + center + half[::-1])
