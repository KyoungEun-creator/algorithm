# 2501: 약수 구하기

# 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.
# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.

N, K = map(int, input().split())

# N의 약수들을 담은 리스트
arr = []
for i in range (1, N + 1):
    if N % i == 0:
        arr.append(i)

if len(arr) >= K:
    print(arr[K - 1])
else:
    print(0)