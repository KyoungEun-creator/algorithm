# 1181: 단어 정렬

# 첫째 줄에 단어의 개수 N이 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거한다. 
# 논리: 중복제거 -> 사전순 나열 -> 길이순(짧-긴) 나열

N = int(input())

# 1. 알파벳 소문자로 이루어진 N개의 단어 받음
words = []
for i in range(N):
    words.append(input())
# words = [str(input()) for i in range(N)]

# 2. 중복이 사라진 단어 리스트 
no_dup = list(set(words))

# 3. 사전 순으로 나열
no_dup.sort()

# 4. 길이 순으로 나열
no_dup.sort(key = len)

# 원소 하나씩 프린트
for elem in no_dup:
    print(elem)