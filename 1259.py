# 여러 개의 테스트 케이스를 입력 받음: n = input()
# 입력의 마지막 줄에는 0이 주어짐
# 팰린드롬수면 'yes', 아니면 'no'를 출력

# 문자열로 입력받음
# 문자열 뒤집기 [::-1] 
# 문자열을 뒤집어도 기존 문자열과 같아야 팰린드롬수가 됨

while True:
    n = input()
    if n == '0':
        break
    elif n == n[::-1]:
        print('yes')
    else:
        print('no')
