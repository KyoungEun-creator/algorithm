# 2161: 카드1

'''
입력
첫째 줄에 정수 N(1 ≤ N ≤ 1,000)이 주어진다.

출력
첫째 줄에 버리는 카드들을 순서대로 출력한다. 제일 마지막에는 남게 되는 카드의 번호를 출력한다.
'''

N = int(input())

q = []
res = []

for i in range(1, N+1):
    q.append(i)
   
while len(q) > 1:
    # 첫 번째 요소를 제거하고 동시에 반환 받아 res에 추가함
    res.append(q.pop(0)) 
    # 첫 번째 요소를 제거하고 동시에 q의 마지막에 추가함
    q.append(q.pop(0))
    

print(*res, q[0])
