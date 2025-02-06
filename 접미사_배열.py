# 11656: 접미사

'''
입력
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.

출력
첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.
'''

S = input()
dictionary = []
# print(len(S))
# print(S[7:8])

for i in range(len(S)): # 0~7
    dictionary.append(S[i:len(S) + 1])
# print(sorted(dictionary))

for elem in sorted(dictionary):
    print(elem)
    