# 4796: 캠핑

'''
입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 
각 테스트 케이스는 한 줄로 이루어져 있고, L, P, V를 순서대로 포함하고 있다. 모든 입력 정수는 int범위이다. 
마지막 줄에는 0이 3개 주어진다.

출력
각 테스트 케이스에 대해서, 강산이가 캠핑장을 최대 며칠동안 사용할 수 있는지 예제 출력처럼 출력한다.
'''

case = 1
while True:
   
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    days = L * (V // P) + min(V % P, L)
    sentence =  "Case %d: %d" % (case, days)

    print(sentence)
    case += 1
    
   