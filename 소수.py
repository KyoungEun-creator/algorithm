# 2581: 소수

'''
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
'''

M = int(input())
N = int(input())
arr = [] 

for i in range(M, N+1): 
    num = 0
    for j in range(1, i+1):
        if i % j == 0:
            num += 1
    if num == 2:
        arr.append(i)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
         

# old
M = int(input())
N = int(input())

# 소수를 담을 리스트 
arr = []

for i in range (M, N + 1):
    # 약수의 개수 
    num = 0     
    for j in range (1, i + 1):
        if i % j == 0:
            num += 1
    if num == 2:
        arr.append(i)

if len(arr) == 0:
    print("-1")
else:
    print(sum(arr))
    print(min(arr))