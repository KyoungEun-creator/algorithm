# title: 블랙잭

# 첫째 줄에 카드의 개수 N과 M이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0

for i in range (N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if numbers[i] + numbers[j] + numbers[k] > M:
                continue 
            else:
                result = max(result, numbers[i] + numbers[j] + numbers[k])

print(result)


