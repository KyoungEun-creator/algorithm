# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력
# 첫 줄에 수의 개수 N
# 다음으로 N개의 수가 주어짐

N = int(input())
nums = list(map(int, input().split()))

answer = 0  # 소수의 개수

for num in nums:
    cnt = 0     # 약수의 개수

    # 소수의 조건 (1)
    if num > 1:
        for i in range(2, num):
            if num % i == 0: 
                cnt += 1
        # 소수의 조건 (2)
        if cnt == 0:
            answer += 1

print(answer)

# 소수의 조건: (1) 1보다 커야함. (2) 1과 자기자신을 제외한 약수가 없어야 함.

