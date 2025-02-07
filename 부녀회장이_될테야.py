# 2775: 부녀회장이 될테야

'''
입력
첫 번째 줄에 Test case의 수 T가 주어진다. 
그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

출력
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.
'''

def people(k, n, memo={}):
    if k == 0: # 0층의 n호는 n명씩
        return n 
    if n == 1: # 모든 층의 1호는 1명
        return 1
    if (k, n) in memo:  # 이미 계산한 값이면 바로 반환
        return memo[(k, n)]
    
    # 새로 계산 후 저장
    memo[(k, n)] = people(k-1, n, memo) + people(k, n-1, memo)
    return memo[(k, n)]

T = int(input())
for _ in range(T):
    k = int(input())  
    n = int(input())  
    print(people(k, n)) 

# ---------------------------

def people(k, n):
    dp = [[i for i in range(n+1)] for _ in range(k+1)]

    for floor in range(1, k+1):
        for room in range(1, n+1):
            dp[floor][room] = dp[floor][room-1] + dp[floor-1][room]
    
    return dp[k][n]

T = int(input())
for _ in range(T):
    k = int(input())  
    n = int(input())  
    print(people(k, n))