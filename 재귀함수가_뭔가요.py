# 17478: 재귀함수가 뭔가요?

'''
입력
교수님이 출력을 원하는 재귀 횟수 N(1 ≤ N ≤ 50)이 주어진다.

출력
출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답을 출력한다.
'''

N = int(input())

def chatbot(n, depth=0):
    indentation = "____" * depth
    print(indentation + '"재귀함수가 뭔가요?"')
    if n == 0:
        print(indentation + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print(indentation + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(indentation + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(indentation + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        chatbot(n-1, depth+1)
    print(indentation + "라고 답변하였지.")
    
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
chatbot(N)