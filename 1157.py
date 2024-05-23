# title: 단어 공부

# 알파벳 대소문자로 된 단어가 주어진다.
# 가장 많이 사용된 알파벳이 무엇인지 알아내 해당 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 일단 전부 소문자로 바꾸기 
small = input().lower()
# 중복을 제거한 요소들의 리스트로 바꾸기 
no_dup = list(set(small))
# 중복을 제거한 요소 하나하나가 단어(전부 소문자) 내에서 몇 번 사용되었는지 세기
# 그렇게 센 개수에 대한 리스트 변수cnt 만들어주기
cnt = []
for elem in no_dup:
    count = small.count(elem)
    cnt.append(count)
# cnt 안에서 가장 큰 수 찾기 max(cnt)
# cnt 안에서 가장 큰 수의 개수 세기 cnt.count(max(cnt))
# cnt 안에서 가장 큰 수의 개수가 2개 이상이면 ? 출력하기
if cnt.count(max(cnt)) >= 2:
    print("?")
# 그렇지 않을 경우, cnt 안에서 가장 큰 수가 위치한 인덱스 찾기 cnt.index(max(cnt)
# no_dup 리스트 안에서 동일 인덱스에 해당하는 요소 추출하기 no_dup[cnt.index(max(cnt))]
# 해당 알파벳 대문자로 변환하기
else:
    print(no_dup[(cnt.index(max(cnt)))].upper())
    
