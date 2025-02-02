# 13305: 주유소

'''
입력
첫 번째 줄에는 도시의 개수를 나타내는 정수 N(2 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 인접한 두 도시를 연결하는 도로의 길이가 제일 왼쪽 도로부터 N-1개의 자연수로 주어진다. 
다음 줄에는 주유소의 리터당 가격이 제일 왼쪽 도시부터 순서대로 N개의 자연수로 주어진다. 
제일 왼쪽 도시부터 제일 오른쪽 도시까지의 거리는 1이상 1,000,000,000 이하의 자연수이다. 
리터당 가격은 1 이상 1,000,000,000 이하의 자연수이다. 

출력
표준 출력으로 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용을 출력한다. 
'''

N = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

minPrice = price[0]
cost = 0
for i in range(N-1): 
    if minPrice > price[i]:
        minPrice = price[i]
    cost += (minPrice * km[i])

print(cost)