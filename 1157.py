# title: 단어 공부

# 알파벳 대소문자로 된 단어가 주어진다.
# 가장 많이 사용된 알파벳이 무엇인지 알아내 해당 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

input_lower = input().lower()                   # 소문자 만들기
no_duplicate_list = list(set(input_lower))      # 중복 제거된 요소들의 리스트 만들기
cnt = []                                        

for i in no_duplicate_list:         # 중복 제거된 리스트 안의 요소 하나하나에 대해서 
    count = input_lower.count(i)    # 소문자 변환만 된 단어 안에 해당 요소가 몇 개 있는지 세기
    cnt.append(count)               # no_duplicate_list 안의 각 요소들이 반복된 개수를 리스트 안에 넣어주기

if cnt.count(max(cnt)) >= 2:        # 가장 많이 사용된 알파벳이 2개 이상일 때
    print("?")
else:                               # 가장 많이 사용된 알파벳이 오직 하나일 때
    print(no_duplicate_list[cnt.index(max(cnt))])

# print("각 알파벳의 개수", cnt)
# print("각 알파벳의 개수 중 가장 큰 수", max(cnt))
# print("각 알파벳의 개수 중 가장 큰 수가 몇 개 있는가 세기", cnt.count(max(cnt)))
# print("각 알파벳의 개수 중 가장 큰 수가 어느 인덱스에 있는가 알아보기", cnt.index(max(cnt)))